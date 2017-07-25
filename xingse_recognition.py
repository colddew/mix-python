#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'colddew'
import requests
import json
# import sys


def xingse_recognition(file_name):

    image = open(file_name, 'rb')
    files = {'flower': image}
    headers = {
        'Referer': 'https://servicewechat.com/wx66aed246411799b2/7/page-frame.html'
    }
    payload = {'photo_from': 'wx', 'version': '1.0', 'latitude': '30.2726500000', 'longitude': '120.1258200000',
               'user_id': '666666', 'device_type': 'android'}
    response = requests.post('http://api2.xingseapp.com/apapp/recognize', files=files, headers=headers,
                             allow_redirects=True, data=payload)

    json_data = json.loads(response.content)
    res = json_data['response']

    return res

print(xingse_recognition(r'/Users/anmy/Downloads/pic_temp/1.jpg'))
