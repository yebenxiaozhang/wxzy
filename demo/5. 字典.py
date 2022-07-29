"""
============================
Author: 潘师傅
Time: 2022/7/29 17:39
Project: wxzy
Company: 无限主义
============================
"""

# 列表的排序、反转
# 按照从大小到，从小到大 - 降序、升序

num_list = [120, 250, 11, 44, 77, 45, 22, 390]
# num_list.sort()  # 升序 - 从小到大
# print(num_list) # 对列表本身做了修改
# num_list.sort(reverse=True)
# print(num_list)

# 反转
# print(num_list[::-1])
# print(num_list)
#
# num_list.reverse() # 修改原列表
# print(num_list)


# # ()括号 - tuple
# my_tuple = ()  # 有序，以,分隔成员。成员值可以重复。
# my_tuple2 = (18,22,33,45,60,70)
# print(my_tuple2[2])  # 下标取值
# my_tuple3 = ("hello",) # 1个值
# print(my_tuple3)
# print(type(my_tuple3))

# 字典 dict  dictionary
# {}  无序   key名唯一,常用字符串。 值可以是任意的数据类型。 key:value
dog_info = {
    "name": "陈钱罐",
    "sex": "公",
    "age": "3个月",
    "type": "串串",
    "owner": "陈多多"
}

my_dict = {}  # 空字典
print(dog_info)

print(dog_info["age"])  # 键名
# print(dog_info["parent"])  # KeyError: 'parent'
print(dog_info.get("age"))  # 字典.get(键名)
print(dog_info.get("parent"))  # None

# 添加、修改键值对。
# 如果键名不存在于字典当中，那就是添加键值对。
# 如果键名存在于字典当中，那就是修改键对应的值。
dog_info["age"] = "3个半月"
print(dog_info)

dog_info["father"] = "金毛"
print(dog_info)

# 添加字典2到字典1：字典1.update(字典2)
dog_other_info = {"color": "香槟色", "size": "50cm"}
# dog_info.update(dog_other_info)
# print(dog_info)

# 字典里面，可以成员是字典吗？可以成员是列表吗？
dog_info["other_info"] = dog_other_info
print(dog_info)

# 删除
# del dog_info["father"]
# print(dog_info)
dog_info.pop("father")
print(dog_info)

# # 键 名
# keys = dog_info.keys()
# # list()  转换成列表数据类型
# all_keys = list(keys)
# print(all_keys)
#
# # 值
# values = dog_info.values()
# # list()  转换成列表数据类型
# all_values = list(values)
# print(all_values)
#
# # 键值对
# items = dog_info.items()
# # list()  转换成列表数据类型
# all_items = list(items)
# print(all_items)


list_aa = ["ssss", 11, 22, 11, 22, "hello"]
# 去重
set_aa = set(list_aa)
# 转成列表
print(list(set_aa))

# 字符串、整数、浮点数、布尔值、元组
# 列表、字典、
# 集合

# 运算符：比较，逻辑，成员

# 逻辑 - 控制流。
