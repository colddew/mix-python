#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-08 10:20:46
# Project: zqplant

from pyspider.libs.base_handler import *
from pymongo import MongoClient


class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.pagination_url = 'https://app.tefact.com/plant/page'
        self.detail_url = 'https://app.tefact.com/plant/find'
        self.image_path = '/Users/anmy/Downloads/tmp/zqplant/'
        self.image_prefix = 'http://file.duorou.me/'
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def on_start(self):
        self.crawl(self.pagination_url, method='POST', data={'pageNum': 1000}, callback=self.index_page)

    def index_page(self, response):
        total_page = response.json.get('data').get('page').get('totalPage')
        if total_page > 0:
            for index in range(1, total_page + 1):
                self.crawl(self.pagination_url + '?pageNo=' + str(index), method='POST', data={'pageNum': index}, callback=self.list_page)

    def list_page(self, response):
        plants = response.json.get('data').get('plants')
        if plants and len(plants) > 0:
            for plant in plants:
                species_name = plant.get('name_cn')

                result = self.mongo_db['spider_zqplant'].find_one({'speciesName': species_name, 'source': 'zqplant'})
                if result:
                    pass
                else:
                    self.mongo_db['spider_zqplant'].insert({
                        'extSpeciesId': plant.get('wk_id'),
                        'speciesName': species_name,
                        'image': self.image_prefix + plant.get('icon_large').split()[0],
                        'source': 'zqplant',
                        'familyName': '',
                        'familyTerminology': '',
                        'genusName': '',
                        'genusTerminology': '',
                        'terminology': plant.get('name_en'),
                        'alias': plant.get('other_names'),
                        'area': '',
                        'growthSeason': plant.get('grow_season'),
                        'sunshine': plant.get('sun'),
                        'temperature': '',
                        'moisture': plant.get('water'),
                        'breedPattern': plant.get('feed'),
                        'breedDifficulty': plant.get('grow_difficulty'),
                        'description': plant.get('description'),
                        'price': plant.get('price')
                    })

                gallery = plant.get('gallery_large')
                if gallery:
                    for item in gallery.split(';'):
                        if item:
                            image = self.image_prefix + item.split(',')[1].split()[0]
                            if image:
                                result = self.mongo_db['spider_zqplant_image'].find_one({'speciesName': species_name, 'image': image})
                                if not result:
                                    self.mongo_db['spider_zqplant_image'].insert({
                                        'speciesName': species_name,
                                        'image': image
                                    })
