"""
======================
Author: 潘师傅
Time: 2023-06-26 16:20
Project: yinlian
Company: 无限主义
======================
"""

import unittest
import time

from Common.my_logger import logger
from Common.yinlian_api import yinlian
from Common.handle_config import conf
from Common.handle_db import HandleDB
from ddt import ddt,data
from jsonpath import jsonpath

@ddt
class draw(unittest.TestCase):

    yinlian = None

    @classmethod
    def setUpClass(cls) -> None:
        """获取最新活动id"""
        logger.info('************ 翻牌模块用例 开始执行 ************')
        cls.yinlian = yinlian()
        logger.info('现在进行获取最新翻牌活动id')
        res = cls.yinlian.getBlindbox(activity_type=2)
        cls.lind_box_Id = jsonpath(res.json(), '$.data.id')[0]
        logger.info('最新翻牌活动id为: {}'.format(cls.lind_box_Id))
        logger.info('数据库清理数据')
        db = HandleDB()  # 建立数据库连接
        try:
            logger.info('现在更新第一张表')
            current_date = time.strftime('%Y-%m-%d')  # 获取当前日期的字符串表示
            # 构建 SQL 查询语句，使用参数化查询
            sql = f"""DELETE FROM mkt_blindbox_lottery WHERE user_id = '{conf.get('token', 'user_id')}' 
                       AND blindbox_id = '{cls.lind_box_Id}' AND create_time LIKE '{current_date}%'"""
            db.update(sql)
            logger.info('现在更新第二张表')
            sql = f"""DELETE FROM mkt_blindbox_task WHERE user_id = '{conf.get('token', 'user_id')}' 
                       AND blindbox_id = '{cls.lind_box_Id}' AND create_time LIKE '{current_date}%'"""
            db.update(sql)
            logger.info('本次测试所需的表更新完毕，现在开始测试')
        except Exception as e:
            logger.error(f'数据库操作发生异常: {str(e)}')
        finally:
            db.close()  # 关闭数据库连接

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     logger.info('关闭游标、关闭数据库链接')
    #     cls.db.close()

    @data(2,6)
    def test_001_tasksDraw(self, get_type):
        """做任务进行抽奖"""
        logger.info('做任务获取翻牌次数，目前使用增加翻牌类型为 {}'.format(get_type))
        res = self.yinlian.blindboxaddLottery(get_type=get_type, auth_token=conf.get('token', 'token'),
                                              app_id=conf.get('appId', 'fpappId'))
        draw_number = jsonpath(res.json(), '$.data')[0]
        logger.info('获取翻牌次数为 {}'.format(draw_number))
        if draw_number == 0:
            self.assertEqual(1,draw_number, msg='本次分享未获得翻牌次数！因开始前清理过数据库，故应取得次数')
        else:
            logger.info('本次分享获得翻牌次数: {}'.format(draw_number))


            logger.info('获得翻牌次数后与活动详情是否一致？')
            number = self.get_lottery_number()
            self.assertEqual(int(draw_number), int(number))
            logger.info('获得翻牌次数后与获得详情一致')


            logger.info('抽奖，获取奖励id')
            res = self.wait_for_result(self.yinlian.blindboxIdlottery, blind_box_id=self.lind_box_Id,
                                       auth_token=conf.get('token', 'token'), app_id=conf.get('appId', 'fpappId'))
            drawid = jsonpath(res.json(), '$.data.id')[0]
            prizeType = jsonpath(res.json(), '$.data.prizeType')[0]
            logger.info('获取到本次中奖的id为：{}'.format(drawid))


            logger.info('现在进行读取中奖记录，并且获取集合')
            res = self.wait_for_result(self.yinlian.my_Winning_record, blind_box_id=self.lind_box_Id,
                                       token=conf.get('token', 'token'), app_id=conf.get('appId', 'fpappId'))
            drawdata = jsonpath(res.json(), '$.data..id')
            logger.info('已读取到中奖记录前10到id集合为: {}'.format(drawdata))


            logger.info('现在进行中奖信息进行对比')
            if int(prizeType) != 5:
                logger.info('现在模拟已中奖：需展示在中奖记录中')
                self.assertIn(drawid, drawdata)
                logger.exception("中奖信息与中奖记录核对上了，pass")
            else:
                logger.info('现在模拟结果为未中奖：不展示在中奖记录中')
                self.assertNotIn(drawid, drawdata)
                logger.exception("中奖信息与中奖记录核对上了，pass")


            logger.info('抽奖结束后，查看抽奖次数是否减少')
            number = self.get_lottery_number()
            self.assertEqual(draw_number-1, number, msg='抽奖次数未减少')

    @data(2,6)
    def test_repetition_draw_get_lottery(self, get_type):
        """重复做任务，是否有获取翻牌次数"""
        logger.info('获取抽奖次数信息')
        res = self.yinlian.blindboxInfo(blindbox_id=str(self.lind_box_Id), auth_token=conf.get('token', 'token'),
                                        app_id=conf.get('appId', 'fpappId'))
        number = jsonpath(res.json(), '$.data.lotteryNum')[0]
        logger.info('翻牌次数为: {}'.format(number))


        logger.info('获取任务类型: {} 开始进行做任务'.format(get_type))
        res = self.yinlian.blindboxaddLottery(get_type=get_type, auth_token=conf.get('token', 'token'),
                                              app_id=conf.get('appId', 'fpappId'))
        draw_number = jsonpath(res.json(), '$.data')[0]
        logger.info('做任务取得次数为: {}'.format(draw_number))


        logger.info('进行数据比较')
        self.assertEqual(draw_number, number, msg='重复获取应为0')
        logger.info('数据对比ok')


    def test_001(self):
        """每人中奖次数/每日抽奖次数等！！"""

    def wait_for_result(self, method, *args, **kwargs):
        """等待接口请求结果"""
        res = method(*args, **kwargs)
        while 'success' != jsonpath(res.json(), '$.msg')[0]:
            res = method(*args, **kwargs)
            time.sleep(0.5)
        return res

    def get_lottery_number(self):
        """获取抽奖次数"""
        res = self.yinlian.blindboxInfo(blindbox_id=str(self.lind_box_Id), auth_token=conf.get('token', 'token'),
                                        app_id=conf.get('appId', 'fpappId'))
        return jsonpath(res.json(), '$.data.lotteryNum')[0]

