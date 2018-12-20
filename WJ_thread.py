# -*- coding: utf-8 -*-
# @Time: 2018/12/16 19:40
# @File: WJ_thread.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import threading
import time
from 代理测试 import browser as br
import numpy as np

class WRoom:
    url = 'https://ty.5i5j.com/{}/'
    next_page_url = 'https://ty.5i5j.com/{}/n{}'

    def __init__(self,tp,td):
        self.tp = tp
        self.td = td

    def get_url(self, url):
        doc = requests.get(url,headers = np.random.choice(br))
        doc.encoding = 'utf-8'
        doc = doc.text
        return doc

    def bs_data(self,data):
        soup = BeautifulSoup(data,'html.parser')
        workkey = [i.text.replace('\n','') for i in soup.find_all('h3','listTit')]
        # 房源关键字
        rent = []  #租金
        housetype = []  # 户型
        area = []  # 面积
        # payment = []  # 支付方式
        district = [] # 小区
        orientation = []  # 朝向
        tage = []  #楼层
        decoration = []  # 装修
        rentway = []  # 出租方式
        all_set = soup.find_all('div',class_='listX')
        for i in all_set:
            t = 0
            for x in i.find_all('p')[:-1]:
                t+=1
                p = x.text.replace('·','')
                housetype.append(p[0])