"""
======================
Author: 潘师傅
Time: 2022-12-29 15:06
Project: wxzy
Company: 无限主义
======================
"""

import unittest
import time
import json

from Common.handle_excel import HandleExcel
from Common.handle_requests import send_requests
from Common.handle_path import datas_dir
from Common.myddt import ddt, data
from Common.my_logger import logger
from Common.handle_data import replace_mark_with_data
from Common.handle_db import HandleDB
from Common.handle_config import conf
from jsonpath import jsonpath
from Common.common_api import *
from Common.handle_phone import get_new_phone

he = HandleExcel(datas_dir+"/api_cases.xlsx", "优惠券")
cases = he.read_all_datas()
he.close_file()


@ddt
class TestCoupon(unittest.TestCase):

    api = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api = commonApi()

    @classmethod
    def setUpClass(cls) -> None:
        """
        用例开始前的准备：例如先登录
        :return:
        """
        logger.info('************ 优惠券模块用例 开始执行 ************')
        cls.api = commonApi()
        res = cls.api.login(user=conf.get('admin', 'user'), password=conf.get('admin', 'password'))
        cls.token = jsonpath(res.json(), '$.access_token')[0]
        phone = get_new_phone()
        res = cls.api.login_mobile(user=phone)
        cls.user_token = jsonpath(res.json(), '$.data.access_token')[0]

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('************ 优惠券模块用例 执行结束 ************')

    @data(*cases)
    def test_coupon(self, case):
        """
        1. 新建优惠券 2. 获取优惠券ID 3. 领取优惠券
        :param case:
        :return:
        """
        # 替换
        if int(case['id']) > 1:
            res = self.api.coupon_list(token=self.token)
            couponId = jsonpath(res.json(), '$.data.rows[0].id')[0]
            receivedNum = jsonpath(res.json(), '$.data.rows[0].receivedNum')[0]
            if case["request_data"].find("#couponId#") != -1:
                case = replace_mark_with_data(case, '#couponId#', couponId)
                case = replace_mark_with_data(case, '#receivedNum#', receivedNum)
                case = replace_mark_with_data(case, '\n', '')

        logger.info('************ 执行用例 {}:{} ************'.format(case['id'], case['title']))
        # 字符串转化为字典
        expected = eval(case["request_data"])
        # expected = case["request_data"]
        x, y = self.api.add_time(minutes=case['minutes'])
        res = self.api.add_coupon(token=self.token, method=case['method'],
                                  couponName='优惠券' + x, appId=conf.get('user', 'appid'), startTime=x, endTime=y,
                                  perReceiveType=expected['perReceiveType'], perReceiveNum=expected['perReceiveNum'],
                                  publishNum=expected['publishNum'], receivedNum=expected['receivedNum'],
                                  useStatus=expected['useStatus'], couponDisplay=expected['couponDisplay'],
                                  couponId=expected['couponId'])
        # 期望结果，从字符串转换成字典对象。
        expected = eval(case["expected"])
        logger.info("用例的期望结果为：{}".format(case["expected"]))
        try:
            if 'code' in res.json():
                self.assertEqual(res.json()['code'], expected['code'])
            else:
                self.assertEqual(res.status_code, expected['code'])
        except AssertionError:
            logger.exception("断言失败！")
            raise

        if int(case['id']) >= 5:
            if int(case['id']) == 7:
                demo = self.api.time_difference(y=y)
                while int(demo) < 0:
                    time.sleep(0.5)
                    demo = self.api.time_difference(y=y)
            res = self.api.getCouponList(token=self.user_token, appid=conf.get('user', 'appid'))
            # 获取所有的ID，但会多获取应用ID ----- 待解决
            gather = jsonpath(res.json(), '$.data..id')
            res_1 = self.api.getGoodsCoupon(token=self.user_token, appid=conf.get('user', 'appid'), goodsId=conf.get('user', 'goodsId'))
            gather_1 = jsonpath(res_1.json(), '$..id')
            if gather is False:
                gather = '0'
            if gather_1 is False:
                gather_1 = '0'
            try:
                if int(case['expected_2']) == 1:
                    self.assertIn((eval(case["request_data"])['couponId']), gather)
                    self.assertIn((eval(case["request_data"])['couponId']), gather_1)
                else:
                    self.assertNotIn((eval(case["request_data"])['couponId']), gather)
                    self.assertNotIn((eval(case["request_data"])['couponId']), gather_1)
            except AssertionError:
                logger.exception("断言失败！")
                raise
        else:
            # 领取优惠券
            if int(case['id']) == 1:
                res = self.api.coupon_list(token=self.token)
                couponId = jsonpath(res.json(), '$.data.rows[0].id')[0]
            value = int((json.loads(case['request_data']))['perReceiveType'])
            while value >= 0:
                res = self.api.receiveCoupon(token=self.user_token, couponId=couponId)
                value = value - 1

            # 期望结果，从字符串转换成字典对象。
            expected = eval(case['expected_1'])
            logger.info("用例的期望结果为：{}".format(case["expected_1"]))
            try:
                if 'code' in res.json():
                    self.assertEqual(res.json()['code'], expected['code'])
                    self.assertEqual(res.json()['msg'], expected['msg'])
                else:
                    self.assertEqual(res.status_code, expected['code'])
            except AssertionError:
                logger.exception("断言失败！")
                raise

