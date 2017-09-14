#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Project: yuhuagu

from pymongo import MongoClient


class YuhuaguCheck:
    def __init__(self):
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def check_species(self):
        cursor = self.mongo_db['species'].find({})
        for c in cursor:
            name = c.get('name')
            name = name.replace(u'(', '').replace(u')', '').replace(u'（', '').replace(u'）', '').replace(u'图片', '').replace(
                    u'多肉', '').replace(u'植物', '')

            index = self.get_first_alpha_index(name)
            if index and index > 0:
                print name[:index]
            else:
                print name[:]

        # cursor = self.mongo_db['spider_yuhuagu'].find({})
        # for c in cursor:
        #     print c.get('speciesName')

    def get_species(self):
        result = self.mongo_db['species'].find_one({'name': '霸王鞭图片'})
        print result
        print result.get('_id')
        print result.get('name')

    def get_first_alpha_index(self, name):
        for i in name:
            if i.encode('utf-8').isalpha():
                return name.find(i)

if __name__ == '__main__':
    check = YuhuaguCheck()
    check.check_species()
    # check.get_species()
