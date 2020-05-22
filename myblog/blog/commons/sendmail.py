#!/usr/bin/python
# -*- coding: UTF-8 -*-
from modules.db_conn import DB

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail(object):
    def __init__(self):
        self.db = DB()
        # 第三方 SMTP 服务
        self.mail_host = "smtp.mxhichina.com"  # 设置服务器
        self.mail_user = "ysman@manyushuai.site"  # 用户名
        self.mail_pass = "Man123456"  # 口令
        self.sender = 'ysman@manyushuai.site'

    def send_mail(self, user_email, random_number):

        receivers = [user_email]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        message = MIMEText(str(random_number), 'plain', 'utf-8')
        message['From'] = "ysman@manyushuai.site"
        message['To'] = "1309584951@qq.com"
        subject = '验证码'+str(self.get_sendmail_max_id()[0][0])
        message['Subject'] = Header(subject, 'utf-8')

        smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
        # smtpObj.connect(self.mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(self.mail_user, self.mail_pass)
        smtpObj.sendmail(self.sender, receivers, message.as_string())
        return True

    def get_sendmail_max_id(self):
        sql = '''select max(id) from login_record'''
        res = self.db.query(sql)
        if res:
            return res
