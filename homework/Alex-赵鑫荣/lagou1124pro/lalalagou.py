# -*- coding: utf-8 -*-
"""
   File Name：     lalalagou
   Product:        PyCharm
   Project:    python4
   File:       lalalagou.py
   Author :       ZXR
   date：          2018/12/5
   time:           9:52
"""
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
import numpy as np
import matplotlib.pyplot as plt

class lagouzp:
    '''
    爬取拉勾网招聘信息
    '''
    def __init__(self,ct = '北京',kd = 'python'):
        '''
        初始化时的属性
        :param ct: 限定城市     可以为None(即全国)
        :param pn: 页面：即第几页
        :param kd: 搜索关键字
        '''
        self.ct = ct
        #self.pn = pn
        self.kd = kd

    def get_json(self,pn = 1):
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        #设置代理
        proxies ={
            'http': '140.143.96.216:80', 'https': '140.143.96.216:80',
            'http': '119.27.177.169:80', 'https': '119.27.177.169:80',
            'http': '221.7.255.168:8080', 'https': '221.7.255.168:8080'
        }

        res_status = requests.post(url,headers = headers,data = param)
        res_status.encoding = 'utf-8'
        if res_status.status_code == 200:
            res_info = res_status.json()
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
            # 公司全名
            job_detail.append(j['companyFullName'])
            # 公司链接
            cm_url = 'https://www.lagou.com/gongsi/{}.html'
            job_detail.append(cm_url.format(j['companyId']))
            # 公司简称
            job_detail.append(j['companyShortName'])
            # 公司规模
            job_detail.append(j['companySize'])
            # 融资
            job_detail.append(j['financeStage'])
            # 所属区域
            job_detail.append(j['district'])
            # 职称
            job_detail.append(j['positionName'])
            # 招聘学历
            job_detail.append(j['education'])
            # 要求工作年限
            job_detail.append(j['workYear'])
            # 薪资范围
            job_detail.append(j['salary'])
            # 福利待遇
            job_detail.append(j['positionAdvantage'])
            # 工作领域
            job_detail.append(j['industryField'])
            # 工作类型
            job_detail.append(j['industryLables'])
            #工作技能
            job_detail.append(j['skillLables'])
            # 发布时间
            job_detail.append(j['createTime'])
            # 工作全职
            job_detail.append(j['jobNature'])
            # 具体工作
            job_detail.append(j['secondType'])
            # 地铁线路
            job_detail.append(j['linestaion'])

            page_all_job.append(job_detail)
        return page_all_job

    def to_datacsv(self,data,
                     columns = ['工作链接','公司全名','公司链接','公司简称','公司规模','融资阶段','区域',
                                '职位名称','学历要求','工作经验','薪资范围','职位福利','工作领域',
                                '工作类型','工作技能','发布时间','是否全职','具体工作','地铁线路']):
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


kind = 'python'

#pyt_obj = lagouzp()
#pyt_json = pyt_obj.get_json()
#page_num = pyt_obj.get_total(pyt_json)    #总页数
#print(page_num)
#pyt_obj = lagouzp(kd=kind)
#json_data = pyt_obj.get_json(pn = 32)
#print(json_data)
#job = pyt_obj.get_detailinfo(json_data = json_data)
#print(job)



all_python_job = []
for i in range(3,101):
    all_python_job = []
    pyt_obj = lagouzp(kd=kind)
    json_data = pyt_obj.get_json(pn = i)
    time.sleep(15)
    all_python_job += pyt_obj.get_detailinfo(json_data = json_data)
    print('第{}页数据爬取完毕，目前职位总数为：{}'.format(i,len(all_python_job)))
    pyt_obj.to_datacsv(all_python_job)
    print('第{}页数据正在写入，目前职位总数为：{}'.format(i, len(all_python_job)))
    time.sleep(15)
