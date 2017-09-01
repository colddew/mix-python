#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Project: mengsang

from pymongo import MongoClient
from bson.objectid import ObjectId
from collections import Counter
import codecs
import re
import os


class MengSangCheck:
    def __init__(self):
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def loadSpecies(self):
        with codecs.open('/Users/anmy/Downloads/tmp/mengsang.log', 'r', 'utf-8') as f:
            lines = f.readlines()
            species = lines[::2]
            return species
            # print len(species)
            # for i in range(0, len(species)):
            #     print species[i].strip()

    def loadUrls(self):
        with codecs.open('/Users/anmy/Downloads/tmp/mengsang.log', 'r', 'utf-8') as f:
            lines = f.readlines()
            urls = lines[1::2]
            return urls
            # print len(urls)
            # for i in range(0, len(urls)):
            #     print urls[i].strip()

    def loadMongo(self):
        species_names = self.mongo_db['spider'].find({}, {'speciesName': 1, 'image': 1, '_id': 0})
        names = list()
        for name in species_names:
            if name['image']:
                names.append(name['image'])
                # print name['image']
            else:
                print name['speciesName']
        return names

if __name__ == '__main__':
    check = MengSangCheck()
    # species = check.loadSpecies()
    # print len(species)
    # urls = check.loadUrls()
    # print len(urls)
    mongo = check.loadMongo()
    print len(mongo)
    # print Counter(mongo)
