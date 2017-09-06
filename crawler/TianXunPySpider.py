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
        'proxy': '182.254.155.112:5000/get',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'
        }
    }

    def __init__(self):
        self.base_url = 'https://www.baidu.com'
        self.pagination_url = 'https://www.tianxun.com/intl-oneway-chgh-sins.html?depdate=2017-09-16&cabin=Economy&adult=1&child=0&infant=0'
        self.page_no = 1
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['airTicket']

    def on_start(self):
        self.crawl(self.base_url, callback=self.index_page)

    def index_page(self, response):
        pass
