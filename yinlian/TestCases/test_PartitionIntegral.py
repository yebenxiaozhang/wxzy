"""
======================
Author: 潘师傅
Time: 2023-06-27 17:28
Project: yinlian
Company: 无限主义
======================
"""


import unittest
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
        sql = 'select * from mkt_blindbox_lottery'
        count = self.db.get_count(sql)
        print(count)
        # res = self.yinlian.sign_flip(blind_box_id=self.lind_box_Id,token=conf.get('token', 'token'))
        # draw_number =  jsonpath(res.json(), '$.data')[0]
        # if draw_number == 1:
        #     self.yinlian.sign_lottery(blind_box_id=self.lind_box_Id,token=conf.get('token', 'token'))