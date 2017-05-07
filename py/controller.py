#!/usr/bin/env python
#coding=utf-8
#python version:2.7.4
#system:windows 10
import spider
import time
import ConfigParser
import sender
conf = ConfigParser.ConfigParser()
#读取配置信息
conf.read("../doc/config.conf")
from_addr = conf.get("sender","addr")
from_pass = conf.get("sender","password")
to_addr = conf.get("receiver","addr")
smtp_server = conf.get("server","smtp_server")

#爬取发送的内容，因网络问题有可能抛异常
def doSpider():
    while(spider.getContent() == 0):
        time.sleep(10)
        spider.getContent()
    return spider.getContent()
Content = doSpider()

#发送邮件，因服务商问题有可能抛异常
def send():
    while(sender.main(Content,from_addr,from_pass,to_addr,smtp_server)==0):
        time.sleep(10)
        sender.main(Content,from_addr,from_pass,to_addr,smtp_server)

#执行主函数
send()
