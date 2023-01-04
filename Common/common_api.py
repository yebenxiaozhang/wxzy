"""
======================
Author: 潘师傅
Time: 2022/12/29 15:28 
Project: wxzy
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
        res = send_requests(method='post', url='api/auth/oauth/token?grant_type=password',
                            data={
                                "username": user,
                                "password": password
                            }, data_type=2)
        return res

    def login_mobile(self, user):
        """
        登录小程序
        :param user: 登录手机号
        :return:
        """
        res = send_requests(method='post', url='/api/auth/authentication/mobile',
                            data={
                                "appId": "wxdb8f809214c26e2e",
                                "type": "moblile",
                                "mobile": user,
                                "smsCode": "1"
                            })
        return res

    def add_coupon(self, token, couponName, startTime, endTime,
                   method='post', couponId=None, appType='1',
                   belongType=0,
                   couponType='0', consumeThreshold=0, offsetAmount=1,
                   discountRatio=90, discountLimit=10,
                   appId='5',
                   useType='0',  mktCouponGoodsList=None,
                   publishNum='998',receivedNum=None,
                   perReceiveType=0, perReceiveNum=None,
                   timeType='1', validityDay=5, useStartTime=None, useEndTime=None,
                   description=None, useStatus=0,
                   couponDisplay='1,2'):
        """
        新建优惠券/修改优惠券
        :param token: token
        :param appType: 1：全平台通用
        :param mktCouponGoodsList: 指定商品，传列表 格式如：[{'goodsId': '453'}]
        :param couponName:  优惠券名称
        :param couponType: 优惠券类型：'0'满减券 1折扣券
        :param consumeThreshold: 优惠券门槛：无门槛直接填写'0'
        :param offsetAmount: 抵扣金额：
        :param discountRatio: 折扣比例：int类型
        :param discountLimit: 抵扣上限：int类型
        :param useType: 使用范围 0全平台通用 1指定商品
        :param couponDisplay: 展示位置 1商品详情 2领券中心
        :param belongType: 0平台红包 1站点红包
        :param perReceiveType: 每人领取次数,0:不限，1 限制
        :param perReceiveNum: 每人限领取的张数
        :param timeType: 使用有效期，0 指定日期，1领后*天生效
        :param validityDay: 领取*天生效
        :param useStatus: 活动状态 0开启  1停用
        :param appId: 生效应用，以字符串的形式进行，多个应用用【,】分开
        :param startTime: 领券的开始时间
        :param endTime: 领取的结束时间
        :param useStartTime: 使用的开始时间
        :param useEndTime: 使用的结束时间
        :param description: 使用说明
        :param publishNum: 优惠券数量
        :param receivedNum: 优惠券被领取的数量
        :param couponId: 优惠券id，修改时必传
        :return:
        """
        dates = {
            'belongType': belongType,
            'appType': appType,
            'couponName': couponName,
            'couponType': couponType,
            'useType': useType,
            'perReceiveType': perReceiveType,
            'appId': appId,
            'useStatus': useStatus,
            'startTime': startTime,
            'endTime': endTime,
            'receiveTime': [startTime, endTime],
            'timeType': timeType,
            'description': description,
            'publishNum': publishNum,
            'consumeThreshold': consumeThreshold,
            'couponDisplay': couponDisplay
                }
        if couponId:
            dates['id'] = couponId
        if couponType == '0' or couponType == 0:
            dates['offsetAmount'] = offsetAmount
        else:
            dates['discountRatio'] = discountRatio
            dates['discountLimit'] = discountLimit
        if useType == '1' or useType == 1:
            dates['mktCouponGoodsList'] = mktCouponGoodsList
        if perReceiveType == '1' or perReceiveType == 1:
            dates['perReceiveNum'] = perReceiveNum
        if timeType == '0' or timeType == 0:
            dates['useStartTime'] = useStartTime
            dates['useEndTime'] = useEndTime
            dates['useTime'] = [useStartTime, useEndTime]
        else:
            dates['validityDay'] = validityDay
        if receivedNum:
            dates['receivedNum'] = receivedNum

        res = send_requests(method=method, url='/api/system/coupon',
                            data=dates, token=token)
        return res

    def add_time(self, days=None, hours=None, minutes=None):
        """
        获取当前时间，及未来或过去的时间
        :param days: 天，获取一天后的时间，填写1；反之填写-1
        :param hours: 小时，获取一个小时候的时间，则写1，反之填写-1
        :param minutes: 分钟，获取一分钟后的时间，则填写1；反之填写-1
        :return:
        """
        datetime.datetime.now()
        # 2019-06-30 10:51:14.089271
        # 格式化时间
        x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if days:
            y = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
            return x, y
        if hours:
            y = (datetime.datetime.now() + datetime.timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M:%S")
            return x, y
        if minutes:
            y = (datetime.datetime.now() + datetime.timedelta(minutes=minutes)).strftime("%Y-%m-%d %H:%M:%S")
            return x, y

    def receiveCoupon(self, token, couponId):
        """
        领取优惠券
        :param couponId: 优惠券id，以字符串的形式
        :return:
        """
        res = send_requests(method='post', url='/api/app/api/coupon/receiveCoupon/' + couponId,
                            data={
                                "couponId": couponId,
                                "receivingChannel": 0
                            }, token=token)
        return res

    def coupon_list(self, token, couponName=None, coiponId=None, couponType=None, status=None):
        """
        优惠券列表
        :param token: 必传参数
        :param couponName: 优惠券名称
        :param coiponId: 优惠券id
        :param couponType: 优惠券类型 0满减 1折扣
        :param status: 优惠券状态 0未开始 1进行中 2已结束 3已停用
        :return:
        """
        data = {}
        if couponName:
            data['couponName'] = couponName
        if coiponId:
            data['id'] = coiponId
        if couponType:
            data['couponType'] = couponType
        if status:
            data['status'] = status
        res = send_requests(method='get', url='api/system/coupon/list', data=data, token=token)
        return res

    def getCouponList(self, token, appid, couponType=None):
        """
        小程序获领券中心
        :param token: 必传
        :param appid: 应用id
        :param couponType: 0满减 1折扣
        :return:
        """
        data = {}
        if couponType:
            data['couponType'] = couponType
        res = send_requests(method='get', url='api/app/api/coupon/getCouponList', data=data, token=token, appid=appid)
        return res

    def getGoodsCoupon(self, token, goodsId, appid):
        """
        商品详情中的优惠券
        :param token: 必传
        :param goodsId: 商品ID
        :param appid: 应用id
        :return:
        """
        res = send_requests(method='get', url='api/app/api/coupon/getGoodsCoupon/' + goodsId + '/public',
                            data={'goodsId': goodsId}, token=token, appid=appid)
        return res

    def time_difference(self, y):
        """
        时间差
        :param y:
        :return:
        """
        from datetime import datetime, date
        dome = time.strftime("%Y-%m-%d %H:%M:%S")
        time_1_struct = datetime.strptime(y, "%Y-%m-%d %H:%M:%S")
        time_2_struct = datetime.strptime(dome, "%Y-%m-%d %H:%M:%S")
        if time_1_struct > time_2_struct:
            if dome[:10] == y:
                return ((time_1_struct - time_2_struct).seconds / 60 / 60)
            else:
                total_seconds = (time_1_struct - time_2_struct).total_seconds()
                return (-(total_seconds) / 60 / 60)
        elif time_1_struct < time_2_struct:
            if dome[:10] == y:
                return ((time_2_struct - time_1_struct).seconds / 60 / 60)
            else:
                total_seconds = (time_2_struct - time_1_struct).total_seconds()
                return ((total_seconds) / 60 / 60)
