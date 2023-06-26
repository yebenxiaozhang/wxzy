"""
======================
Author: 潘师傅
Time: 2023-06-26 11:09
Project: yinlian
Company: 无限主义
======================
"""
import datetime
import math
import time

from Common.handle_requests import send_requests
from Common.handle_config import conf
from jsonpath import jsonpath


class commonApi:

    def __init__(self):
        pass

    def login(self, user, password):
        """
        登录
        :param user: 用户名
        :param password: 加密过后的密码
        :return:
        """
        res = send_requests(method='post', url='api/login',
                            data={
                                "username": user,
                                "password": password
                            }, data_type=2)
        return res




d = commonApi()
d.login(user='admin', password='admin123')





