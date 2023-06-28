"""
======================
Author: 潘师傅
Time: 2023-06-27 17:28
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
from jsonpath import jsonpath



class PartitionIntegral(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        logger.info('获取最新id')
        cls.yinlian = yinlian()
        res = cls.yinlian.getBlindbox(activity_type=2)
        cls.lind_box_Id = jsonpath(res.json(), '$.data.id')[0]
        logger.info('最新翻牌活动id为:' + str(cls.lind_box_Id))
        cls.db = HandleDB()
        # 运行前数据的清洗？？？？？？？？？？？？？？？？？

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('关闭游标、关闭数据库链接')
        cls.db.close()


    def test_001(self):
        """签到3，6，7，翻牌"""
        current_date = time.strftime('%Y-%m-%d')        # 获取当前日期的字符串表示
        # 构建 SQL 查询语句，将日期模式拼接到 LIKE 子句中
        sql = f"""UPDATE mkt_blindbox_task SET deleted = 1 WHERE user_id = '{conf.get('token', 'user_id')}' 
                 AND blindbox_id = '{self.lind_box_Id}' AND deleted = 0 AND create_time LIKE '{current_date}%'"""
        sql1 = f"""UPDATE mkt_blindbox_lottery SET deleted = 1 WHERE user_id = '{conf.get('token', 'user_id')}' 
                 AND blindbox_id = '{self.lind_box_Id}' AND deleted = 0 AND create_time LIKE '{current_date}%'"""
        self.db.update(sql)
        self.db.update(sql1)

        # res = self.yinlian.sign_flip(blind_box_id=self.lind_box_Id,token=conf.get('token', 'token'))
        # draw_number =  jsonpath(res.json(), '$.data')[0]
        # if draw_number == 1:
        #     self.yinlian.sign_lottery(blind_box_id=self.lind_box_Id,token=conf.get('token', 'token'))