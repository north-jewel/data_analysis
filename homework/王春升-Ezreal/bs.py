#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @时间    :   2018/12/5 9:43
# @文件名  : secondurlpy.py
# @项目名称: PyCharm

# 第二层url
import requests
from bs4 import BeautifulSoup
url = 'https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0'
res = requests.get(url)
class Result:
    def __init__(self,url = 'https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0',
                 ):
        res = requests.get(url)
        self.soup = BeautifulSoup(res.text, 'html.parser')

    def company_name(self):
        '''
        :return:
        '''
        company_name = self.soup.select_one('a.catn').get('title')
        return company_name
    def job_required(self):
        job_required = self.soup.select('div.inbox > p')[:12]
        job_required = [i.text.strip() for i in job_required]
        job_required = [''.join(i.split()) for i in job_required if len(i) != 0]
        return job_required
    def company_location(self):
        company_location = self.soup.select_one('div.bmsg > p.fp').text
        return company_location
    def edu_required(self):
        edu_required = self.soup.select_one('p.msg').text
        edu_required = edu_required.split('|')
        edu_required = ["".join(i.split()) for i in edu_required]
        return edu_required
    def company_description(self):
        company_description = self.soup.select('p.at')
        return company_description
    def company_type(self):
        company_description = self.company_description()
        company_type = company_description[0].text
        return company_type
    def company_size(self):
        company_description = self.company_description()
        company_size = company_description[1].text
        return company_size
    def skill_type(self):
        company_description = self.company_description()
        skill_type = [i.text.strip() for i in company_description[2:4]]
        return skill_type


print(res)
if res.status_code==200:
    res.encoding = 'gbk'
    # print(res.text)
    soup = BeautifulSoup(res.text,'html.parser')
    div = soup.find(class_='tHeader tHjob')
    # print(div)
    print(div.h1)
    print(type(div.h1.get('title')))
    print(div.h1.get('title'))
    print(soup.find('h1').text.strip())

    print(soup.select_one('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > h1').text)
    print(soup.select_one('div > h1').text)

    # 找唯一标识 ！！！！
    # 有n多种方法 仁者见仁智者见智
    title = div.h1.get('title')
    # company_name = soup.select_one('body > div.tCompanyPage > '
    #                                'div.tCompany_center.clearf
    company_name = soup.select_one('a.catn').get('title')
    print(company_name)
    job_required = soup.select('div.inbox > p')[:12]
    job_required = [i.text.strip() for i in job_required]
    job_required = [''.join(i.split()) for i in job_required if len(i) != 0]
    print(job_required)
    company_location = soup.select_one('div.bmsg > p.fp').text
    print(company_location)
    edu_required = soup.select_one('p.msg').text
    edu_required = edu_required.split('|')
    edu_required = ["".join(i.split()) for i in edu_required]
    print(edu_required)
    company_description = soup.select('p.at')
    # print(company_description)
    company_type = company_description[0].text
    company_size = company_description[1].text
    skill_type = [i.text.strip() for i in company_description[2:4]]
    print(skill_type)
    company_info = soup.select_one('div.tmsg').text
    print(company_info.strip())
    company_welfare = soup.select('div.t1 > span')
    company_welfare = [i.text.strip() for i in company_welfare]
    print(company_welfare)
    salary =  soup.select_one('div.cn > strong').text
    print(salary)
    skills_required = soup.select('p.fp > a')
    skills_required = [i.text.strip() for i in skills_required]
    print(skills_required)


    # body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > h1
