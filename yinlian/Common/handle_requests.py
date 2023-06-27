"""
======================
Author: 潘师傅
Time: 2022-11-09 17:11
Project: wxzy
Company: 无限主义
======================
"""
import requests
import json
import urllib3

from Common.my_logger import logger
from Common.handle_config import conf
"""
基于项目做定制化封装
1、鉴权:token
2、项目通用的请求头:
    {"X-Lemonban-Media-Type": "lemonban.v2"}

3、请求体格式：application/json
"""


def __handle_header(data_type, token=None, appId=None):
    """
    处理请求头。加上项目当中必带的请求头。如果有token，加上token。
    :param token: token值
    :return: 处理之后headers字典
    """
    headers = {"Authorization": "Basic YmFja2VuZDpiYWNrZW5k"}
    if data_type == 1:
        headers["Content-Type"] = "{}".format('application/json')
    else:
        headers["Content-Type"] = "{}".format('application/x-www-form-urlencoded')

    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    if appId:
        headers["appId"] = appId
    return headers


def send_requests(method, url, data=None, token=None, data_type=1, appId=None):
    """
    :param method:
    :param url:
    :param data:字典形式的数据。
    :param token:
    :return:
    """
    logger.info("发起一次HTTP请求")
    # 得到请求头
    headers = __handle_header(data_type, token, appId)
    # 得到完整的url - 拼接url
    # print('处理前的url', url)
    url = __pre_url(url)
    # print('处理后的url' + url)
    # 请求数据的处理 - 如果是字符串，则转换成字典对象。
    data = __pre_data(data)
    # 将请求数据转换成字典对象。
    logger.info("请求头为：{}".format(headers))
    logger.info("请求方法为：{}".format(method))
    logger.info("请求url为：{}".format(url))
    logger.info("请求数据为：{}".format(data))
    # 根据请求类型，调用请求方法
    method = method.upper()  # 大写处理
    urllib3.disable_warnings()  # 去除警告
    if method == "GET":
        resp = requests.get(url, data, headers=headers, verify=False)
    elif method == 'PUT':
        resp = requests.put(url, json=data, headers=headers, verify=False)
    else:
        if data_type == 1:
            resp = requests.post(url, json=data, headers=headers, verify=False)
        else:
            resp = requests.post(url, data, headers=headers, verify=False)
    logger.info("响应状态码为：{}".format(resp.status_code))
    logger.info("响应数据为：{}".format(resp.json()))
    return resp


def __pre_url(url):
    """
    拼接接口的url地址。
    :param url:
    :return:
    """
    base_url = conf.get("server", "base_url")
    # if base_url[8:12] == 'test' and path_type != 1:
    #     if url.startswith("/"):
    #         return base_url + '/stage-api' + url
    #     else:
    #         return base_url + "/stage-api/" + url
    # else:

    if url.startswith("/"):
        return base_url + url
    else:
        return base_url + "/" + url


def __pre_data(data):
    """
    如果data是字符串，则转换成字典对象。
    :param data:
    :return:
    """
    if data is not None and isinstance(data, str):
        return json.loads(data)
    return data


if __name__ == '__main__':
    login_url = "api/login"
    login_datas = {
                    "username": 'admin',
                    "password": 'admin123'
                }

    resp = send_requests("POST", login_url, login_datas)
    token = resp.json()["token"]

    # recharge_url = "/api/marketing/app/draw/query/my/lottery"
    # resp = send_requests(method="get", url=recharge_url, data=None, token=token)
    # print(resp.json())
