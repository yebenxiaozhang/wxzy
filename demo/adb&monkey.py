"""
============================
Author: 潘师傅
Time: 2022/7/29 17:40
Project: wxzy
Company: 无限主义
============================
"""
"""
注意是用脚本时， 需要将脚本上传到手机上
在cmd上运行： adb shell monkey -f +路径 +次数
"""
"""
#头文件、控制monkey发送消息的参数
type = raw events
count = 10
speed = 1.0
#以下monkey命令
start data >>
    ******** 以上为固定写法
    启动应用前，把应用的数据清理掉
    RunCmd(pm clear [包名])
"""

"""
LaunchActivict(pkg_nama,activity)
启动应用 参数：包名

Tap(x,y)
模拟单击事件

RumCmd(cmd)
在设备上运行shell命令

DispatchString(input)
输入字符串

UserWait(sleep Time)
让脚本中断一段时间

RotateScreen(rotationDegree,persist)
旋转屏幕，rotationDegree为旋转角度，persist表示旋转后是否固定

DispatchPress(keyName)
按键

DispatchFlip(ture/false)
打开或者关闭软键盘

PressAndHold(x,y,pressDuration)
模拟长按事件

DeviceWakeUp()
唤醒屏幕

"""