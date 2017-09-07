#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-07 12:10:30
# Project: qunar

from pyspider.libs.base_handler import *
from pymongo import MongoClient
import re
import os


class Handler(BaseHandler):
    crawl_config = {
        'itag': 'v1.0',
        "proxy":"52.80.53.96:33862",
        "headers":{
            "Proxy-Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
            "Accept": "*/*",
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4"
        }
    }

    def __init__(self):
        self.base_url = 'https://flight.qunar.com/'
        self.pagination_url = 'https://flight.qunar.com/site/oneway_list_inter.htm?searchDepartureAirport=%E6%9D%AD%E5%B7%9E&searchArrivalAirport=%E6%82%89%E5%B0%BC&searchDepartureTime=2017-09-16&searchArrivalTime=2017-09-29&nextNDays=0&startSearch=true&fromCode=HGH&toCode=SYD&from=flight_int_search&lowestPrice=null&favoriteKey=&showTotalPr=0&adultNum=1&childNum=0&cabinClass='
        self.page_no = 1
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['flight']

    def on_start(self):
        self.crawl(self.base_url, callback=self.index_page, fetch_type='js')

    def index_page(self, response):
        self.crawl(self.pagination_url, callback=self.list_page, fetch_type='js', js_script='''
                   function() {
                       document.getElementsByClassName('sort')[0].lastChild.click();
                   }
                   ''')

    def list_page(self, response):
        flight = response.doc('.m-airfly-lst div:first')
        print flight('.col-price span').html()
