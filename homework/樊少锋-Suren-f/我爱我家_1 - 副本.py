import requests
import re
import numpy as np
import pandas as pd
import urllib
from bs4 import BeautifulSoup
import math
import random
import time
from cc import *

def get_ip():
    with open('get_xici_ip.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return random.choice(lines)

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

headers = {'user-agen': random.choice(my_headers)
               }
proxies = {'HTTPS': 'HTTPS://' + get_ip().replace('\n', '')}

def get_url():
    url = 'https://m.5i5j.com/bj/zufang/index-n1/_北京'
    info = requests.get(url, proxies=proxies, headers=headers, )
    print(info)
    if info.status_code == 200:
        info.encoding = 'utf-8'
        html_ = info.text
        soup = BeautifulSoup(html_, 'html.parser')
        # a = soup.find_all('ul',class_='er_list')[0].find_all('a')
        url_list = [i.get('href') for i in soup.find('ul', class_='er_list').find_all('a')]
        name_list = [i.text.strip() for i in soup.find_all('h3')[6:]]

        return url_list, name_list

print(get_url())
def url_list():
    soup = BeautifulSoup(get_url(), 'html.parser')
    #a = soup.find_all('ul',class_='er_list')[0].find_all('a')
    url_list = [i.get('href') for i in soup.find('ul',class_='er_list').find_all('a')]
    name_list = [i.text.strip() for i in soup.find_all('h3')[6:]]

    return url_list,name_list


def home_info():

    soup = BeautifulSoup(html, 'html.parser')

    zong_list = [i.text for i in soup.find('ul',class_='house_Dmain clearfix').find_all('li')]

    a=[]            #租金、支付方式、面积、户型、朝向、楼层、装修、楼型、出租方式、看房时间、小区
    for i in range(len(zong_list)):
        if i <= 7:
            a.append(zong_list[i][2:])
            continue
        if i == 8 or 9:
            a.append(zong_list[i][4:])
            continue
        if i == 10:
            a.append(zong_list[i][2:])
            continue


    #地铁
    metor = soup.find('ul',class_='house_te clearfix').find_all('p')[1].text
    a.append(metor)
    #房源配套设施
    housingfacilities = [i.text for i in soup.find('ul',class_='huose_she clearfix').find_all('p')]
    a.append(housingfacilities)
    #看房记录
    record = [i.text for i in soup.find('dl',class_= 'lookList clearfix').find_all('p')]
    for i in record:
        if i == '最近带看'or '近7天带看' or '近30天带看':
            record.remove(i)
    for x in record:
        a.append(x)
    #开发商
    developers = [i.text for i in soup.find('ul',class_='house_main clearfix').find_all('li')][1][3:]
    a.append(developers)
    #商圈
    tradingarea = [i.text for i in soup.find('div',class_='de-crumb').find_all('a')][3][:-2]
    a.append(tradingarea)

    return a

def write_csv():
    data = home_info()
    df = pd.DataFrame([data],columns=['租金','支付方式','面积','户型','朝向','楼层','装修','楼型','出租方式','看房时间',
                                      '小区','地铁','房源配套设施','最近带看','近7天带看','近30天带看','开发商','商圈'])
    df.to_csv('我爱我家.csv',index=False, encoding='utf-8-sig')

    return '完成'





        