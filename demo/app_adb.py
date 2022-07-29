"""
============================
Author: 潘师傅
Time: 2022/7/29 17:42
Project: wxzy
Company: 无限主义
============================
"""
"""
adb help
查看帮助手册

adb devices
检测连接到电脑的安卓设备

adb pull <手机路径> <电脑路径>
从手机拉取信息到本地电脑

adb push <电脑路径> <手机路径>
从本地电脑推送信息到手机上

adb shell
登录手机shell （命令行的人机界面）

adb install XXXX.apk
安装手机应用

adb uninstall XXXX.apk
卸载手机应用

adb logcat
打印log信息

adb shell dumpsys activity | find "mFocusedActivity"
查看前台应用activity名

adb connect/disconnect
通过wifi进行远程连接手机进行调试

adb start-server
启动adb

adb kill-server
停止adb

adb shell am start -n 包名/入口
启动APP

adb shell pm clear <包名>
清除应用数据与缓存

adb shell input tap X轴坐标 y轴坐标
点击坐标

adb shell pm list packages
查看所有应用

adb shell pm list packages -s
只显示系统应用

adb shell pm list packages -3
只显示第三方应用

aapt dump badging
解析包名，查看包名


"""
