"""
============================
Author: 潘师傅
Time: 2022/7/29 17:41
Project: wxzy
Company: 无限主义
============================
"""

"""
adb logcat -v time > [路径]
日志保存到指定位置（有时间显示） 

日志关键字：
    fatal exception 奔溃
        将报错信息给到开发即可

    anr in  无响应
        需要查看手机本地 /data/anr/traces.txt 拉取下来 进行查看

app发生异常我们测试人员应该给怎么做？
1、截图
2、问题机型、手机系统
3、复现步骤、100%复现/偶尔复现
4、app异常信息（日志）
    app发生了崩溃问题，adb logcat -v time 抓取logcat信息
    app发生了应用程序无响应问题，
        除了adb logcat -v time 抓取logcat信息
        还需要adb pull /data/traces.txt 存放本地

"""
