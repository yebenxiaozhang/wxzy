"""
======================
Author: 潘师傅
Time: 2022-11-09 17:02
Project: wxzy
Company: 无限主义
======================
"""
from configparser import ConfigParser
import os
from Common.handle_path import conf_dir


class HandleConfig(ConfigParser):

    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


file_path = os.path.join(conf_dir, "yinlian.ini")
conf = HandleConfig(file_path)
# print(conf.get('log', 'name'))


# if __name__ == '__main__':
#     conf = HandleConfig("wxzy.ini")
#     conf.get('log', 'name')

