#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-09 10:40:25
# Project: drzj

from pyspider.libs.base_handler import *
from pymongo import MongoClient
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.image_path = '/Users/anmy/Downloads/tmp/drzj/'
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def on_start(self):
        for skip in range(0, 10150, 100):
            cursor = self.mongo_db['spider_drzj_image'].find({}).sort('_id').limit(100).skip(skip)
            for c in cursor:
                if c and c.get('image'):
                    self.crawl(c.get('image'), callback=self.store_image, save={'species_name': c.get('speciesName'), 'species_id': c.get('_id')})

    def store_image(self, response):

        species_name = response.save['species_name']
        species_id = response.save['species_id']

        dir_path = self.image_path + species_name + "/"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        image_path = dir_path + species_id + ".jpg"
        if not os.path.exists(image_path):
            try:
                f = open(image_path, 'wb')
                f.write(response.content)
                f.close()
                print 'download image success, {}, {}, {}'.format(species_name, species_id, response.url)
            except:
                print 'download image fail, {}, {}, {}'.format(species_name, species_id, response.url)
