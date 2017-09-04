#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-01 17:31:42
# Project: wanxiang

from pyspider.libs.base_handler import *
from pymongo import MongoClient
from bson.objectid import ObjectId
import math


# check mongo: db.runCommand({"distinct":"vendor", "key":"speciesName"})
class Handler(BaseHandler):
    crawl_config = {
        'itag': 'v1.1'
    }

    def __init__(self):
        self.base_url = 'http://duorou.com/duorouzhiwu-1-b0-duorouzhiwu.html'
        self.pagination_url = 'http://duorou.com/duorouzhiwu-1-b0-min0-max0-attr0-{}-sort_orderASCgoods_id-DESC.html'
        self.page_no = 1
        self.page_size = 20
        self.image_path = '/Users/anmy/Downloads/tmp/vendor/'
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def on_start(self):
        self.crawl(self.base_url, callback=self.index_page)

    def index_page(self, response):
        total = int(response.doc('#pager b:first').text().strip())
        self.page_no = int(math.ceil(float(total) / self.page_size))
        for index in range(1, self.page_no + 1):
            self.crawl(self.pagination_url.format(index), callback=self.list_page)

    def list_page(self, response):
        for each in response.doc('.modContent li').items():
            a = each('.portfolio-title a')
            list_page_url = a.attr.href
            species_name = a.text().strip()
            image = each('.portfolio-img img').attr.src
            self.crawl(list_page_url, callback=self.detail_page,
                       save={'species_name': species_name, 'image': image})

    def detail_page(self, response):
        species_name = response.save['species_name']
        image = response.save['image']
        lis = response.doc('.ProductD li')
        for each in lis.items():
            size = each.text().strip()
            imageUrl = image
            if each.attr.image and lis.length > 1:
                imageUrl = 'http://duorou.com/' + each.attr.image

            result = self.mongo_db['vendor'].find_one({'speciesName': species_name, 'size': size})
            if result:
                self.mongo_db['vendor'].update_one({'_id': ObjectId(result['_id'])}, {'$set': {
                    'originalPrice': each.attr.price,
                    'promotionPrice': each.attr.promote,
                    'inventory': each.attr.num
                }})
            else:
                self.mongo_db['vendor'].insert({
                    'speciesName': species_name,
                    'size': size,
                    'originalPrice': each.attr.price,
                    'promotionPrice': each.attr.promote,
                    'inventory': each.attr.num,
                    'imageUrl': imageUrl,
                    'detailUrl': response.url,
                    'vendor': 'wanxiang'
                })
