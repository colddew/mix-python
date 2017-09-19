# -*- encoding: utf-8 -*-
from pymongo import MongoClient
import datetime


class WanXiangCheck(object):

    def __init__(self):
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def check(self):
        result = self.mongo_db['vendor'].find_one({'speciesName': '红唇'})
        print result
        print result.get('_id')
        print result.get('speciesName')
        print result.get('updateTime')
        print result.get('updateTime') + datetime.timedelta(hours=8)

if __name__ == '__main__':
    check = WanXiangCheck()
    check.check()
