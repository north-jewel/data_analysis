# -*- coding: utf-8 -*-
"""
   File Name：     qianchengwuyou
   Product:        PyCharm
   Project:    python4
   File:       qianchengwuyou.py
   Author :       ZXR
   date：          2018/12/5
   time:           9:42
"""
import requests
from bs4 import BeautifulSoup
from cityparam import chengshi
import re

url = 'https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
print(type(soup))    #  <class 'bs4.BeautifulSoup'> 生成此类的对象
div = soup.find(class_='tHeader tHjob')
print(type(div))    #  <class 'bs4.element.Tag'>  .find()方法返回此类对象
dd = soup.find_all('p')    #<class 'bs4.element.ResultSet'>  .find_all()方法返回此类对象
print(type(dd))
soup_select = soup.select('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob')
print(type(soup_select))    #<class 'list'>  .select()方法返回list对象
soup_select_one = soup.select_one('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob')
print(type(soup_select_one))    #<class 'bs4.element.Tag'>

job_name = soup.select_one('div > h1').text.strip()
company_name = soup.select_one('p.cname > a.catn').text.strip()
company_size = soup.select_one('div.tCompany_sidebar > div:nth-of-type(1) > div.com_tag > p:nth-of-type(2)').text
work_area = soup.select_one('div.tCompany_sidebar > div:nth-of-type(1) > div.com_tag > p:nth-of-type(3)').get('title')
company_area = soup.select_one('div.tCompany_main > div:nth-of-type(2) > div > p').text.strip()
company_info = soup.select_one('div.tCompany_main > div:nth-of-type(3) > div').text.strip()
salary = soup.select_one('div.tHeader.tHjob > div > div.cn > strong').text
area = soup.select_one('div.tHeader.tHjob > div > div.cn > p.msg.ltype').get('title').split('\xa0\xa0|\xa0\xa0')[0]
work_experience = soup.select_one('div.tHeader.tHjob > div > div.cn > p.msg.ltype').get('title').split('\xa0\xa0|\xa0\xa0')[1]
education = soup.select_one('div.tHeader.tHjob > div > div.cn > p.msg.ltype').get('title').split('\xa0\xa0|\xa0\xa0')[2]
create_time = soup.select_one('div.tHeader.tHjob > div > div.cn > p.msg.ltype').get('title').split('\xa0\xa0|\xa0\xa0')[4]
job_information = soup.select_one('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-of-type(1)').text
work_fare = soup.select_one('div.tHeader.tHjob > div > div.cn > div > div').text

class qiancheng:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }

    def __init__(self):
        pass

    def get_search(self,city,keyword,page,encoding = 'gbk'):
        url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        city_num = chengshi[city]
        url = url.format(city_num,keyword,page)
        res = requests.get(url,headers = self.headers)
        if res.status_code == 200:
            res.encoding = encoding
            return res.text
        else:
            return None


    def get_joburl(self,
                   res_html,
                   **kwargs,):
        '''
        传入源代码，和正则表达式，在源代码中匹配符合正则表达式的内容，返回一个获取到的字典
        :param res_html:网页源代码
        :param kwargs:正则表达式
        :return:返回满足正则表达式的字典
        '''
        url = '<input class="checkbox" type="checkbox" name="delivery_jobid" value=".*?" jt="0" style="display:none" />.*?\
        <span>.*?<a target="_blank" title="(.*?)" href="(.*?)" onmousedown="">.*?</a>'
        for key,value in kwargs.items():
            kwargs[key] = re.findall(value,res_html,re.S)
        return kwargs


    def get_info(self,url,encoding = 'gb2312'):
        '''
        输入需要访问的具体工作的链接和页面编码格式，然后请求此url，如果正常，返回页面源码，否则：返回None
        :param url: 具体工作url
        :param encoding: 页面编码格式
        :return: 返回页面源码
        '''
        res = requests.get(url=url,headers=self.headers)
        if res.status_code == 200:
            res.encoding = encoding
            return res.text
        else:
            return None


    def get_jobinfo(self,
                    res_html,
                    analytic = 'lxml',
                    way = 1,
                    **kwargs,
                    ):
        soup = BeautifulSoup(res_html,analytic)
        for key,value in kwargs.item():
            if way == 1:
                try:
                    kwargs[key] = soup.select_one(value).text.strip()
                except:
                    kwargs[key] = None
            elif way == 2:
                try:
                    kwargs[key] = soup.select_one(value).get('title')
                except:
                    kwargs[key] = None
            elif way == 3:


        return kwargs

    def get_jobdetail(self,
                      res_html,
                      analytic = 'lxml',
                      **kwargs,
                      ):
        soup = BeautifulSoup(res_html,analytic)
        for key,value in kwargs.items():
            kwargs[key] = soup.select_one(value).get('title')


a = qiancheng()
#html = a.get_search('北京','python','1')
# a.get_joburl(html,url = '<input class="checkbox" type="checkbox" name="delivery_jobid" value=".*?" jt="0" style="display:none" />.*?\
#     <span>.*?<a target="_blank" title="(.*?)" href="(.*?)" onmousedown="">.*?</a>')
