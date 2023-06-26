"""
======================
Author: 潘师傅
Time: 2022-12-27 14:06
Project: wxzy
Company: 无限主义
======================
"""

import unittest
import json

from Common.handle_excel import HandleExcel
from Common.handle_requests import send_requests
from Common.handle_path import datas_dir
from Common.myddt import ddt, data
from Common.my_logger import logger
from Common.handle_db import HandleDB

he = HandleExcel(datas_dir+"/api_cases.xlsx", "运营后台登录")
cases = he.read_all_datas()
he.close_file()

# db = HandleDB()


@ddt
class TestLoginCMS(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info('************ 登录模块用例 开始执行 ************')

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('************ 登录模块用例 执行结束 ************')

    @data(*cases)
    def test_login(self, case):
        logger.info('************ 执行用例 {}:{} ************'.format(case['id'], case['title']))
        # 步骤 测试数据 - 发起请求
        response = send_requests(method=case['method'], url=case['url'], data=case['request_data'],
                                 data_type=case['data_type'])

        # 期望结果，从字符串转换成字典对象。
        expected = eval(case["expected"])
        res = response.json()
        # 断言 - code == 0 msg == ok
        logger.info("用例的期望结果为：{}".format(case["expected"]))
        try:
            if 'code' in res:
                self.assertEqual(response.json()['code'], expected['code'])
                self.assertEqual(response.json()['msg'], expected['msg'])
            else:
                self.assertEqual(response.status_code, expected['code'])
                self.assertEqual(response.json()['user_info']['phone'], expected['phone'])
            # 如果check_sql有值，说明要做数据库校验。
            # if case["check_sql"]:
            #     # logger.info()
            #     result = db.select_one_data(case["check_sql"])
            #     self.assertIsNotNone(result)
        except AssertionError:
            logger.exception("断言失败！")
            raise



