# import unittest
# import os
# import json
#
# from Common.handle_requests import send_requests
# from Common.handle_excel import HandleExcel
# from Common.myddt import ddt, data
# from Common.handle_path import datas_dir
# from Common.my_logger import logger
# from Common.handle_db import HandleDB
# from Common.handle_phone import get_new_phone
# from Common.handle_data import replace_mark_with_data
#
#
# he = HandleExcel(datas_dir+"/api_cases.xlsx", "优惠券")
# cases = he.read_all_datas()
# he.close_file()
#
# db = HandleDB()
#
# @ddt
# class TestRegister(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         logger.info("======  注册模块用例 开始执行  ========")
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         logger.info("======  注册模块用例 执行结束  ========")
#
#     @data(*cases)
#     def test_register_ok(self, case):
#         # print("本条测试数据：",case)
#         logger.info("*********   执行用例{}：{}   *********".format(case["id"], case["title"]))
#
#         # 替换 - 动态 -
#         # 请求数据 #phone# 替换 new_phone
#         # check_sql里的  #phone# 替换 new_phone
#         print(case)
#         if case["request_data"].find("#couponId#") != -1:
#             case = replace_mark_with_data(case, "#couponId#", '79')
#
#         print(case)
#
#
# method = 'get'
# method = method.upper()  # 大写处理
# if method == "GET":
#     print('1')
# elif method == 'PUT':
#     print('2')
# else:
#     print('3')


# a = 0
#
# while a != 5:
#     print(a)
#     a = a + 1
#
