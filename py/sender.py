#!/usr/bin/env python
#coding=utf-8
#python version:2.7.4
#system:windows 10
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
#邮件模块
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

#成功->返回1
#失败->返回0
def main(Content,from_addr,from_pass,to_addr,smtp_server):
    msg = MIMEText(Content, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'夏成都 <%s>' % from_addr)
    msg['To'] = _format_addr(u'客户 <%s>' % to_addr)
    msg['Subject'] = Header(u'天气信息 ', 'utf-8').encode()
    try:
        server = smtplib.SMTP(smtp_server, 587)
        server.ehlo()
        server.starttls()
        server.set_debuglevel(1)
        server.login(from_addr, from_pass)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
    except Exception,e:
        print "发送过程出错"
        return 0
    return 1



