#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-11 23:42:16
# Project: yuhuagu

from pyspider.libs.base_handler import *
from pymongo import MongoClient
import re
import os


class Handler(BaseHandler):
    crawl_config = {
        'itag': 'v1.0'
    }

    def __init__(self):
        self.base_url = 'http://www.yuhuagu.com/duojiang'
        self.pagination_url = 'http://www.yuhuagu.com/duojiang/list_32_{}.html'
        self.page_no = 1
        self.image_path = '/Users/anmy/Downloads/tmp/yuhuagu/'
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
        for each in response.doc('#pbox div').items():
            a = each('a')
            detail_url = a.attr.href
            image = a('img')
            image_url = image.attr.src
            species_name = image.attr.alt
            if detail_url and species_name:
                self.crawl(detail_url, callback=self.detail_page, save={'species_name': species_name})

    def detail_page(self, response):
        species_name = response.save['species']
        print species_name
