#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Project: mengsang

from pyspider.libs.base_handler import *
from pymongo import MongoClient
import re
import os
import codecs


class Handler(BaseHandler):
    crawl_config = {

    }

    def __init__(self):
        self.base_url = 'http://www.mengsang.com/duorou'
        self.pagination_url = 'http://www.mengsang.com/duorou/list_1_{}.html'
        self.page_no = 1
        self.image_path = '/Users/anmy/Downloads/tmp/succulent/'
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def on_start(self):
        with codecs.open('/Users/anmy/Downloads/tmp/mengsang.log', 'r', 'utf-8') as f:
            lines = f.readlines()
            species = lines[::2]
            urls = lines[1::2]
            if len(species) == len(urls):
                for i in range(0, len(species)):
                    print species[i]
                    print urls[i]
                    self.crawl(urls[i].replace(' ', '%20'), callback=self.detail_page, save={'species': species[i].strip()})

    def detail_page(self, response):

        # init data
        species_name = response.save['species']
        image = ''
        source = 'mengsang'
        family_name = ''
        family_terminology = ''
        genus_name = ''
        genus_terminology = ''
        terminology = ''
        alias = ''
        area = ''
        growth_season = ''
        sunshine = ''
        temperature = ''
        moisture = ''
        breed_pattern = ''
        breed_difficulty = ''
        description = ''

        # extract data
        image_path = response.doc('.cbLeft img:first').attr.src
        if image_path:
            image = image_path

        for each in response.doc('.cbLeft li').items():

            if u'http://www.mengsang.com/duorou' in each.html():

                for td in each('table td').items():

                    item = td.text()
                    if u'科' in item:
                        print item
                        pattern = re.compile(u'(.*?) \((.*?)\) / (.*?)\((.*?)\)')
                        match = re.search(pattern, item)
                        if match:
                            family_name = match.group(1)
                            print family_name
                            family_terminology = match.group(2)
                            print family_terminology
                            genus_name = match.group(3)
                            print genus_name
                            genus_terminology = match.group(4)
                            print genus_terminology

                    if u'别名' in item:
                        alias = item[3:]
                        print alias

                    if u'原产地:' in item:
                        area = item[4:]
                        print area

            if u'简介' in each.html():
                description = each.text()[2:].strip()
                print description

            li = '<li>' + each.html() + '</li>'
            if u'生长季' in li:
                pattern = re.compile(u'生长季：(.*?)<')
                match = re.search(pattern, li)
                if match:
                    growth_season = match.group(1)
                    print growth_season

            if u'日照量' in li:
                pattern = re.compile(u'日照量：(.*?)<')
                match = re.search(pattern, li)
                if match:
                    sunshine = match.group(1)
                    print sunshine

            if u'浇水量' in li:
                pattern = re.compile(u'浇水量：(.*?)<')
                match = re.search(pattern, li)
                if match:
                    moisture = match.group(1)
                    print moisture

        items = list(response.doc('.cbRight .tTable td:odd').items())
        breed_pattern = items[0].text()
        print breed_pattern
        breed_difficulty = items[1]('img').attr.src[-5:-4]
        print breed_difficulty
        temperature = items[3].text()
        print temperature
        ss = items[4]('img').attr.src[-5:-4]
        if ss:
            sunshine = sunshine + ',' + ss
        print ss
        mo = items[5]('img').attr.src[-5:-4]
        if mo:
            moisture = moisture + ',' + mo
        print moisture

        div = response.doc('.cbRight .borderTop div').html()
        pattern = re.compile(u'<span.*?>英文学名：</span>(.*?)</div>')
        match = re.search(pattern, div)
        if match:
            terminology = match.group(1)
            print terminology

        # wrap data
        species = {
            'speciesName': species_name,
            'image': image,
            'source': source,
            'familyName': family_name,
            'familyTerminology': family_terminology,
            'genusName': genus_name,
            'genusTerminology': genus_terminology,
            'terminology': terminology,
            'alias': alias,
            'area': area,
            'growthSeason': growth_season,
            'sunshine': sunshine,
            'temperature': temperature,
            'moisture': moisture,
            'breedPattern': breed_pattern,
            'breedDifficulty': breed_difficulty,
            'description': description
        }

        # store data and image
        result = self.mongo_db['spider'].find_one({'speciesName': species_name})
        if not result:
            self.mongo_db['spider'].insert(species)

        self.crawl(image.replace(' ', '%20'), callback=self.store_image, save={'file_name': species_name})

    def store_image(self, response):
        content = response.content
        file_path = self.image_path + response.save['file_name'] + ".png"
        if not os.path.exists(file_path):
            f = open(file_path, 'wb')
            f.write(content)
            f.close()
