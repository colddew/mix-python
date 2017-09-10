#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-08 10:20:46
# Project: zqplant

from pymongo import MongoClient
import os
import sys
import urllib


reload(sys)
sys.setdefaultencoding('utf8')


class ZQplantImageCrawler(object):
    def __init__(self):
        self.image_path = '/Users/anmy/Downloads/tmp/zqplant/'
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def store_main_image(self):
        for skip in range(0, 310, 10):
            cursor = self.mongo_db['spider_zqplant'].find({}).sort('_id').limit(10).skip(skip)
            for c in cursor:
                if c and c.get('image'):
                    species_name = c.get('speciesName')
                    image = c.get('image')

                    dir_path = self.image_path
                    if not os.path.exists(dir_path):
                        os.makedirs(dir_path)

                    image_path = dir_path + species_name + '.jpg'
                    if not os.path.exists(image_path):
                        try:
                            u = urllib.urlopen(image)
                            data = u.read()
                            f = open(image_path, 'wb')
                            f.write(data)
                            f.close()
                            print 'download image success, {}, {}'.format(species_name, image)
                        except:
                            print 'download image fail, {}, {}'.format(species_name, image)

    def store_other_image(self):
        for skip in range(0, 50, 10):
            cursor = self.mongo_db['spider_zqplant_image'].find({}).sort('_id').limit(10).skip(skip)
            for c in cursor:
                if c and c.get('image'):
                    species_name = c.get('speciesName')
                    image = c.get('image')

                    dir_path = self.image_path + species_name + "/"
                    if not os.path.exists(dir_path):
                        os.makedirs(dir_path)

                    image_path = dir_path + image[image.rfind('/') + 1:]
                    if not os.path.exists(image_path):
                        try:
                            u = urllib.urlopen(image)
                            data = u.read()
                            f = open(image_path, 'wb')
                            f.write(data)
                            f.close()
                            print 'download image success, {}, {}'.format(species_name, image)
                        except:
                            print 'download image fail, {}, {}'.format(species_name, image)

if __name__ == '__main__':
    crawler = ZQplantImageCrawler()
    # crawler.store_main_image()
    # crawler.store_other_image()
