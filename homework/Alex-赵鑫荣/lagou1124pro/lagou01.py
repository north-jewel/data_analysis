# -*- coding: utf-8 -*-
"""
   File Name：     lagou01
   Product:        PyCharm
   Project:    python4
   File:       lagou01.py
   Author :       ZXR
   date：          2018/11/24
   time:           13:44
"""
import requests
import time
import urllib.parse
import math
import pandas as pd
from bs4 import BeautifulSoup
import random
import re
import numpy as np
import matplotlib.pyplot as plt

class lagouzp:
    '''
    爬取拉勾网招聘信息
    '''
    agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    ]
    def __init__(self,ct = '北京',kd = 'python'):
        '''
        初始化时的属性
        :param ct: 限定城市     可以为None(即全国)
        :param kd: 搜索关键字
        '''
        self.ct = ct
        self.kd = kd
        # self.ip_list = self.get_ip_list()

    def get_json(self,pn,ip_list,x):
        # 请求的url
        if self.ct == None:
            url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        else:
            cturl = urllib.parse.quote(self.ct)       #对城市进行URL编码
            url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(cturl)
        #post请求参数
        param = {
            'first':'true',      #是否为首页
            'pn': pn,         #页码
            'kd':self.kd          #搜索关键字
        }
        #设置请求header
        headers ={
            'Host': 'www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
            'User-Agent': random.choice(self.agent_list),
        }
        #设置代理
        # proxies ={
        #     'http': '140.143.96.216:80', 'https': '140.143.96.216:80',
        #     'http': '119.27.177.169:80', 'https': '119.27.177.169:80',
        #     'http': '221.7.255.168:8080', 'https': '221.7.255.168:8080'
        # }
        res_status = requests.post(url,headers = headers,data = param,proxies = self.get_random_ip(ip_list,x))
        res_status.encoding = 'utf-8'
        if res_status.status_code == 200:
            res_info = res_status.json()
            print(res_info)
            #返回请求响应中的'content'中的'positionResult'(包括总数，以及职位信息(公司名、地址、工资、学历要求等))
            return res_info['content']['positionResult']
        return None

    def get_total(self,json_data):
        '''
        通过(索引)获取并计算出总页数
        :return:
        '''
        position_result = json_data
        total_num = position_result['totalCount']
        page_total = math.ceil(total_num/15)    #每页15条，向上取整，算出总页数
        return page_total

    def get_detailinfo(self,json_data):
        job_info = json_data['result']
        page_all_job = []
        for j in job_info:
            job_detail = []
            # 工作详细链接
            job_url = 'https://www.lagou.com/jobs/{}.html'
            job_detail.append(job_url.format(j['positionId']))
            # time.sleep(5)
            # res_info = self.get_job_detail(url=job_url.format(j['positionId']))
            # print(job_url.format(j['positionId']))
            # soup = BeautifulSoup(res_info, 'html.parser')
            # # 添加工作描述
            # # job_detail > dd.job_bt
            # job_describe = soup.select('#job_detail > dd.job_bt')[0].text.replace('\n', '')
            # job_detail.append(job_describe)
            # # 添加办公地点
            # job_position = soup.select('#job_detail > dd.job-address.clearfix')[0].text.replace('\n','')
            # job_detail.append(job_position)
            #公司全名
            job_detail.append(j['companyFullName'])
            # 公司链接
            cm_url = 'https://www.lagou.com/gongsi/{}.html'
            job_detail.append(cm_url.format(j['companyId']))
            #公司简称
            job_detail.append(j['companyShortName'])
            #公司规模
            job_detail.append(j['companySize'])
            #融资
            job_detail.append(j['financeStage'])
            #所属区域
            job_detail.append(j['district'])
            #职称
            job_detail.append(j['positionName'])
            # 招聘学历
            job_detail.append(j['education'])
            #要求工作年限
            job_detail.append(j['workYear'])
            #薪资范围
            job_detail.append(j['salary'])
            #福利待遇
            job_detail.append(j['positionAdvantage'])
            #工作领域
            job_detail.append(j['industryField'])
            #工作类型
            job_detail.append(j['industryLables'])
            #发布时间
            job_detail.append(j['createTime'])
            #工作全职
            job_detail.append(j['jobNature'])
            #具体工作
            job_detail.append(j['secondType'])
            # 地铁线路
            job_detail.append(j['linestaion'])

            page_all_job.append(job_detail)
            # time.sleep(15)
        return page_all_job


    def get_job_detail(self,url,ip_list,x):
        headers = {
            'Accept':'*/*',
            'Host': 'www.lagou.com',
            'Referer': url,
            'User-Agent': random.choice(self.agent_list),
        }
        res_status = requests.get(url,headers = headers,proxies = self.get_random_ip(ip_list,x))
        res_status.encoding = 'utf-8'
        if res_status.status_code == 200:
            res_info = res_status.text
            # soup = BeautifulSoup(res_info, 'lxml')
            # job_describe = soup.select('#job_detail > dd.job_bt')[0].text.replace('\n', '')
            # job_position = soup.select('#job_detail > dd.job-address.clearfix')[0].text.replace('\n', '')
            return res_info
        else:
            return None

    def get_random_header(self):
        headers = {'User-Agent': random.choice(self.agent_list),
                   'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   'Accept-Encoding': 'gzip'}
        return headers


    def get_random_ip(self, ip_list,x):
        print(len(ip_list))
        print("正在设置随机代理...")
        # proxy_list = []
        # for ip in ip_list:
        #     proxy_list.append('http://' + ip)
        proxy_ip = random.choice(ip_list)
        # proxy_ip = str(ip_list.iloc[x]['ip'])+':'+str(ip_list.iloc[x]['port'])
        proxies = {'http': proxy_ip,'https':proxy_ip}
        print("代理设置成功.")
        print(proxies)
        return proxies


    def to_datacsv(self,data,
                     columns = ['公司全名','公司链接','公司简称','公司规模','融资阶段','区域',
                                '职位名称','学历要求','工作经验','薪资范围','职位福利','工作领域',
                                '工作类型','发布时间','是否全职','具体工作','地铁线路','工作要求','办公地点']):
        df = pd.DataFrame(data=data, columns=columns)
        #print(df)
        try:
            pd.read_csv('newlagou{}.csv'.format(self.kd))
            print(1)
        except:
            print(2)
            df.to_csv('newlagou{}.csv'.format(self.kd), index=False, encoding='utf-8-sig')
        else:
            df.to_csv('newlagou{}.csv'.format(self.kd), mode='a', index=False, header=False, encoding='utf-8-sig')
        print('保存完成！')
        return '保存完成！'




# pyt_obj = lagouzp()
# ip_list = pyt_obj.get_ips(pn = 3)
# print(ip_list)
# job_info = pyt_obj.get_job_detail(url='https://www.lagou.com/jobs/3145309.html')
# soup = BeautifulSoup(job_info, 'lxml')
# job_describe = soup.select('#job_detail > dd.job_bt')[0].text.replace('\n', '')
# print(job_describe)
#pyt_json = pyt_obj.get_json()
#page_num = pyt_obj.get_total(pyt_json)    #总页数
#print(page_num)
#pyt_obj = lagouzp(kd=kind)
#json_data = pyt_obj.get_json(pn = 32)
#print(json_data)
#job = pyt_obj.get_detailinfo(json_data = json_data)
#print(job)


kind = 'python'
all_python_job = []
pyt_obj = lagouzp(kd=kind)
# all_ip_list = []
# for i in range(1,20):
#     ip_list = pyt_obj.get_ips(pn=i)
#     all_ip_list+=ip_list
# print(all_ip_list)
# df = pd.read_csv('./manageip.csv',index_col = None,names = None)
df1 = pd.read_csv('./xiciip.csv',index_col=None,names = None)
df2 = pd.read_csv('./kuaidaili.csv',index_col=None,names = None)
df3 = pd.concat([df1,df2],ignore_index=True)
list1 = []
for i in range(0,len(df3)):
    list1.append(str(df3.iloc[i]['ip'])+':'+str(df3.iloc[i]['port']))

for i in range(0,3):
    all_python_job = []
    # time.sleep(12)
    try:
        json_data = pyt_obj.get_json(pn=i + 1,ip_list=list1,x = i)
        all_python_job += pyt_obj.get_detailinfo(json_data=json_data)
        print(all_python_job)
    except:
        json_data = pyt_obj.get_json(pn=i + 1,ip_list=list1, x=i+1)
        all_python_job += pyt_obj.get_detailinfo(json_data=json_data)
    finally:
        for y in all_python_job:
            time.sleep(8)
            print(y[0])
            try:
                job_info = pyt_obj.get_job_detail(url=y[0],ip_list=list1,x=all_python_job.index(y)+1)
                print(len(job_info))
                y.append(job_info[0])
                y.append(job_info[1])
                y.remove(y[0])
                time.sleep(2)
                print('暂停2秒')
            except:
                job_info = pyt_obj.get_job_detail(url=y[0], ip_list=list1, x=all_python_job.index(y) + 2)
                print(len(job_info))
                y.append(job_info[0])
                y.append(job_info[1])
                y.remove(y[0])
            finally:
                print('第{}页数据爬取完毕，目前职位总数为：{}'.format(i,len(all_python_job)))
                pyt_obj.to_datacsv(all_python_job)
                print('第{}页数据正在写入，目前职位总数为：{}'.format(i, len(all_python_job)))
        time.sleep(8)



