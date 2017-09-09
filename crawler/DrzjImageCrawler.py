#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-08 10:00:22
# Project: drzj

from pymongo import MongoClient
import os
import urllib
import time


class DrzjImageCrawler(object):

    def __init__(self):
        self.image_path = '/Users/anmy/Downloads/tmp/drzj/'
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def store_image(self):
        for skip in range(2670, 10150, 10):
            cursor = self.mongo_db['spider_drzj_image'].find({}).sort('_id').limit(10).skip(skip)
            for c in cursor:

                dir_path = self.image_path + c.get('speciesName') + "/"
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

                image_path = dir_path + str(c.get('_id')) + ".jpg"
                if not os.path.exists(image_path):
                    try:
                        u = urllib.urlopen(c.get('image'))
                        data = u.read()
                        f = open(image_path, 'wb')
                        f.write(data)
                        f.close()
                        print 'download image success, {}, {}'.format(str(c.get('_id')), c.get('image'))
                    except:
                        print 'download image fail, {}, {}'.format(str(c.get('_id')), c.get('image'))
            time.sleep(1)

if __name__ == '__main__':
    crawler = DrzjImageCrawler()
    crawler.store_image()
