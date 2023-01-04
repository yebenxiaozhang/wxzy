"""
============================
Author: 潘师傅
Time: 2022/7/29 17:45
Project: wxzy
Company: 无限主义
============================
"""

from HTMLTestRunner import HTMLTestRunner
import unittest
from BeautifulReport import BeautifulReport

s = unittest.TestLoader().discover(r"/")
# 第一步：读取该目录下所有以test*.py的文件

# 测试报告 html的形式1
# with open("report.html", "wb") as fs:
#     run = HTMLTestRunner(fs, title='这是测试报告标题', tester='这里是填写测试人员')
#     run.run(s)

# 测试报告 html形式2
br = BeautifulReport(s)
br.report("这是测试报告标题", "bp_report.html")

