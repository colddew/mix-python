#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Project: mengsang

from pyspider.libs.base_handler import *
from pymongo import MongoClient
import codecs


class Handler(BaseHandler):
    crawl_config = {

    }

    def __init__(self):
        self.base_url = 'http://www.mengsang.com/duorou'
        self.pagination_url = 'http://www.mengsang.com/duorou/list_1_{}.html'
        self.page_no = 1
        self.image_path = '/Users/anmy/Downloads/tmp/mengsang/'
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def on_start(self):
        self.crawl(self.base_url, callback=self.index_page)

    def index_page(self, response):
        strong = response.doc('.pageinfo strong:first').text()
        self.page_no = int(strong)
        for index in range(1, self.page_no + 1):
            self.crawl(self.pagination_url.format(index), callback=self.list_page)

    def list_page(self, response):
        for each in response.doc('.tImgUl li').items():
            detail = each('.tImgIcons a')
            detail_url = detail.attr.href
            species = detail.text().strip()
            f = codecs.open('/Users/anmy/Downloads/tmp/crawler.log', 'a', 'utf-8')
            if species:
                f.write(species + '\n')
            if detail_url:
                f.write(detail_url + '\n')
            f.close()
