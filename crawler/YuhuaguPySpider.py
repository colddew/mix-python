#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-11 23:42:16
# Project: yuhuagu

from pyspider.libs.base_handler import *
from pymongo import MongoClient
from bson.objectid import ObjectId
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class Handler(BaseHandler):
    crawl_config = {
        'itag': 'v1.0'
    }

    def __init__(self):
        self.base_url = 'http://www.yuhuagu.com/duojiang'
        self.pagination_url = 'http://www.yuhuagu.com/duojiang/list_32_{}.html'
        self.page_no = 1
        self.image_path = '/Users/anmy/Downloads/tmp/yuhuagu/'
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def on_start(self):
        self.crawl(self.base_url, callback=self.index_page)

    def index_page(self, response):
        strong = response.doc('.pageinfo strong:first').text()
        self.page_no = int(strong)
        for index in range(1, self.page_no + 1):
            self.crawl(self.pagination_url.format(index), callback=self.list_page)

    def list_page(self, response):
        for each in response.doc('#pbox div').items():
            a = each('a')
            detail_url = a.attr.href
            image = a('img')
            image_url = image.attr.src
            species_name = image.attr.alt
            if detail_url and species_name:
                self.crawl(detail_url, callback=self.detail_page, save={'species_name': species_name, 'image_url': image_url})

    def detail_page(self, response):

        try:
            # response.content = response.content.decode('gbk', 'replace').encode('gbk')
            response.content = response.content.decode('gbk', 'ignore').encode('gbk')
            image_url = response.save['image_url']

            species_name = ''
            terminology = ''
            alias = ''
            terminology = ''
            family_name = ''
            genus_name = ''
            area = ''
            description = ''

            name = response.doc('#art h1').text().strip()
            name = name.replace(u'(', '').replace(u')', '').replace(u'（', '').replace(u'）', '').replace(u'图片', '').replace(u'多肉', '').replace(u'植物', '')

            index = self.get_first_alpha_index(name)
            if index and index > 0:
                species_name = name[:index]
                terminology = name[index:]
            else:
                species_name = name[:]

            items = list(response.doc('#artad_101 span').items())
            if not species_name:
                species_name = items[0].text()

            alias = items[1].text()

            if not terminology:
                terminology = items[2].text().replace('\\', '')

            family_genus = items[3].text()
            if family_genus:
                family_index = family_genus.find(u'科')
                family_name = family_genus[:family_index + 1]
                genus_name = family_genus[family_index + 1:]

            area = items[4].text()
            description = response.doc('.wenz_tou').text()

            result = self.mongo_db['spider_yuhuagu'].find_one({'speciesName': species_name, 'source': 'yuhuagu'})
            if result:
                db_family_name = result.get('familyName')
                db_genus_name = result.get('genusName')
                db_terminology = result.get('terminology')
                db_alias = result.get('alias')
                db_area = result.get('area')
                db_description = result.get('description')

                self.mongo_db['spider_yuhuagu'].update_one({'_id': ObjectId(result['_id'])}, {'$set': {
                    'familyName': db_family_name if db_family_name else family_name,
                    'genusName': db_genus_name if db_genus_name else genus_name,
                    'terminology': db_terminology if db_terminology else terminology,
                    'alias': db_alias if db_alias else alias,
                    'area': db_area if db_area else area,
                    'description': db_description + '' + description,
                }})
            else:
                self.mongo_db['spider_yuhuagu'].insert({
                    'speciesName': species_name,
                    'image': image_url,
                    'source': 'yuhuagu',
                    'familyName': family_name,
                    'genusName': genus_name,
                    'terminology': terminology,
                    'alias': alias,
                    'area': area,
                    'description': description
                })

            for each in response.doc('.wenz img').items():
                image = each.attr.src
                result = self.mongo_db['spider_yuhuagu_image'].find_one({'speciesName': species_name, 'image': image})
                if not result:
                    self.mongo_db['spider_yuhuagu_image'].insert({
                        'speciesName': species_name,
                        'image': image
                    })
        except:
            result = self.mongo_db['error'].find_one({'errorUrl': response.url})
            if not result:
                self.mongo_db['error'].insert({
                    'errorUrl': response.url
                })

    def get_first_alpha_index(self, name):
        for i in name:
            if i.encode('utf-8').isalpha():
                return name.find(i)
