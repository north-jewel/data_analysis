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
import pandas as pd
import time
import random
import threading

# url = 'https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0'
# res = requests.get(url)
# soup = BeautifulSoup(res.text,'html.parser')
# print(type(soup))    #  <class 'bs4.BeautifulSoup'> 生成此类的对象
# div = soup.find(class_='tHeader tHjob')
# print(type(div))    #  <class 'bs4.element.Tag'>  .find()方法返回此类对象
# dd = soup.find_all('p')    #<class 'bs4.element.ResultSet'>  .find_all()方法返回此类对象
# print(type(dd))
# soup_select = soup.select('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob')
# print(type(soup_select))    #<class 'list'>  .select()方法返回list对象
# soup_select_one = soup.select_one('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob')
# print(type(soup_select_one))    #<class 'bs4.element.Tag'>
#
# job_name = soup.select_one('div > h1').text.strip()
# company_name = soup.select_one('p.cname > a.catn').text.strip()
# company_size = soup.select_one('div.tCompany_sidebar > div:nth-of-type(1) > div.com_tag > p:nth-of-type(2)').text
# work_area = soup.select_one('div.tCompany_sidebar > div:nth-of-type(1) > div.com_tag > p:nth-of-type(3)').get('title')
# company_area = soup.select_one('div.tCompany_main > div:nth-of-type(2) > div > p').text.strip()
# company_info = soup.select_one('div.tCompany_main > div:nth-of-type(3) > div').text.strip()
# salary = soup.select_one('div.tHeader.tHjob > div > div.cn > strong').text
# area = soup.select_one('div.tHeader.tHjob > div > div.cn > p.msg.ltype').get('title').split('\xa0\xa0|\xa0\xa0')[0]
# work_experience = soup.select_one('div.tHeader.tHjob > div > div.cn > p.msg.ltype').get('title').split('\xa0\xa0|\xa0\xa0')[1]
# education = soup.select_one('div.tHeader.tHjob > div > div.cn > p.msg.ltype').get('title').split('\xa0\xa0|\xa0\xa0')[2]
# create_time = soup.select_one('div.tHeader.tHjob > div > div.cn > p.msg.ltype').get('title').split('\xa0\xa0|\xa0\xa0')[4]
# job_information = soup.select_one('div.tCompany_center.clearfix > div.tCompany_main > div:nth-of-type(1)').text
# work_fare = soup.select_one('div.tHeader.tHjob > div > div.cn > div > div').text

class qiancheng:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }

    def __init__(self):
        pass

    def get_search(self,city,keyword,page,encoding = 'gbk'):
        '''
        通过传入城市、搜索关键字、页码数和编码格式，来请求前程无忧搜索页面，返回页面源代码
        :param city:城市
        :param keyword:搜索关键字
        :param page:页码数
        :param encoding:编码格式
        :return:返回搜索后的页面源代码
        '''
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
                   analytic = 'html.parser',
                   **kwargs,):
        '''
        传入源代码，和正则表达式，在源代码中匹配符合正则表达式的内容，返回一个获取到的字典
        :param res_html:网页源代码
        :param kwargs:正则表达式
        :return:返回满足正则表达式的字典
        '''
        # url = '<input class="checkbox" type="checkbox" name="delivery_jobid" value=".*?" jt="0" style="display:none" />.*?\
        # <span>.*?<a target="_blank" title="(.*?)" href="(.*?)" onmousedown="">.*?</a>'
        # for key,value in kwargs.items():
        #     kwargs[key] = re.findall(value,res_html,re.S)
        try:
            soup = BeautifulSoup(res_html,analytic)
            contenturl = soup.find_all('p',class_='t1')
            time_list = soup.find_all('span', class_='t5')[1:]
            url_list = []
            for p in contenturl:
                url_list.append((p.a.text.strip(),p.a.get('href'),time_list[contenturl.index(p)].text))
            print('soup方法获得总数为：',len(url_list))
        except:
            pattern = '<input class="checkbox" type="checkbox" name="delivery_jobid" value=".*?" jt="0" style="display:none" />.*?<span>.*?<a target="_blank" title="(.*?)" href="(.*?)" onmousedown="">.*?</a>.*?</span>.*?</p>.*?<span class="t2"><a target="_blank" title=".*?" href=".*?">.*?</a></span>.*?<span class="t3">.*?</span>.*?<span class="t4">.*?</span>.*?<span class="t5">(.*?)</span>'
            url_list = re.findall(pattern, res_html, re.S)
            print('正则方法获得总数为：',len(url_list))
        return url_list


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
                    now_url,
                    res_html,
                    analytic = 'html.parser',
                    way = 1,
                    **kwargs,
                    ):
        soup = BeautifulSoup(res_html,analytic)
        k_list = list(kwargs)
        for key,value in kwargs.items():
            if way == 1:
                try:
                    kwargs[key] = soup.select_one(value).text.strip()
                except Exception as e:
                    kwargs[key] = None
                    # with open('errorlog.txt','a') as f:
                    #     f.write('执行链接{}中{}错误信息：{}'.format(now_url,key,e))
                    #     f.write('\n')
                    #     print('执行链接{}中{}错误信息：{}'.format(now_url,key,e))
            elif way == 2:
                try:
                    kwargs[key] = soup.select_one(value[0]).get('title').split('\xa0\xa0|\xa0\xa0')[value[1]]
                except:
                    kwargs[key] = None
                    # with open('errorlog.txt','a') as f:
                    #     f.write('执行链接{}中{}错误信息：{}'.format(now_url,key,e))
                    #     f.write('\n')
                    #     print('执行链接{}中{}错误信息：{}'.format(now_url,key,e))
            elif way == 3:
                try:
                    kwargs[key] = soup.find(value[0],class_ = value[1]).text.strip()
                    # kwargs[key] = soup.select_one(value).get('title')
                except:
                    kwargs[key] = None
                    # with open('errorlog.txt','a') as f:
                    #     f.write('执行链接{}中{}错误信息：{}'.format(now_url,key,e))
                    #     f.write('\n')
                    #     print('执行链接{}中{}错误信息：{}'.format(now_url,key,e))
            elif way == 4:
                try:
                    kwargs[key] = soup.find('span',class_ = value).find_previous('p').get('title')
                except:
                    kwargs[key] = None
                    # with open('errorlog.txt','a') as f:
                    #     f.write('执行链接{}中{}错误信息：{}'.format(now_url,key,e))
                    #     f.write('\n')
                    #     print('执行链接{}中{}错误信息：{}'.format(now_url,key,e))
        return kwargs


    def to_datacsv(self,data,
                   ):
        df = pd.DataFrame.from_dict(data,orient='index').T
        threadLock.acquire()
        try:
            pd.read_csv('qianchengwuyou.csv')
            print('追加保存：',1)
        except:
            print('创建保存：',2)
            df.to_csv('qianchengwuyou.csv', index=False, encoding='utf-8-sig')
        else:
            df.to_csv('qianchengwuyou.csv', mode='a', index=False, header=False, encoding='utf-8-sig')
        threadLock.release()
        print('保存完成！')
        return '保存完成！'

if __name__ == '__main__':
    def crawl(i,n,num,a = qiancheng()):
        h5 = a.get_info(i[1])
        print('正在爬取：第{}页，共第{}条数据'.format(n, num))
        # num += 1
        print(i[0])
        print(i[1])
        d1 = a.get_jobinfo(now_url=i[1],res_html=h5, way=1,
                           job_name='div > h1',
                           company_name='p.cname > a.catn',
                           # company_size='div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_sidebar > div:nth-of-type(1) > div.com_tag > p:nth-of-type(2)',
                           # company_area='div.tCompany_main > div:nth-of-type(2) > div > p',
                           # company_info='div.tCompany_main > div:nth-of-type(3) > div',
                           salary='div.tHeader.tHjob > div > div.cn > strong',
                           # job_information='div.tCompany_center.clearfix > div.tCompany_main > div:nth-of-type(1)',
                           # work_fare='div.tHeader.tHjob > div > div.cn > div > div',
                           )
        d2 = a.get_jobinfo(now_url=i[1],res_html=h5, way=2,
                           area=['div.tHeader.tHjob > div > div.cn > p.msg.ltype', 0],
                           work_experience=['div.tHeader.tHjob > div > div.cn > p.msg.ltype', 1],
                           education=['div.tHeader.tHjob > div > div.cn > p.msg.ltype', 2],
                           people_num=['div.tHeader.tHjob > div > div.cn > p.msg.ltype', 3],
                           # create_time = ['div.tHeader.tHjob > div > div.cn > p.msg.ltype',-1],
                           )
        d3 = a.get_jobinfo(now_url=i[1],res_html=h5, way=3,
                           job_information = ['div','bmsg job_msg inbox'],
                           company_area = ['div','bmsg inbox'],
                           company_info = ['div','tmsg inbox'],
                           work_fare = ['div','t1'],
                           )
        d4 = a.get_jobinfo(now_url=i[1],res_html=h5, way=4,
                           company_type='i_flag',
                           company_size='i_people',
                           work_area='i_trade',
                           )
        d1['create_time'] = i[2]  # 添加发布时间
        d1.update(d2)
        d1.update(d3)
        d1.update(d4)
        d1['job_url'] = i[1]  # 添加工作链接
        print('数据爬取完毕，开始保存！')
        # print(d1)
        time.sleep(random.randint(0,2))
        a.to_datacsv(d1)

    a = qiancheng()
    num=1
    threadLock = threading.Lock()
    for n in range(1,114):
        html = a.get_search('北京','python',str(n))
        url_list = a.get_joburl(html)
        # d = a.get_joburl(html,url = '<input class="checkbox" type="checkbox" name="delivery_jobid" value=".*?" jt="0" style="display:none" />.*?\
        #     <span>.*?<a target="_blank" title="(.*?)" href="(.*?)" onmousedown="">.*?</a>')
        # url_list = d['url']
        thread_list = []
        for i in url_list:
            t = threading.Thread(target=crawl, args=(i,n,url_list.index(i),))

            thread_list.append(t)

        for t in thread_list:
            t.start()

        for t in thread_list:
            t.join()

        print('爬虫暂停2秒！')
        time.sleep(random.randint(0,2))
        print('爬虫重启')
