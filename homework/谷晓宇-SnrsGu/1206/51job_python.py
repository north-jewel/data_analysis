#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6/9:52
# @Author  : SnrsGu
# @Email   : SnrsGu@qq.com & SnrsGu@gmail.com
# @File    : 51job_python.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import pandas as pd,numpy as np
import glob
import threading

class Job:
    def __init__(self,url,encoding = 'gbk'):
        self.url = url
        self.encoding = encoding
        self.html = self.html(self.url,self.encoding)

    def html(self,url,encoding):
        response = requests.get(url)
        response.encoding = encoding
        return response.text

    def soup(self,html):
        soup = BeautifulSoup(html,'lxml')
        return soup

    def info(self,html = None,soup = None):
        if soup != None:
            skill_type_list = soup.select('div.mt10 > p:nth-of-type(1) > a')  #遍历，出现的所有类型，需要.text再.strip()
            company_name = soup.select_one('p.cname > a.catn').get('title')
            company_size_type_list = soup.find_all('p',class_ = 'at')  #遍历索引title
            company_description = soup.find('div',class_ = 'tmsg inbox')  #.text
            company_location = soup.find('div',class_ = 'bmsg inbox')  #.p.text
            skills_required = soup.find_all('div',class_ = 'bmsg job_msg inbox')
            city_experience_edu = soup.select_one('div.cn > p.msg.ltype')  #.split('|')
            company_welfare_x = soup.find_all('span',class_ = 'sp4')  #遍历.text

            skill_type = []
            company_size_type = []
            company_welfare = []
            if skill_type_list:
                for i in skill_type_list:
                    skill_type.append(i.text.strip())
            else:
                skill_type = np.nan

            if company_size_type_list:
                for i in company_size_type_list:
                    company_size_type.append(i['title'])
            else:
                company_size_type = np.nan

            if company_description:
                company_description = company_description.text
            else:
                company_description = np.nan

            if company_location:
                company_location = company_location.p.text
            else:
                company_location = np.nan

            if city_experience_edu:
                city_experience_edu = city_experience_edu['title'].split('|')
            else:
                city_experience_edu = np.nan

            if company_welfare_x:
                for i in company_welfare_x:
                    company_welfare.append(i.text)
            else:
                company_welfare = np.nan

            info_dict = {'company_name':[company_name],
                         'skill_type':[skill_type],
                         'company_size_type':[company_size_type],
                         'company_description':[company_description.replace('\t','').replace('\r','').replace('\n','')],
                         'company_location':[company_location],
                         'city':[city_experience_edu[0].replace('\xa0\xa0','')],
                         'experience':[city_experience_edu[1].replace('\xa0\xa0','')],
                         # 'edu':city_experience_edu[2].replace('\xa0\xa0',''),
                         'company_welfare':[company_welfare]
                         }
            print(info_dict)
            info_df = pd.DataFrame(info_dict)
            return info_df

    def save(self,df):
        if glob.glob('51job_info.csv'):
            df.to_csv('51job_info.csv',encoding="utf_8_sig",index = False,header = None,mode = 'a')
        else:
            df.to_csv('51job_info.csv',encoding="utf_8_sig",index = False,mode = 'a')


if __name__ == '__main__':
    df = pd.read_csv('url.csv', header=None)
    for i in range(len(df)):
        url = df.iloc[i, 0]
        a = Job(url)
        a.save(a.info(soup = a.soup(a.html)))
        print(url,'OK')
