"""
============================
Author: 潘师傅
Time: 2022/7/29 17:40
Project: wxzy
Company: 无限主义
============================
"""


def add(a, b, c, d):
    sum = a + b + c + d
    print(sum)
    return sum


list_1 = [1, 2, 3, 4]

s = add(*list_1)      # 调用函数时，传参的时候 可以用 * 进行拆包
print(s)

lis_2 = {
    '1': 2,
    '2': 3

}
