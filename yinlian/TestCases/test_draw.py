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
        res = cls.yinlian.getBlindbox(activityType=2)
        cls.lindboxId = jsonpath(res.json(), '$.data.id')[0]
        logger.info('最新翻牌活动id为:' + str(cls.lindboxId))

    @data(2,6)
    def test_001_tasksDraw(self,get_type):
        """做任务进行抽奖"""
        logger.info('做任务获取翻牌次数，目前使用增加翻牌类型为 {}'.format(get_type))
        res = self.yinlian.blindboxaddLottery(gettpye=get_type, token=conf.get('token', 'token'),
                                              appId=conf.get('appId', 'fpappId'))
        draw_number = jsonpath(res.json(), '$.data')[0]
        logger.info('获取翻牌次数为 {}'.format(draw_number))
        if draw_number == 0:
            logger.info('本次分享未获得翻牌次数！！！！！！！如何进行判断今天分享过了没有？？？？未做判断！！！')
        else:
            logger.info('本次分享获得翻牌次数: {}'.format(draw_number))


            logger.info('获得翻牌次数后与活动详情是否一致？')
            number = self.get_lottery_number()
            self.assertEqual(int(draw_number), int(number))
            logger.info('获得翻牌次数后与获得详情一致')

            # try:
            #     res = self.yinlian.blindboxInfo(blindboxId=str(self.lindboxId), token=conf.get('token', 'token'),
            #                                      appId=conf.get('appId', 'fpappId'))
            #     number = jsonpath(res.json(), '$.data.lotteryNum')[0]
            #     self.assertEqual(int(draw_number), int(number))
            #     logger.info('获得翻牌次数后与获得详情一致')
            # except AssertionError:
            #     logger.exception("断言失败！获得翻牌次数后与获得详情不一致")
            #     logger.exception("获得详情翻牌次数为： " + str(number))
            #     raise


            logger.info('抽奖，获取奖励id')
            res = self.wait_for_result(self.yinlian.blindboxIdlottery, blindboxId=str(self.lindboxId),
                                       token=conf.get('token', 'token'), appId=conf.get('appId', 'fpappId'))
            drawid = jsonpath(res.json(), '$.data.id')[0]
            prizeType = jsonpath(res.json(), '$.data.prizeType')[0]
            logger.info('获取到本次中奖的id为：{}'.format(drawid))

            # logger.info('现在进行抽奖并且获取中奖id')
            # res = self.yinlian.blindboxIdlottery(blindboxId=str(self.lindboxId), token=conf.get('token', 'token'),
            #                                      appId=conf.get('appId', 'fpappId'))
            # # 请求后不一定就会出结果，可能是您正在抽奖之中,请稍候，所以每间隔0。5秒进行请求一次
            # while 'success' != jsonpath(res.json(), '$.msg')[0]:
            #     res = self.yinlian.blindboxIdlottery(blindboxId=str(self.lindboxId), token=conf.get('token', 'token'),
            #                                          appId=conf.get('appId', 'fpappId'))
            #     time.sleep(0.5)
            # drawid = jsonpath(res.json(), '$.data.id')[0]
            # prizeType = jsonpath(res.json(), '$.data.prizeType')[0]
            # logger.info('获取到本次中奖的id为：' + str(drawid))


            logger.info('现在进行读取中奖记录，并且获取集合')
            res = self.wait_for_result(self.yinlian.myblindboxlottery, blindboxId=str(self.lindboxId),
                                       token=conf.get('token', 'token'), appId=conf.get('appId', 'fpappId'))
            drawdata = jsonpath(res.json(), '$.data..id')
            logger.info('已读取到中奖记录前10到id集合为: {}'.format(drawdata))

            # logger.info('现在进行读取中奖记录。并且获取集合')
            # res = self.yinlian.myblindboxlottery(blindboxId=str(self.lindboxId), token=conf.get('token', 'token'),
            #                                      appId=conf.get('appId', 'fpappId'))
            # # 请求后不一定就会出结果，可能是您正在抽奖之中,请稍候，所以每间隔0。5秒进行请求一次
            # while 'success' != jsonpath(res.json(), '$.msg')[0]:
            #     res = self.yinlian.myblindboxlottery(blindboxId=str(self.lindboxId),
            #                                          token=conf.get('token', 'token'),
            #                                          appId=conf.get('appId', 'fpappId'))
            #     time.sleep(0.5)
            # # 如果接口返回是0的结果没有进行判断
            # drawdata = jsonpath(res.json(), '$.data..id')
            # logger.info('已读取到中奖记录前10到id集合为' + str(drawdata))

            logger.info('现在进行中奖信息进行对比')
            if int(prizeType) != 5:
                logger.info('现在模拟已中奖：需展示在中奖记录中')
                self.assertIn(drawid, drawdata)
                logger.exception("中奖信息与中奖记录核对上了，pass")
            else:
                logger.info('现在模拟结果为未中奖：不展示在中奖记录中')
                self.assertNotIn(drawid, drawdata)
                logger.exception("中奖信息与中奖记录核对上了，pass")

            # logger.info('现在进行中奖信息进行对比')
            # if int(prizeType) != 5:
            #     logger.info('现在模拟已中奖：需展示在中奖记录中')
            #     try:
            #         self.assertIn(drawid, drawdata)
            #         logger.exception("中奖信息与中奖记录核对上了，pass")
            #     except AssertionError:
            #         logger.exception("断言失败！刚抽中的奖励没有在中奖记录中显示，或中奖记录没有根据中奖时间倒序排列")
            #         raise
            #
            # else:
            #     logger.info('现在模拟结果为未中奖：不展示在中奖记录中')
            #     try:
            #         self.assertNotIn(drawid, drawdata)
            #         logger.exception("中奖信息与中奖记录核对上了，pass")
            #     except AssertionError:
            #         logger.exception("断言失败！刚抽中的奖励没有在中奖记录中显示，或中奖记录没有根据中奖时间倒序排列")
            #         raise


            logger.info('抽奖结束后，查看抽奖次数是否减少')
            number = self.get_lottery_number()
            self.assertEqual(draw_number-1, number, msg='抽奖次数未减少')

            # logger.info('抽奖结束后，查看抽奖次数是否减少')
            # try:
            #     res = self.yinlian.blindboxInfo(blindboxId=str(self.lindboxId), token=conf.get('token', 'token'),
            #                                      appId=conf.get('appId', 'fpappId'))
            #     number = jsonpath(res.json(), '$.data.lotteryNum')[0]
            #     self.assertEqual(draw_number-1, number)
            # except AssertionError:
            #     logger.exception("断言失败！获得翻牌次数后与获得详情不一致" + "获得详情翻牌次数为： " + str(number))
            #     raise


    @data(2,6)
    def test_repetition_draw_get_lottery(self, get_type):
        """重复做任务，是否有获取翻牌次数"""
        logger.info('获取抽奖次数信息')
        res = self.yinlian.blindboxInfo(blindboxId=str(self.lindboxId), token=conf.get('token', 'token'),
                                        appId=conf.get('appId', 'fpappId'))
        number = jsonpath(res.json(), '$.data.lotteryNum')[0]
        logger.info('翻牌次数为: {}'.format(number))


        logger.info('获取任务类型: {} 开始进行做任务'.format(get_type))
        res = self.yinlian.blindboxaddLottery(gettpye=get_type, token=conf.get('token', 'token'),
                                              appId=conf.get('appId', 'fpappId'))
        draw_number = jsonpath(res.json(), '$.data')[0]
        logger.info('做任务取得次数为: {}'.format(draw_number))


        logger.info('进行数据比较')
        self.assertEqual(draw_number, number, msg='重复获取应为0')
        logger.info('数据对比ok')


    def test_001(self):
        """抽到未中奖应不显示在中奖记录中"""

    def wait_for_result(self, method, *args, **kwargs):
        """等待接口请求结果"""
        res = method(*args, **kwargs)
        while 'success' != jsonpath(res.json(), '$.msg')[0]:
            res = method(*args, **kwargs)
            time.sleep(0.5)
        return res

    def get_lottery_number(self):
        """获取抽奖次数"""
        res = self.yinlian.blindboxInfo(blindboxId=str(self.lindboxId), token=conf.get('token', 'token'),
                                        appId=conf.get('appId', 'fpappId'))
        return jsonpath(res.json(), '$.data.lotteryNum')[0]

