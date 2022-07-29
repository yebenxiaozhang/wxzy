"""
============================
Author: 潘师傅
Time: 2022/7/29 17:39
Project: wxzy
Company: 无限主义
============================
"""
# 字符串的转义： \
s2 = '我来自福建，我喜欢别人叫我\'靓仔\''
s3 = "我来自福建，我喜欢别人叫我'靓仔'"
# print(s2)
# print(s3)

# 取某一个位置的值
# 从0开始 正向 + 1
# print(s2[0])
# print(s2[3])

# 区间的值 变量名字[起:结束]
# print(s2[0:3])   # 0 1 2
# print(s2[:3])   # 0 1 2
# print(s2[:7:2])   # 0 2 4 6 步长为2
#
# print(s2[-1:-7:-1])   # -1 -2 -3 -4 -5 -6
# print(s2[::-1])         # 面试


print("******************  常用方法/功能   *******************")
person_info = "我来自福建，我喜欢别人叫我'靓仔'"
# find(子字符串) 正向查找子字符串，找到返回的值都是>=0。没找着就是-1
index = person_info.find("我来自福建111")  # 0 正向查找子字符串。
# print(index)

# count(字符/字符串) 统计在原字符串当中出现的次数
count = person_info.count("我")
# print(count)

# len(字符串)  获取字符串的总长度
# print(len(person_info))

# upper() 将字符串的字母转换成大写。重新生成一个字符串。不会修改原来的字符串。
res = person_info.upper()
# print(res)
# print(person_info)


person_info = "我来自福建，我喜欢别人叫我'靓仔'"
# split() 分割。分隔符：
# sep: 分隔符。不会出现在分割后的数据当中。
# maxsplit: 1  分割的次数。
str_pian = person_info.split("，")
print(str_pian)  # str_pian是个列表

s2 = person_info.split("我")
print(s2)

# join()  拼接。按照拼接符将其拼接起来。
# 把支离破碎的几个字符串，拼接成一个完整的字符串！
# 1、拼接符：一定是字符串。;
ss = "    ".join(str_pian)  # 按照一定的规律去拼接 列表里的字符串。
print(ss)

# 格式化 format函数
# 字符串.format()
# 动态的去改变字符串的值：占位符{}。有几个占位符，就需要几个替换参数。
# 不需要指定数据类型。
# age = input("年龄：")
# # age = int(age)
# name = input("名字")
#
# # 1 没写序号，顺序赋值
# print("我的年龄是: {}岁，我的名字是：{}".format(age,name))
#
# # 2 有一些数据需要重复使用。在占位符{}里加索引。
# # {0}  {1}  {2}。根据序号对应的位置，去赋值。
# print("我的年龄是: {1}岁，我的名字是：{2},我的老师是：{2}。我喜欢干什么：{0}".format(age,name,"睡觉"))
#

# 3、只保留2位小数点{:.2f}.百分比：{:.2%}会对数据乘以100
# print("我昨天的作业得了{:.2f} 分   完成度为 {:.2%}".format(89.88888,0.98))
#

# print("我的成绩是：%.2f" % 2.12)

print(" hello,world! \n hello,py30!")  # \n 表示换行

print(" hello,world! \t hello,py30!")  # \t tab

print(r" hello,world! \n hello,py30!")  # r 取消转义，正常输出！！

# 拼接 +  字符串
str1 = " hello,world!!!"
str2 = "hello,python!"
str3 = "No!!!"
int1 = 20
print(str1 + str2 + str3 + str2)


# a = {
#     'name': '张三',
#     'age': 22
# }
#
# for key, vlue in a.items():
#     print(key, vlue)
#
# for x in range(1, 10):
#     print()
#     for y in range(1, x + 1):
#         print(str(x) + '*' + str(y) + '=' + str(x * y), end=' ')
#

# print('ssss\ndddd')
# print(r'sss\ndddd')

# print(id('111'))

a = 1
b = isinstance(a, int)
print(b)
if b is True:
    print('321')
print(4//3)
print(4/3)
print(4 % 3)
print(2**3)

