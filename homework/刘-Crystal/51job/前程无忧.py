import requests
import re
from cityinfo import cityInfo
from info_re import all_re
import numpy as np
import pandas as pd
class Job:


    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}


    def __init__(self,
                 city,job,
                 encoding='gbk',
                 CITY=cityInfo(),
                 All_re = all_re(),
                 params={'lang': 'c',
                         'stype': '',
                         'postchannel': '0000',
                         'workyear': '99',
                         'cotype': '99',
                         'degreefrom': '99',
                         'jobterm': '99',
                         'companysize': '99',
                         'providesalary': '99',
                         'lonlat': '0,0',
                         'radius': '-1',
                         'confirmdate': '9',
                         'fromType': '',
                         'dibiaoid': '0',
                         'address': '',
                         'line': '',
                         'specialarea': '00',
                         'from': '',
                         'welfare': ''},
                 ):
        self.params = params
        self.encoding = encoding
        self.CITY=CITY
        self.city = city
        self.job = job
        self.re_dict = All_re
        self.every_url = self.jobUrl()
        self.small_url = self.smallUrl()
    def jobUrl(self):
        num=self.CITY[self.city]
        url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,1.html'.format(num,self.job)
        res=requests.get(url,params = self.params,headers= self.header)
        res.encoding = self.encoding
        page_re = '<span class="td">共(.*?)页，到第</span>'
        page = re.findall(page_re,res.text)[0]
        job_url_list = []
        for i in range(1,3):
            url = url.replace('1.','{}').format(str(i)+'.')

            job_url_list.append(url)

        return job_url_list
    def smallUrl(self):
        for i in self.every_url:
            res1 = requests.get (i, headers=self.header)
            res1.encoding = self.encoding
            url_re = '<a target="_blank" title=".*?" href="(.*?)" onmousedown="">\
'
            new_url = re.findall (url_re, res1.text)


            return new_url

    def jobInfo(self):

        for every_url in self.small_url:
            print(every_url)
            url_res = requests.get (every_url, headers=self.header)
            url_res.encoding = self.encoding
            info_sum = re.findall(self.re_dict['city_All'],url_res.text,)[0]#学历 城市 招的人数正则
            print(info_sum)
            city_1 = re.findall(self.re_dict['city1'],info_sum,re.S)[0]
            print(city_1)
            skill_type = re.findall(self.re_dict['skill_type'],url_res.text)#技能类型
            print(skill_type)
            company_name = re.findall(self.re_dict['company_name'],url_res.text)#公司名字
            print (company_name)

            company_description = re.findall(self.re_dict['company_description'],url_res.text)#公司规模,公司类型,公司描述
            print(company_description)
            job_required = re.findall(self.re_dict['job_required'],url_res.text,re.S)#技能需求
            print(job_required)
            company_location = re.findall(self.re_dict['company_location'],url_res.text)#公司位置
            print(company_location)
            experience_required = re.findall(self.re_dict['experience_required'],info_sum,re.S)[0].replace('|','').replace('&nbsp;','')+'经验'#经验
            print(experience_required)
            company_welfare = re.findall(self.re_dict['company_welfare'],url_res.text)#公司福利
            print(company_welfare)
            salary = re.findall(self.re_dict['salary'],url_res.text)[1]#薪资
            print(salary)

            print('-'*20)
            try:
                company_welfare = company_welfare[0]











J = Job(city = '北京',job='python').jobInfo()