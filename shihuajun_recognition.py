#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'colddew'
import requests
import re
# import sys


def shihuajun_recognition(file_name):

    image = open(file_name, 'rb')
    files = {'image': image}
    headers = {
        'Referer': 'https://servicewechat.com/wxbeb90f1d6c17059b/4/page-frame.html'
    }
    payload = {'session': '{"localkey":"openidLpg5VNV","userInfo":{"nickName":"我","avatarUrl":"https://pic2.zhimg.com/71249642e03d01a69102b9857cd9b489_xl.jpg"}}',
               'uuid': 'wxLpg5UQC'}
    response = requests.post('http://qqshihua.html5.qq.com/recognize', files=files, headers=headers,
                             allow_redirects=True, data=payload)
    return response.content

print(shihuajun_recognition(r'/Users/anmy/Downloads/pic_temp/1.jpg'))
