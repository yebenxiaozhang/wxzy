"""
======================
Author: 潘师傅
Time: 2022-12-15 17:06
Project: wxzy
Company: 无限主义
======================
"""
"""
1、一条用例涉及到数据当中，有url、request_data、check_sql

"""


def replace_mark_with_data(case, mark, real_data):
    """
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    :param case: excel当中读取出来一条数据。是个字典。
    :param mark: 数据当中的占位符。#值#
    :param real_data: 要替换mark的真实数据。
    :return:
    """
    for key, value in case.items():
        if value is not None and isinstance(value, str):
            # 确保是个字符串
            if value.find(mark) != -1:
                # 找到标识符
                case[key] = value.replace(mark, real_data)
    return case


if __name__ == '__main__':
    case = {
        "method": "POST",
        "url": "****",
        "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "caicai"}'
    }
    if case["request_data"].find("#phone#") != -1:
        case = replace_mark_with_data(case, "#phone#", "123456789001")
    for key, value in case.items():
        print(key, value)

