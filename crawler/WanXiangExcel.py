#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-27
# Project: wanxiang

from pyspider.libs.base_handler import *
from pymongo import MongoClient
import datetime
import xlrd
import xlwt


class WanXiangExcel(BaseHandler):

    def __init__(self):
        self.mongo_url = 'mongodb://127.0.0.1:27017/succulent'
        self.mongo_client = MongoClient(self.mongo_url)
        self.mongo_db = self.mongo_client['succulent']

    def write(self):
        sheet, workbook = self.init_sheet()
        index = 1

        cursor = self.mongo_db['vendor'].find({}).sort('_id')
        for c in cursor:

            species_name = c.get('speciesName')
            if species_name:
                sheet.write(index, 0, species_name)
                print species_name

            original_price = c.get('originalPrice')
            if original_price:
                sheet.write(index, 1, original_price)
                print original_price

            size = c.get('size')
            if size:
                sheet.write(index, 2, size)
                print size

            inventory = c.get('inventory')
            if inventory:
                sheet.write(index, 3, inventory)
                print inventory

            image_url = c.get('imageUrl')
            if image_url:
                sheet.write(index, 4, image_url)
                print image_url

            update_time = c.get('updateTime')
            if update_time:
                time_style = xlwt.easyxf(num_format_str='YYYY-mm-dd HH:MM:SS')
                sheet.write(index, 5, update_time + datetime.timedelta(hours=8), time_style)
                print update_time + datetime.timedelta(hours=8)

            index += 1

        workbook.save(u'/Users/anmy/Downloads/tmp/vendor.xls')

    def init_sheet(self):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('wanxiang')
        sheet.write(0, 0, 'speciesName')
        sheet.write(0, 1, 'originalPrice')
        sheet.write(0, 2, 'size')
        sheet.write(0, 3, 'inventory')
        sheet.write(0, 4, 'imageUrl')
        sheet.write(0, 5, 'updateTime')
        return sheet, workbook

    def read(self):
        workbook = xlrd.open_workbook(u'/Users/anmy/Downloads/tmp/vendor.xls')
        sheet = workbook.sheet_by_name('wanxiang')
        print sheet.nrows
        print sheet.ncols
        if sheet.nrows:
            for index in range(1, sheet.nrows):
                species_name = sheet.cell(index, 0).value
                print species_name
                original_price = sheet.cell(index, 1).value
                print original_price
                size = sheet.cell(index, 2).value
                print size
                inventory = sheet.cell(index, 3).value
                print inventory
                image_url = sheet.cell(index, 4).value
                print image_url
                update_time = sheet.cell(index, 5).value
                print xlrd.xldate.xldate_as_datetime(update_time, workbook.datemode) if update_time else ''

if __name__ == '__main__':
    check = WanXiangExcel()
    # check.write()
    # check.read()
