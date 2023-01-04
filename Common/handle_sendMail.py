"""
======================
Author: 潘师傅
Time: 2023-01-04 17:51
Project: wxzy
Company: 无限主义
======================
"""
import yagmail
from Common.handle_config import conf


def send_mail(latest_report):
    # 连接服务器
    password = conf.get('mail', 'PassWord')
    mail = yagmail.SMTP("153390680@qq.com", password, "smtp.qq.com", 465)  # 465 端口号
    # 准备正文内容
    theme = '无限主义接口测试报告'
    content = '''
    测试报告请下载好后查看
    '''

    to = ['736297001@qq.com']
    # to = ['736297001@qq.com', '1459792453@qq.com', 'chenxiaomumu@163.com']
    # 45324214@qq.com  23071059@qq.com 34414822@qq.com  "chenxiaomumu@163.com"
    # 发送邮件
    mail.send(to=to,
              # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='chenxiaomumu@163.com'
              subject=theme,  # 主题
              contents=content,  # 内容
              attachments=latest_report,  # 附件
              cc="736297001@qq.com")  # 抄送a

