#!/usr/bin/env python
#coding=utf-8
#python version:2.7.4
#system:windows 10

#定义存放匹配出的数据的数组
import urllib2
import HTMLParser

arr = []
class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.in_div = False

    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'div':
            self.in_div = True

    def handle_data(self,data):
        if self.in_div == True and self.lasttag == 'p':
            arr.append(data)

def getContent():
    try:
        resource = urllib2.urlopen('http://www.ca121.com/list_post?category=8&id=-1').read()
        my = MyParser()
        # 传入要分析的数据，是html的。
        my.feed(resource)
    except Exception,e:
        print "爬取过程出错"
        return 0
    return arr[0]

