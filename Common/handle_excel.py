"""
======================
Author: 潘师傅
Time: 2022-11-09 17:07
Project: wxzy
Company: 无限主义
======================
"""
from openpyxl import load_workbook
import unittest
import json
from Common.handle_path import datas_dir

# print(os.path.abspath(__file__))
# 获取当前路径的绝对路径

# print(os.path.dirname(os.path.abspath(__file__)))
# 获取上一级路径

# print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'api_cases.xlsx'))
# 路径拼接


class HandleExcel:

    def __init__(self, file_path, sheet_name):
        """
        :param file_path: 文件所在的绝对路径
        :param sheet_name: 表的名称
        """
        self.wb = load_workbook(file_path)
        self.sh = self.wb[sheet_name]

    def __read_titles(self):
        """
        :return: 表的第一列名称 key
        """
        titles = []
        for item in list(self.sh.rows)[0]:
            titles.append(item.value)
        return titles

    def read_all_datas(self):
        """
        :return: 先获取表的value, 再进行key=value 拼接
        """
        all_datas = []
        titles = self.__read_titles()
        for item in list(self.sh.rows)[1:]:  # 遍历数据行
            values = []
            for val in item:  # 获取每一行的值
                values.append(val.value)
            res = dict(zip(titles, values))  # title和每一行数据，打包成字典
            all_datas.append(res)
        return all_datas

    def close_file(self):
        """
        :return: 关闭表的读取
        """
        self.wb.close()


if __name__ == '__main__':
    import os

    file_path = os.path.join(datas_dir, "login_cases.xlsx")
    exc = HandleExcel(file_path, "Sheet1")
    cases = exc.read_all_datas()
    exc.close_file()
    print(cases)


