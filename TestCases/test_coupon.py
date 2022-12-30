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
from Common.handle_db import HandleDB
from Common.handle_config import conf
from jsonpath import jsonpath
from Common.common_api import login
from Common.common_api import coupon
from Common.common_api import time_add

# he = HandleExcel(datas_dir+"/api_cases.xlsx", "优惠券")
# cases = he.read_all_datas()
# he.close_file()


class TestCoupon(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        用例开始前的准备：例如先登录
        :return:
        """
        res = login(user=conf.get('admin', 'user'), password=conf.get('admin', 'password'))
        cls.token = jsonpath(res.json(), '$.access_token')[0]

    def test_coupon(self):
        x, y = time_add(minutes=2)
        res = coupon(token=self.token,
                     appType=1, couponName='我是优惠券名称', couponType=1, useType=0, appId='5',
                     startTime='2022-12-29 00:00:00', endTime='2022-12-29 23:59:59',
                     useStartTime='2022-12-29 00:00:00', useEndTime='2022-12-29 23:59:59',
                     description='我是备注', offsetAmount=1, publishNum=999)
        time.sleep(1)
        print(res)

