#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-08 10:00:22
# Project: drzj

from pyspider.libs.base_handler import *
from pymongo import MongoClient
import json


# db.spider_drzj_image.find({'speciesName':'阿修罗'})
# db.runCommand({"distinct":"spider_drzj_image", "key":"speciesName"})
# db.spider_drzj.group( { key: { 'speciesName': true}, initial: {count: 0}, reduce: function(obj,prev){ prev.count++;} } )
class Handler(BaseHandler):
    crawl_config = {
        'itag': 'v1.0'
    }

    def __init__(self):
        self.base_url = 'https://www.drzj.net/plugin.php?id=drzj_tujian:tujian&act=list&from=wxapp&page=1000&kid=0&sid=0&inajax=1'
        self.pagination_url = 'https://www.drzj.net/plugin.php?id=drzj_tujian:tujian&act=list&from=wxapp&page={}&kid=0&sid=0&inajax=1'
        self.total_pages = 100
        self.has_page = True
        self.detail_url = 'https://www.drzj.net/plugin.php?id=drzj_tujian:tujian&act=detail&from=wxapp&pid={}'
        self.image_prefix = 'https://mini-img.drzj.net/duotoutujian/data/img/cover/'
        self.image_detail = 'http://mini-img.drzj.net/duotoutujian/data/img/{}/orginal/{}'
        self.image_path = '/Users/anmy/Downloads/tmp/succulent/'
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def on_start(self):
        self.crawl(self.base_url, callback=self.index_page)

    def index_page(self, response):
        for index in range(1, self.total_pages):
            if self.has_page:
                self.crawl(self.pagination_url.format(index), callback=self.list_page)

    def list_page(self, response):
        result = json.loads(response.text)
        species_list = result.get('data').get('list')
        if list and len(species_list) > 0:
            for each in species_list:

                species_id = each.get('pid')
                print species_id
                species_name = each.get('name')
                print species_name

                result = self.mongo_db['spider_drzj'].find_one({'speciesName': species_name, 'source': 'drzj'})
                if result:
                    # self.mongo_db['spider_drzj'].update_one({'_id': ObjectId(result['_id'])}, {'$set': {
                    #     'image': self.image_prefix + each.get('img_cover'),
                    #     'familyName': each.get('kname'),
                    #     'familyTerminology': each.get('k_ld_name'),
                    #     'genusName': each.get('sname'),
                    #     'genusTerminology': each.get('s_ld_name'),
                    #     'terminology': each.get('ld_name'),
                    #     'alias': each.get('othername'),
                    #     'growthSeason': each.get('season'),
                    #     'sunshine': each.get('sun'),
                    #     'moisture': each.get('water'),
                    #     'breedPattern': each.get('reproduce'),
                    #     'description': each.get('description'),
                    #     'price': each.get('price_des')
                    # }})
                    pass
                else:
                    self.mongo_db['spider_drzj'].insert({
                        'extSpeciesId': species_id,
                        'speciesName': species_name,
                        'image': self.image_prefix + each.get('img_cover'),
                        'source': 'drzj',
                        'familyName': each.get('kname'),
                        'familyTerminology': each.get('k_ld_name'),
                        'genusName': each.get('sname'),
                        'genusTerminology': each.get('s_ld_name'),
                        'terminology': each.get('ld_name'),
                        'alias': each.get('othername'),
                        'area': '',
                        'growthSeason': each.get('season'),
                        'sunshine': each.get('sun'),
                        'temperature': '',
                        'moisture': each.get('water'),
                        'breedPattern': each.get('reproduce'),
                        'breedDifficulty': '',
                        'description': each.get('description'),
                        'price': each.get('price_des')
                    })

                self.crawl(self.detail_url.format(species_id), callback=self.detail_page,
                           save={'species_id': species_id, 'species_name': species_name})
        else:
            self.has_page = False

    def detail_page(self, response):
        species_id = response.save['speciesId']
        species_name = response.save['species_name']

        result = json.loads(response.text)
        photos = result.get('data').get('photo')
        print len(photos)
        if photos and len(photos) > 0:
            for photo in photos:
                image = self.image_detail.format(species_id, photo.get('largeImgName'))
                if image:
                    result = self.mongo_db['spider_drzj_image'].find_one({'speciesName': species_name, 'image': image})
                    if not result:
                        self.mongo_db['spider_drzj_image'].insert({
                            'species_id': species_id,
                            'speciesName': species_name,
                            'image': image
                        })
