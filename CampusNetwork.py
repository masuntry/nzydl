#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
import re
from time import time

url = 'http://10.10.10.2/'
d = {
    'callback': f'dr{time()*1000:.0f}',
    'DDDDD': '191000000', #填学号
    'upass': 'password', #填密码
    '0MKKey': '123456',
    'R1': '0',
    'R3': '2', #联通1 电信2
    'R6': '0',
    'para': '00',
    'v6ip': '',
    '_': f'{time()*1000:.0f}'
}
# 构造http头部
headers = {
    'Accept': "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Connection': 'keep-alive',
    'Host': '10.10.10.2',
    'Referer': 'http://10.10.10.2',
    'User-Agent':  "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}
r = requests.post(url, headers=headers, data=d)
