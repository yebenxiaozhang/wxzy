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


class yinlian:

    def __init__(self):
        pass

    def login(self, user, password):
        """
        登录
        :param user: 用户名
        :param password: 密码
        :return:
        """
        res = send_requests(method='post', url='api/login',
                            data={
                                "username": user,
                                "password": password
                            })
        return res


    def blindboxlist(self, token, activityId=None, activityName=None,activityStatus=None,
                     status=None, startTime=None,activityTime=None,pageNum=1,pageSize=10):
        """
        盲盒列表
        :param token: token
        :param activityId: 盲盒id，精准查询
        :param activityName: 盲盒名称，模糊查询
        :param activityStatus: 活动状态 0未开始 1进行中 2已结束 3已停用
        :param status: 状态 0启用 1禁用
        :param startTime: 活动开始时间
        :param activityTime: 活动结束时间
        :param pageNum: 页
        :param pageSize: 每页显示数量
        :return:
        """
        res = send_requests(method='get',url='/api/blindbox/list',
                            data={
                                'id': activityId,
                                'activityName': activityName,
                                'activityStatus': activityStatus,
                                'status': status,
                                'activityTime.startTime': startTime,
                                'activityTime.endTime': activityTime,
                                'pageNum': pageNum,
                                'pageSize': pageSize
                            }, token=token)
        return res


    def blindboxchangestatus(self, blindboxId, status, token):
        """
        启用/禁用盲盒
        :param blindboxId: 盲盒id
        :param status: 0启用 1禁用
        :param token:
        :return:
        """
        res = send_requests(method='get',
                            url='/prod-api/blindbox/changeStatus/' + blindboxId + '/' + status,
                            token=token)
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

    def getBlindbox(self, activityType=1):
        """
        :param activityType: 1盲盒 2翻牌
        :return:
        """
        res = send_requests(method='get', url='api/app/blindbox/getBlindbox/public',
                            data={
                                'activityType': activityType
                            })
        return res


    def blindboxInfo(self, blindboxId, token, appId):
        """
        活动详情
        :param blindboxId:活动ID
        :return:
        """
        res = send_requests(method='get', url='/api/app/blindbox/query/my/blindboxInfo/' + blindboxId,
                            data={
                                'blindboxId': blindboxId
                            }, token=token, appId=appId)
        return res

    def blinboxlotterycarousel(self, blindboxId, token):
        """
        盲盒中奖信息 - 首页滚动
        :param blindboxId: 盲盒ID
        :param token: token
        :return:
        """
        res = send_requests(method='get', url='/api/app/blindbox/lottery/carousel/' + blindboxId + '/public',
                            data={
                                'blindboxId': blindboxId
                            }, token=token)
        return res

    def blindboxaddLottery(self, gettpye,token, appId=None):
        """
        获取抽奖次数
        :param gettpye: 2签到 6分享
        :param token:
        :return:
        """
        res = send_requests(method='get', url='api/app/blindbox/share/addLottery',
                            data={'type': gettpye}, token=token, appId=appId)
        return res

    def blindboxIdlottery(self, blindboxId, token, appId):
        """
        翻牌 -  抽奖
        :param blindboxId:
        :param token:
        :return:
        """
        res = send_requests(method='get', url='/api/app/blindbox/lottery/' + str(blindboxId),
                            data={
                                'blindboxId': blindboxId
                            }, token=token, appId=appId)
        return res


    def myblindboxlottery(self, blindboxId, token, appId, pageSize=10, pageNum=1):
        """
        获取中奖记录
        :param blindboxId:
        :param token:
        :param appId:
        :return:
        """
        res = send_requests(method='get', url='/api/app/blindbox/query/my/lottery/' + str(blindboxId),
                            data={
                                'blindboxId': blindboxId,
                                'pageSize': pageSize,
                                'pageNum': pageNum
                            }, token=token,appId=appId)
        return res
