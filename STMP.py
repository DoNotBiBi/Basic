#!/usr/bin/python
# -*- coding: UTF-8 -*-
# todo:
#   1.此处是有问题的
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
def stmp_test():
# 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "341776450@qq.com"  # 用户名
    mail_pass = "jtarkjsyjqjibjic"  # 口令

    sender = '341776450@qq.com'
    receivers = ['876677504@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('傻逼的何清', 'plain', 'utf-8')

    msg = MIMEMultipart()
    #邮件正文
    subject = 'Python SMTP 邮件测试'
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header("王康", 'utf-8')
    msg['To'] = Header("何清", 'utf-8')
    msg.attach(message)

    #附件:附件名称用英文

    file_name='a.xlsx'
    att = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="%s"' % (file_name)
    msg.attach(att)
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException as error:
        print(error)
