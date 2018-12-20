import requests
import re
import numpy as np
import pandas as pd
import urllib
from bs4 import BeautifulSoup

class ZL:
    def __init__(self):
        self.get_url = self.get_url()
        self.zl_info = self.zl_info()
        #print(self.zl_info)
        self.search_get = self.search_get()
        self.search_comluns = self.search_comluns()

    def get_url(self):  #访问公司招聘网页连接
        url = 'https://jobs.51job.com/beijing-fsq/104678016.html?s=01&t=0'
        info = requests.get(url)
        info.encoding = 'gbk'
        return info.text

    def zl_info(self):  #公司详细信息
        soup = BeautifulSoup(self.get_url, "html.parser")
        company_info = []
        for i in range(1):
            #技能
            skill_type = soup.select_one('h1').text.strip()
            #print(skill_type)
            company_info.append(skill_type)
            #公司名字
            company_name = soup.select_one('a.catn').text.strip()
            #print(company_name)
            company_info.append(company_name)
            #公司描述
            company_description = soup.find('div',class_='tmsg inbox').text.strip()
            #print(company_description)
            company_info.append(company_description)
            #上班地址
            company_location = soup.select_one('div.bmsg > p.fp').text.strip()
            #print(company_location)
            company_info.append(company_location)
            #公司规模
            company_size = soup.select('div.com_tag > p')
            size_list = []
            for p in company_size:
                c = p.get_text()
                size_list.append(c)
            #print(company_size)
            company_info.append(size_list)
            #公司福利
            company_welfare = soup.select('div.t1 > span')
            welfare_list = []
            for span in company_welfare:
                a = span.get_text()
                welfare_list.append(a)
            #print(welfare_list)
            company_info.append(welfare_list)
            #职位信息
            job_required = soup.select('div.bmsg > p')
            job_list = []
            for p in job_required:
                b = p.get_text()
                job_list.append(b)
            #print (job_list)
            company_info.append(job_list)
            #薪资
            salary = soup.select_one('div.cn > strong').text.strip()
            #print(salary)
            company_info.append(salary)
            #要求
            required = soup.select_one('p.msg').text.strip()
            #print(required)
            company_info.append(required)

        return  company_info

    def search_get(self):  #搜索结果页面
        url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,' \
              'Python%2B%25E9%25AB%2598%25E7%25BA%25A7,2,1.html?lang=c&stype=2&postchannel=0000' \
              '&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0' \
              '&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=' \
              '&specialarea=00&from=&welfare='
        info = requests.get(url)
        info.encoding = 'gbk'

        return info.text

    def search_comluns(self): #结果表头
        soup = BeautifulSoup(self.search_get, "html.parser")
        company_comluns = soup.select('div.title')
        comluns_list = []
        for span in company_comluns:
            a = span.get_text()
            comluns_list.append(a)
        return comluns_list

    def search_data(self):
        soup = BeautifulSoup(self.search_get, "html.parser")
        company_data = soup.select('')
        data_list = []
        for span in company_data:
            a = span.get_text()
            data_list.append(a)
        print(data_list)



x = ZL()
x.search_data()
