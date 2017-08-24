# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import time
import types
import sys
from bs4 import BeautifulSoup
import MySQLdb

# from IAsk import Page
# from IAsk import Mysql
# from IAsk import Tool


# 处理页面标签类
class Tool:
    # 将超链接广告剔除
    removeADLink = re.compile('<div class="link_layer.*?</div>')
    # 去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    # 将多行空行删除
    removeNoneLine = re.compile('\n+')

    def replace(self, x):
        x = re.sub(self.removeADLink, "", x)
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeNoneLine, "\n", x)
        # strip()将前后多余内容删除
        return x.strip()


# 抓取分析某一问题和答案
class Page:
    def __init__(self):
        self.tool = Tool()

    # 获取当前时间
    def getCurrentDate(self):
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    # 通过页面的URL来获取页面的代码
    def getPageByURL(self, url):
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode("utf-8")
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print self.getCurrentTime(), "获取问题页面失败,错误代号", e.code
                return None
            if hasattr(e, "reason"):
                print self.getCurrentTime(), "获取问题页面失败,原因", e.reason
                return None

    # 传入一个List,返回它的标签里的内容,如果为空返回None
    def getText(self, html):
        if not type(html) is types.StringType:
            html = str(html)
        # 提取出<pre>标签里的内容
        pattern = re.compile('<pre.*?>(.*?)</pre>', re.S)
        match = re.search(pattern, html)
        # 如果匹配成功
        if match:
            return match.group(1)
        else:
            return None

    # 传入最佳答案的HTML,分析出回答者和回答时间
    def getGoodAnswerInfo(self, html):
        pattern = re.compile('"answer_tip.*?<a.*?>(.*?)</a>.*?<span class="time.*?>.*?\|(.*?)</span>', re.S)
        match = re.search(pattern, html)
        # 如果匹配,返回回答者和回答时间
        if match:
            time = match.group(2)
            time_pattern = re.compile('\d{2}\-\d{2}\-\d{2}', re.S)
            time_match = re.search(time_pattern, time)
            if not time_match:
                time = self.getCurrentDate()
            else:
                time = "20" + time
            return [match.group(1), time]
        else:
            return [None, None]

    # 获得最佳答案
    def getGoodAnswer(self, page):
        soup = BeautifulSoup(page, "lxml")
        text = soup.select("div.good_point div.answer_text pre")
        if len(text) > 0:
            # 获得最佳答案的内容
            ansText = self.getText(str(text[0]))
            ansText = self.tool.replace(ansText)
            # 获得最佳答案的回答者信息
            info = soup.select("div.good_point div.answer_tip")
            ansInfo = self.getGoodAnswerInfo(str(info[0]))
            # 将三者组合成一个List
            answer = [ansText, ansInfo[0], ansInfo[1], 1]
            return answer
        else:
            # 如果不存在最佳答案,那么就返回空
            return None

    # 传入回答者HTML,分析出回答者,回答时间
    def getOtherAnswerInfo(self, html):
        if not type(html) is types.StringType:
            html = str(html)
        pattern = re.compile('"author_name.*?>(.*?)</a>.*?answer_t">(.*?)</span>', re.S)
        match = re.search(pattern, html)
        # 获得每一个回答的回答者信息和回答时间
        if match:
            time = match.group(2)
            time_pattern = re.compile('\d{2}\-\d{2}\-\d{2}', re.S)
            time_match = re.search(time_pattern, time)
            if not time_match:
                time = self.getCurrentDate()
            else:
                time = "20" + time
            return [match.group(1), time]
        else:
            return [None, None]

    # 获得其他答案
    def getOtherAnswers(self, page):
        soup = BeautifulSoup(page, "lxml")
        results = soup.select("div.question_box li.clearfix .answer_info")
        # 所有答案,包含好多个List,每个List包含了回答内容,回答者,回答时间
        answers = []
        for result in results:
            # 获得回答内容
            ansSoup = BeautifulSoup(str(result), "lxml")
            text = ansSoup.select(".answer_txt span pre")
            ansText = self.getText(str(text[0]))
            ansText = self.tool.replace(ansText)
            # 获得回答者和回答时间
            info = ansSoup.select(".answer_tj")
            ansInfo = self.getOtherAnswerInfo(info[0])
            # 将三者组合成一个List
            answer = [ansText, ansInfo[0], ansInfo[1], 0]
            # 加入到answers
            answers.append(answer)
        return answers

    def getAnswer(self, url):
        if not url:
            url = "http://iask.sina.com.cn/b/gQiuSNCMV.html"
        page = self.getPageByURL(url)
        good_ans = self.getGoodAnswer(page)
        other_ans = self.getOtherAnswers(page)
        return [good_ans, other_ans]


class Mysql:
    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    # 数据库初始化
    def __init__(self):
        try:
            self.db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="123456", db="test", charset="utf8")
            self.cur = self.db.cursor()
        except MySQLdb.Error, e:
            print self.getCurrentTime(), "连接数据库错误，原因%d: %s" % (e.args[0], e.args[1])

    # 插入数据
    def insertData(self, table, my_dict):
        try:
            self.db.set_character_set('utf8')
            cols = ', '.join(my_dict.keys())
            values = '"," '.join(my_dict.values())
            sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, '"' + values + '"')
            try:
                result = self.cur.execute(sql)
                insert_id = self.db.insert_id()
                self.db.commit()
                # 判断是否执行成功
                if result:
                    return insert_id
                else:
                    return 0
            except MySQLdb.Error, e:
                # 发生错误时回滚
                self.db.rollback()
                # 主键唯一，无法插入
                if "key 'PRIMARY'" in e.args[1]:
                    print self.getCurrentTime(), "数据已存在，未插入数据"
                else:
                    print self.getCurrentTime(), "插入数据失败，原因 %d: %s" % (e.args[0], e.args[1])
        except MySQLdb.Error, e:
            print self.getCurrentTime(), "数据库错误，原因%d: %s" % (e.args[0], e.args[1])


class IAsk:
    # 初始化
    def __init__(self):
        self.page_num = 1
        self.total_num = None
        self.page_spider = Page()
        self.mysql = Mysql()

    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    # 获取当前时间
    def getCurrentDate(self):
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 通过网页的页码数来构建网页的URL
    def getPageURLByNum(self, page_num):
        page_url = "http://iask.sina.com.cn/c/951-all-" + str(page_num) + "-new.html"
        return page_url

    # 通过传入网页页码来获取网页的HTML
    def getPageByNum(self, page_num):
        request = urllib2.Request(self.getPageURLByNum(page_num))
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print self.getCurrentTime(), "获取页面失败,错误代号", e.code
                return None
            if hasattr(e, "reason"):
                print self.getCurrentTime(), "获取页面失败,原因", e.reason
                return None
        else:
            page = response.read().decode("utf-8")
            return page

    # 获取所有的页码数
    def getTotalPageNum(self):
        print self.getCurrentTime(), "正在获取目录页面个数,请稍候"
        page = self.getPageByNum(1)
        # 匹配所有的页码数,\u4e0b\u4e00\u9875是下一页的UTF8编码
        pattern = re.compile(
            u'<span class="more".*?>.*?<span.*?<a href.*?class="">(.*?)</a>\s*<a.*?\u4e0b\u4e00\u9875</a>', re.S)
        match = re.search(pattern, page)
        if match:
            return match.group(1)
        else:
            print self.getCurrentTime(), "获取总页码失败"

    # 分析问题的代码,得到问题的提问者,问题内容,回答个数,提问时间
    def getQuestionInfo(self, question):
        if not type(question) is types.StringType:
            question = str(question)
        # print question
        pattern = re.compile(
            u'<span.*?question-face.*?>.*?<img.*?alt="(.*?)".*?</span>.*?<a href="(.*?)".*?>(.*?)</a>.*?answer_num.*?>(\d*).*?</span>.*?answer_time.*?>(.*?)</span>',
            re.S)
        match = re.search(pattern, question)
        if match:
            # 获得提问者
            author = match.group(1)
            # 问题链接
            href = match.group(2)
            # 问题详情
            text = match.group(3)
            # 回答个数
            ans_num = match.group(4)
            # 回答时间
            time = match.group(5)
            time_pattern = re.compile('\d{4}\-\d{2}\-\d{2}', re.S)
            time_match = re.search(time_pattern, time)
            if not time_match:
                time = self.getCurrentDate()
            return [author, href, text, ans_num, time]
        else:
            return None

    # 获取全部问题
    def getQuestions(self, page_num):
        # 获得目录页面的HTML
        page = self.getPageByNum(page_num)
        soup = BeautifulSoup(page, "lxml")
        # 分析获得所有问题
        questions = soup.select("div.question_list ul li")
        # 遍历每一个问题
        for question in questions:
            # 获得问题的详情
            info = self.getQuestionInfo(question)
            if info:
                # 得到问题的URL
                url = "http://iask.sina.com.cn/" + info[1]
                # 通过URL来获取问题的最佳答案和其他答案
                ans = self.page_spider.getAnswer(url)
                print self.getCurrentTime(), "当前爬取第", page_num, "的内容,发现一个问题", info[2], "回答数量", info[3]
                # 构造问题的字典,插入问题
                ques_dict = {
                    "text": info[2],
                    "questioner": info[0],
                    "date": info[4],
                    "ans_num": info[3],
                    "url": url
                }
                # 获得插入的问题的自增ID
                insert_id = self.mysql.insertData("iask_questions", ques_dict)
                # 得到最佳答案
                good_ans = ans[0]
                print self.getCurrentTime(), "保存到数据库,此问题的ID为", insert_id
                # 如果存在最佳答案,那么就插入
                if good_ans:
                    print self.getCurrentTime(), insert_id, "号问题存在最佳答案", good_ans[0]
                    # 构造最佳答案的字典
                    good_ans_dict = {
                        "text": good_ans[0],
                        "answerer": good_ans[1],
                        "date": good_ans[2],
                        "is_good": str(good_ans[3]),
                        "question_id": str(insert_id)
                    }
                    # 插入最佳答案
                    if self.mysql.insertData("iask_answers", good_ans_dict):
                        print self.getCurrentTime(), "保存最佳答案成功"
                    else:
                        print self.getCurrentTime(), "保存最佳答案失败"
                # 获得其他答案
                other_anses = ans[1]
                # 遍历每一个其他答案
                for other_ans in other_anses:
                    # 如果答案存在
                    if other_ans:
                        print self.getCurrentTime(), insert_id, "号问题存在其他答案", other_ans[0]
                        # 构造其他答案的字典
                        other_ans_dict = {
                            "text": other_ans[0],
                            "answerer": other_ans[1],
                            "date": other_ans[2],
                            "is_good": str(other_ans[3]),
                            "question_id": str(insert_id)
                        }
                        # 插入这个答案
                        if self.mysql.insertData("iask_answers", other_ans_dict):
                            print self.getCurrentTime(), "保存其他答案成功"
                        else:
                            print self.getCurrentTime(), "保存其他答案失败"

    # 主函数
    def main(self):
        f_handler = open('iask.log', 'w')
        sys.stdout = f_handler
        page = open('iask.page.txt', 'r')
        content = page.readline()
        start_page = int(content.strip()) - 1
        page.close()
        print self.getCurrentTime(), "开始页码", start_page
        print self.getCurrentTime(), "爬虫正在启动,开始爬取爱问知识人问题"
        self.total_num = self.getTotalPageNum()
        print self.getCurrentTime(), "获取到目录页面个数", self.total_num, "个"
        if not start_page:
            start_page = self.total_num
        for x in range(1, start_page):
            print self.getCurrentTime(), "正在抓取第", start_page - x + 1, "个页面"
            try:
                self.getQuestions(start_page - x + 1)
            except urllib2.URLError, e:
                if hasattr(e, "reason"):
                    print self.getCurrentTime(), "某总页面内抓取或提取失败,错误原因", e.reason
            except Exception, e:
                print self.getCurrentTime(), "某总页面内抓取或提取失败,错误原因:", e
            if start_page - x + 1 < start_page:
                f = open('iask.page.txt', 'w')
                f.write(str(start_page - x + 1))
                print self.getCurrentTime(), "写入新页码", start_page - x + 1
                f.close()

if __name__ == '__main__':
    iask = IAsk()
    iask.main()

