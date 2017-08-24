# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib
import re
import string


# 绩点运算
class SDU:
    # 类的初始化
    def __init__(self):
        # 登录URL
        self.loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
        # 成绩URL
        self.gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
        # CookieJar对象
        self.cookies = cookielib.CookieJar()
        # 表单数据
        self.postdata = urllib.urlencode({
            'stuid': '201200131012',
            'pwd': 'xxxxx'
        })
        # 构建opener
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        # 学分list
        self.credit = []
        # 成绩list
        self.grades = []

    def getPage(self):
        req = urllib2.Request(url=self.loginUrl, data=self.postdata)
        result = self.opener.open(req)
        result = self.opener.open(self.gradeUrl)
        # 返回本学期成绩页面
        return result.read().decode('gbk')

    def getGrades(self):
        # 获得本学期成绩页面
        page = self.getPage()
        # 正则匹配
        myItems = re.findall('<TR>.*?<p.*?<p.*?<p.*?<p.*?<p.*?>(.*?)</p>.*?<p.*?<p.*?>(.*?)</p>.*?</TR>', page, re.S)
        for item in myItems:
            self.credit.append(item[0].encode('gbk'))
            self.grades.append(item[1].encode('gbk'))
        self.getGrade()

    def getGrade(self):
        # 计算总绩点
        sum = 0.0
        weight = 0.0
        for i in range(len(self.credit)):
            if (self.grades[i].isdigit()):
                sum += string.atof(self.credit[i]) * string.atof(self.grades[i])
                weight += string.atof(self.credit[i])

        print u"本学期绩点为:", sum / weight

if __name__ == '__main__':
    sdu = SDU()
    sdu.getGrades()
