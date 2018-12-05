# -*- coding: utf-8 -*-
"""
   File Name：     reger
   Product:        PyCharm
   Project:    python4
   File:       reger.py
   Author :       ZXR
   date：          2018/12/4
   time:           16:40
"""
from bs4 import BeautifulSoup
import requests

url = 'http://ip.seofangfa.com/proxy/1.html'
r = requests.get(url,
             headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'})
r.encoding = 'utf-8'
info = r.text
print(info)
soup = BeautifulSoup(info,'lxml')
a = soup.select('body > div.container.theme-showcase > div.table-responsive > table > tbody:nth-of-type(2)')
print(a)