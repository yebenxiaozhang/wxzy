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
from typing import List, Dict
from Common.handle_requests import send_requests
from Common.handle_config import conf
from jsonpath import jsonpath


class yinlian:

    def __init__(self):
        pass

    def login(self, username: str, password: str) -> Dict:
        """
        登录
        :param username: 用户名
        :param password: 密码
        :return: 返回登录响应结果
        """
        data = {
            "username": username,
            "password": password
        }
        res = send_requests(method='post', url='api/login', data=data)
        return res

    def blindboxlist(self, token: str, activity_id: str = None, activity_name: str = None,
                     activity_status: int = None, status: int = None,
                     start_time: str = None, end_time: str = None,
                     page_num: int = 1, page_size: int = 10) -> Dict:
        """
        盲盒列表
        :param token: 认证令牌
        :param activity_id: 盲盒ID，精准查询
        :param activity_name: 盲盒名称，模糊查询
        :param activity_status: 活动状态 0未开始 1进行中 2已结束 3已停用
        :param status: 状态 0启用 1禁用
        :param start_time: 活动开始时间
        :param end_time: 活动结束时间
        :param page_num: 页码
        :param page_size: 每页显示数量
        :return: 返回盲盒列表的响应结果
        """
        data = {
            'id': activity_id,
            'activityName': activity_name,
            'activityStatus': activity_status,
            'status': status,
            'activityTime.startTime': start_time,
            'activityTime.endTime': end_time,
            'pageNum': page_num,
            'pageSize': page_size
        }
        res = send_requests(method='get', url='/api/blindbox/list', data=data, token=token)
        return res

    def blindboxchangestatus(self, blindbox_id: str, status: int, token: str) -> Dict:
        """
        启用/禁用盲盒
        :param blindbox_id: 盲盒ID
        :param status: 状态 0启用 1禁用
        :param token: 认证令牌
        :return: 返回启用/禁用盲盒的响应结果
        """
        url = f'/prod-api/blindbox/changeStatus/{blindbox_id}/{status}'
        res = send_requests(method='get', url=url, token=token)
        return res


    def blindbox(self, token):


        res  = send_requests(method='post', url='prod-api/blindbox', token=token,
                             data={
                                 "activityType": "1",
                                 "data": [{
                                     "userType": "普通用户",
                                     "drawRate": 20,
                                     "firstPointUse": 15,
                                     "memberPointUse": 10,
                                     "drawRateType": "1"
                                 }, {
                                     "userType": "62VIP用户",
                                     "drawRate": 20,
                                     "firstPointUse": 15,
                                     "memberPointUse": 20,
                                     "drawRateType": "2"
                                 }],
                                 "mktBlindboxPrizeList": [{
                                     "lotteryOdds": 30,
                                     "userLotteryLimit": 100,
                                     "prizeCount": 10000,
                                     "prizeType": "1",
                                     "couponItem": None,
                                     "prizeCode": "31020230411708631",
                                     "prizeName": "优惠券+1",
                                     "useExplain": "优惠券+2",
                                     "prizePic": "20230626/c0ab56f51ee346ec8c1eab912a5cdc5e.jpeg"
                                 }, {
                                     "prizeType": "3",
                                     "prizeName": "积点奖励+1",
                                     "prizePic": "20230626/c0ab56f51ee346ec8c1eab912a5cdc5e.jpeg",
                                     "prizeCount": 10000,
                                     "useExplain": "积点奖励+2",
                                     "lotteryOdds": 20,
                                     "userLotteryLimit": 100,
                                     "couponItem": None,
                                     "prizeCode": "770231685823467520"
                                 }, {
                                     "prizeType": "5",
                                     "prizeName": "为中奖+1",
                                     "prizePic": "20230626/c0ab56f51ee346ec8c1eab912a5cdc5e.jpeg",
                                     "prizeCount": 10000,
                                     "useExplain": "未中奖+2",
                                     "lotteryOdds": 40,
                                     "userLotteryLimit": 100,
                                     "couponItem": None,
                                     "prizeCode": "5"
                                 }],
                                 "mktBlindboxPrizeVipList": [{
                                     "lotteryOdds": 100,
                                     "userLotteryLimit": 100,
                                     "prizeCount": 1000,
                                     "prizeType": "2",
                                     "couponItem": None,
                                     "prizeCode": "1-1",
                                     "prizeName": "红包1-2",
                                     "useExplain": "红包1-3",
                                     "prizePic": "20230626/c0ab56f51ee346ec8c1eab912a5cdc5e.jpegg"
                                 }
                                 ],
                                 "activityName": "{{$timestamp}}",
                                 "activityRule": "活动规则\n活动规则\n活动规则",
                                 "activityTime": ["{{today_add_1}}", "{{today_add_2}}"],
                                 # "firstPrizeType": "1",
                                 "firstPrizeNum": 13,
                                 "firstPrizeCode": "优惠券1-1-1",
                                 "firstPrizeName": "优惠券1-1-2",
                                 "firstDescription": "优惠券1-1-3",
                                 "drawRateType": "1",
                                 "drawRateTypeVip": "2",
                                 "drawRate": 20,
                                 "drawRateVip": 20,
                                 "firstPointUse": 15,
                                 "firstPointUseVip": 15,
                                 "memberPointUse": 10,
                                 "memberPointUseVip": 20,
                                 "activityStartTime": "{{today_add_1}}",
                                 "activityEndTime": "{{today_add_2}}",

                             })
        return res

    def getBlindbox(self, activity_type: int = 1) -> Dict:
        """
        获取盲盒或翻牌活动详情
        :param activity_type: 活动类型 (1盲盒, 2翻牌)
        :return: 返回获取活动详情的响应结果
        """
        res = send_requests(method='get', url='/api/app/blindbox/getBlindbox/public', data={'activityType': activity_type})
        return res

    def blindboxInfo(self, blindbox_id: str, auth_token: str, app_id: str) -> Dict:
        """
        获取活动详情
        :param blindbox_id: 活动ID
        :param auth_token: 认证令牌
        :param app_id: 应用程序ID
        :return: 返回获取活动详情的响应结果
        """
        res = send_requests(method='get', url='/api/app/blindbox/query/my/blindboxInfo/' + blindbox_id,
                            data={'blindboxId': blindbox_id}, token=auth_token, appId=app_id)
        return res

    def blindboxlotterycarousel(self, blindbox_id: str, auth_token: str) -> Dict:
        """
        获取盲盒中奖信息 - 首页滚动
        :param blindbox_id: 盲盒ID
        :param auth_token: 认证令牌
        :return: 返回获取盲盒中奖信息的响应结果
        """
        res = send_requests(method='get', url='/api/app/blindbox/lottery/carousel/' + blindbox_id + '/public',
                            data={'blindboxId': blindbox_id}, token=auth_token)
        return res

    def blindboxaddLottery(self, get_type: int, auth_token: str, app_id: str = None) -> Dict:
        """
        获取抽奖次数
        :param get_type: 获取类型 (2签到, 6分享)
        :param auth_token: 认证令牌
        :param app_id: 应用程序ID
        :return: 返回获取抽奖次数的响应结果
        """
        res = send_requests(method='get', url='/api/app/blindbox/share/addLottery',
                            data={'type': get_type}, token=auth_token, appId=app_id)
        return res

    def blindboxIdlottery(self, blind_box_id: int, auth_token: str, app_id: str) -> Dict:
        """
        翻牌 - 抽奖
        :param blind_box_id: 盲盒ID
        :param auth_token: 认证令牌
        :param app_id: 应用程序ID
        :return: 返回抽奖结果的响应结果
        """
        res = send_requests(method='get', url=f'/api/app/blindbox/lottery/{blind_box_id}',
                            data={'blindboxId': blind_box_id}, token=auth_token, appId=app_id)
        return res


    def my_Winning_record(self, blind_box_id: int, token: str, app_id: str,
                          page_size: int = 10, page_num: int = 1) -> Dict:
        """
        获取中奖记录
        :param blind_box_id: 盲盒ID
        :param token: 认证令牌
        :param app_id: 应用程序ID
        :param page_size: 每页数量，默认为10
        :param page_num: 页码，默认为1
        :return: 返回中奖记录的响应结果
        """
        data = {
            'pageSize': page_size,
            'pageNum': page_num
        }
        res = send_requests(method='get', url=f'/api/app/blindbox/query/my/lottery/{blind_box_id}',
                            data=data, token=token, appId=app_id)
        return res

    def sign_detail(self, blind_box_id:int, token:str) -> Dict:
        """
        瓜分详情
        :param blind_box_id: 活动idID
        :param token:认证令牌
        :return:
        """
        res = send_requests(method='get', url=f'/api/app/sign/detail/{blind_box_id}',
                            data={
                                'blindboxId': blind_box_id
                            }, token=token)
        return res


    def sign_flip(self, blind_box_id:int, token:str) -> Dict:
        """
        签到 - 瓜分千万积分
        :param blind_box_id: 活动ID
        :param token: 认证令牌
        :return:
        """
        res = send_requests(method='get', url=f'/api/app/sign/flip/{blind_box_id}',
                            data={'id': blind_box_id}, token=token)
        return res


    def sign_lottery(self, blind_box_id:int, token:str) -> Dict:
        """
        翻牌 - 瓜分千万积分
        :param blind_box_id: 活动ID
        :param token: 认证令牌
        :return:
        """
        res = send_requests(method='get', url=f'api/app/sign/lottery/point/{blind_box_id}',
                            data={'blindboxId': blind_box_id}, token=token)
        return res

