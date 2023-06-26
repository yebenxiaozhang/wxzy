"""
======================
Author: 潘师傅
Time: 2023-01-04 17:33
Project: wxzy
Company: 无限主义
======================
"""

from Common.HTMLTestRunner import HTMLTestRunner
from Common.handle_path import cases_dir, reports_dir
from Common.handle_sendMail import send_mail
import unittest
import time
import os
from BeautifulReport import BeautifulReport


def latest_report(report_dir):
    """
    获取最新的测试报告
    :param report_dir:
    :return:
    """
    lists = os.listdir(report_dir)
    print(lists)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + "/" + fn))
    # print("The latest report is:" + lists[-1])
    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file


if __name__ == '__main__':
    # s = unittest.TestLoader().discover(r"/")
    s = unittest.TestLoader().discover(cases_dir)
    # 第一步：读取该目录下所有以test*.py的文件

    # 测试报告 html的形式1
    with open(reports_dir + "/" + time.strftime("%Y-%m-%d %H:%M:%S") + " report.html", "wb") as fs:
        run = HTMLTestRunner(fs, title='这是测试报告标题', tester='这里是填写测试人员')
        run.run(s)

    # 测试报告 html形式2
    # br = BeautifulReport(s)
    # br.report("这是测试报告标题", "bp_report.html")

    # # 获取最新测试报告
    # latest_report = latest_report(reports_dir)
    # # 发送邮件报告
    # send_mail(latest_report)



