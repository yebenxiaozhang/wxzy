"""
============================
Author: 潘师傅
Time: 2022/7/29 17:38
Project: wxzy
Company: 无限主义
============================
"""
"""
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
"""

print('*****************数字***************')

# 简单判断是否同一类型
a = 111
print(isinstance(a, int))

# 取整数
print(8 // 3)

# 取余数
print(8 % 5)

# 乘方
print(3 ** 3)

print('*****************字符串***************')

str_1 = '我来自福建'

print(str_1)  # 输出字符串
print(str_1[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str_1[0])  # 输出字符串第一个字符
print(str_1[2:5])  # 输出从第三个开始到第五个的字符
print(str_1[2:])  # 输出从第三个开始的后的所有字符
print(str_1 * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(str_1 + "TEST")  # 连接字符串

# 特殊字符  反转译
print('python\n3')
print(r'python\n3')

print('*****************列表***************')
# 列表基础操作与字符串一致
# 与字符串不一样的是，列表中的元素是可以改变的
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0] = 10
print(a)
a[2:3] = [11, 12]
print(a)

a[5:] = []
print(a)

# 反转
print(a[::-1])

print('*****************元组***************')
# 元组基础操作与字符串一致
# 修改元组元素的操作是非法的


print('*****************集合***************')
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素

print('*****************字典***************')

dict = {}

dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值






