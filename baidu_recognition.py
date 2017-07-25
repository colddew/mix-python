#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'colddew'
import requests
import re
# import sys


def baidu_recognition(file_name):

    image = open(file_name, 'rb')
    files = {'image': image}
    response = requests.post('http://image.baidu.com/pictureup/uploadshitu', files=files, allow_redirects=True)

    temp_url = re.sub('%3A', ':', re.findall('queryImageUrl=(.*?)&querySign', response.url)[0])
    real_url = re.sub('%2F', '/', temp_url)
    return real_url

print(baidu_recognition(r'/Users/anmy/Downloads/pic_temp/1.jpg'))
