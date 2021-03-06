#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-05 16:42:49
# Project: tianxun

from pyspider.libs.base_handler import *
from pymongo import MongoClient
import re
import os


class Handler(BaseHandler):
    crawl_config = {
        'itag': 'v1.0',
        "proxy":"52.80.53.96:33862",
        "headers":{
            "Proxy-Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
            "Accept": "*/*",
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4"
        }
    }

    def __init__(self):
        self.base_url = 'https://www.tianxun.com'
        self.pagination_url = 'https://www.tianxun.com/intl-oneway-chgh-sins.html?depdate=2017-09-16&cabin=Economy&adult=1&child=0&infant=0'
        self.cookies = {}
        self.page_no = 1
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['flight']

    def on_start(self):
        self.crawl(self.base_url, callback=self.index_page)

    def index_page(self, response):
        print response.cookies
        self.crawl(self.pagination_url, callback=self.list_page)

    def list_page(self, response):
        pass
