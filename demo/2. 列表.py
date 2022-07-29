"""
============================
Author: 潘师傅
Time: 2022/7/29 17:38
Project: wxzy
Company: 无限主义
============================
"""
# 列表(list) - 是一种数据类型。 字符串(str)，布尔值(bool)，整数(int)，浮点数(float)
# 定义
list_my = []  # 空列表  排队的队列里没人
print(list_my)

# 可以放任意类型的数据。可以重复。
list_python30 = ["小音", "石头哥", "小剑剑", "大问号", "哥迷", True, 123, 0.22]

# 有xu的，通过下标取值。从0开始

# 通过下标取值方式   列表名[下标]
print(list_python30[2])

# 通过值获取它的下标  列表名.index(数据)
print(list_python30.index("小剑剑"))

# 不可变类型：数字、布尔值、字符串
# 列表：可变类型。可增删改

# 1、添加数据/值。可以是任意类型。
# 1）追加在末尾。 列表.append(值)
list_python30.append("落魄的小测试")
print(list_python30)

# 2) 插队：小猪猪。insert(索引,值)
list_python30.insert(0, "小猪猪")
print(list_python30)

# 3) 列表1.extend(列表2): 将列表2追加到列表1
new_list = ["荒年", "henry", "Null"]
list_python30.extend(new_list)
print(list_python30)

# 2、修改数据。 找到索引，并修改索引对应的值。
index = list_python30.index("落魄的小测试")
list_python30[index] = "不要再长肉了"  # 修改值
print(list_python30)

# print(list_python30[14])   # IndexError: list index out of range


# 3、删除数据。
# 删除某一个位置的值.
# 列表.remove(数据)    删除列表当中第一次出现的指定数据
list_python30.remove(True)
print(list_python30)

# del 列表[索引]    删除列表中某个索引的数据。
del list_python30[6]
print(list_python30)

# 列表.pop()     删除列表末尾数据
last_value = list_python30.pop()
print(list_python30)
print(last_value)

# 获取列表的长度   len()
print(len(list_python30))
item = list_python30[len(list_python30) - 1]
print(item)

# 列表一般都是放同一类型的数据。
# 算术运算符、比较、赋值、逻辑

# 成员运算符   成员   in  列表/字符串   成员 not in 列表/字符串

result = '荒年' in list_python30
print(result)

result2 = "是包子呀呀呀" not in list_python30
print(result2)

print("11" in "112233444444")

# 获取30以内 可以被3整除的数

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
