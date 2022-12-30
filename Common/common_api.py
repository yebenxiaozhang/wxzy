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

from Common.handle_requests import send_requests
from Common.handle_config import conf
from jsonpath import jsonpath


def login(user, password):
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


def coupon(token, couponName, startTime, endTime, couponId=None, appType='1',
           belongType=0,
           couponType='0', consumeThreshold=0, offsetAmount=1,
           discountRatio=90, discountLimit=10,
           appId='5',
           useType='0',  mktCouponGoodsList=None,
           publishNum='998',
           perReceiveType=0, perReceiveNum=None,
           timeType='1', validityDay=5, useStartTime=None, useEndTime=None,
           description=None, useStatus=0,
           couponDisplay='1,2'):
    """
    新建优惠券/修改优惠券
    :param token: token
    :param appType: 1：全平台通用
    :param mktCouponGoodsList: 指定商品，传列表
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

    res = send_requests(method='post', url='/api/system/coupon',
                        data=dates, token=token)
    return res


def time_add(days=None, hours=None, minutes=None):
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



