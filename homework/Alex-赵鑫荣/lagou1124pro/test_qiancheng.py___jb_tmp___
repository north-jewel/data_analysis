# -*- coding: utf-8 -*-
"""
   File Name：     test_qiancheng
   Product:        PyCharm
   Project:    python4
   File:       test_qiancheng.py
   Author :       ZXR
   date：          2018/12/6
   time:           15:12
"""
import requests
from bs4 import BeautifulSoup
import re

res = requests.get(url='https://jobs.51job.com/beijing-tzq/108716045.html?s=01&t=0',)
res.encoding = 'gb2312'
if res.status_code == 200:
    s = res.text
    # pattern = '<input class="checkbox" type="checkbox" name="delivery_jobid" value=".*?" jt="0" style="display:none" />.*?<span>.*?<a target="_blank" title="(.*?)" href="(.*?)" onmousedown="">.*?</a>.*?</span>.*?</p>.*?<span class="t2"><a target="_blank" title=".*?" href=".*?">.*?</a></span>.*?<span class="t3">.*?</span>.*?<span class="t4">.*?</span>.*?<span class="t5">(.*?)</span>'
    # url_list = re.findall(pattern,s,re.S)
    # print(len(url_list))
    # print(url_list)

    soup = BeautifulSoup(s,'html.parser')
    # contenturl = soup.find_all('p', class_='t1')
    # time_list = soup.find_all('span', class_='t5')[1:]
    # url_list = []
    # for p in contenturl:
    #     url_list.append((p.a.text.strip(), p.a.get('href'), time_list[contenturl.index(p)].text))
    # print(len(url_list))
    # print(url_list)
    a = soup.find('div',class_='bmsg.job_msg.inbox')
    print(a)
