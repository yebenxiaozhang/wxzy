"""
============================
Author: 潘师傅
Time: 2022/7/29 17:42
Project: wxzy
Company: 无限主义
============================
"""
"""
1. 手机操作系统
android 较多， ios 较少且不能降级，只能单向升级

2. 多分辨率测试
android 端有20多种，而ios较少

3. 按键： android 一般有3个按键，而ios只有一个home键
    3.1 android 长按home呼出应用列表和切换应用，然后右滑终止应用
 Back键在大部分情况下和页面上的返回键功能一样，不过还要看Back键是否被重写，测试Back键的反馈是否正确，可以在应用间切换，还可以返回主屏幕
    3.2 Ios单击home键返回主界面，双击回到单手操作模式

4. push测试（推送测试）
    Android：点击home键，程序后台运行时，此时接收到push，点击后唤醒应用，查看此时是否可以正常跳转
    Ios：点击home键关闭程序；屏幕锁屏时的情况（红点的显示）

5. 安装和卸载测试
    Android的下载、安装的平台和工具，平台比较多
    Ios主要有App store，iTunes，testflight下载

6. 升级测试
可以被升级的必要条件：新旧版本具有相同的签名、具有相同的包名、有一个标识符区分新旧版本（如版本号）

7. 分享跳转
分享后的文案是否正确、分享后跳转是否正确、显示的消息来源是否正确

8. 触屏测试
同时触摸不同的位置或同时进行不同的操作，查看客户端的处理情况，比如，是否会crash等

"""

