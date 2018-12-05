# -*- coding: utf-8 -*-
# @Time: 2018/12/5 15:12
# @File: qcwy.py

import bs4
from bs4 import BeautifulSoup
import requests


class QCwy:
    def __init__(self, url):
        self.url = url

    def get_json(self):
        res = requests.get(self.url)
        res.encoding = 'gb2312'
        res_text = res.text
        return res_text


    def clear(self):
        doc = self.get_json()
        soup = BeautifulSoup(doc, 'html.parser')
        soup.find(class_='bmsg job_msg inbox').select('p')  # 职位信息
        soup.find(class_='bmsg inbox').select('p')  # 工作地点
        soup.find(class_='tmsg inbox')  # 公司信息
        soup.find(class_='t1').find_all(class_='sp4')  # 公司待遇
        soup.find(class_='cn').find_all('h1')  # 职位名称
        soup.find(class_='cn').find_all('strong')  # 薪资待遇
        soup.find('p', class_='msg ltype').text
x = QCwy('https://jobs.51job.com/shenzhen-ftq/108974685.html?s=01&t=0')
x.clear()
