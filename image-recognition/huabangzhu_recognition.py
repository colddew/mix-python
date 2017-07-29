#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

__author__ = 'colddew'
import requests
import re
# import sys


def huabangzhu_recognition(file_name):

    image = open(file_name, 'rb')
    files = {'imageFile': image}
    headers = {
        'Referer': 'https://servicewechat.com/wxef1cc544d81acbb4/3/page-frame.html'
    }
    payload = {'code': '071hjCVb2RGFgR0hw5Ub2llkVb2hjCVQ'}
    response = requests.post('http://hua.nongbangzhu.cn/rest/classify/form', files=files, headers=headers,
                             allow_redirects=True, json=payload)
    return response.content

print(huabangzhu_recognition(r'/Users/anmy/Downloads/pic_temp/1.jpg'))
