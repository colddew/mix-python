# -*- encoding: utf-8 -*-

from pymongo import MongoClient
import sys
import os
import urllib

reload(sys)
sys.setdefaultencoding('utf8')


class YuhuaguImageCrawler(object):
    def __init__(self):
        self.image_path = '/Users/anmy/Downloads/tmp/yuhuagu/'
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']
