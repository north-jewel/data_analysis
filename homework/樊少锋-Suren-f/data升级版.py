import requests
import re
import numpy as np
import pandas as pd

class Lg_data:
    '''
    city:城市
    skill_type:技能
    '''
    def __init__(self,city='北京',skill_type='python爬虫'):
        self.city = city
        self.skill_type = skill_type
        self.get_url = self.get_url()
        self.get_page = self.get_page()
        self.lg_data = self.lg_data()
        self.company_info = self.company_info()

    def get_url(self,page = 2):  #请求访问页面

        param = {
            'page': page,  # 页码
            'skill_type': self.skill_type   #关键字
        }
        #headers请求头
        headers = {
            'Host': 'www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/70.0.3538.110 Safari/537.36',
        }
        url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.\
            format(self.city)
        info = requests.get(url,headers = headers,params=param)
        info.encoding = 'utf-8'
        if info.status_code == 200:
            lg_info = info.json()['content']['positionResult']

        return lg_info

    def get_page(self):  #计算数据总页数
        pass

    def lg_data(self):   #获取所有招聘信息
        data_num = self.get_url['resultSize']
        company = []
        for i in range(data_num):
            lagou_data = self.get_url['result'][i]
            company.append(lagou_data)
        return company

    def company_info(self):  #获取招聘公司的各项信息
        company_data = []
        for i in self.lg_data:
            # 公司地址
            company_data.append(i['district'])
            # 公司名称
            company_data.append(i['companyFullName'])
            # 公司规模
            company_data.append(i['companySize'])
            # 职称
            company_data.append(i['positionName'])
            # 招聘学历
            company_data.append(i['education'])
            # 要求工作年限
            company_data.append(i['workYear'])
            # 薪资范围
            company_data.append(i['salary'])
            # 福利待遇
            company_data.append(i['positionAdvantage'])
            # 工作领域
            company_data.append(i['industryField'])
            # 工作类型
            company_data.append(i['industryLables'])
            # 发布时间
            company_data.append(i['createTime'])
            # 具体工作
            company_data.append(i['secondType'])

        company_data_list = []
        x = 0
        for i in range(len(company_data)//12):
            company_data_list.append([z for z in company_data[x:x+12]])
            x = x+12
        return company_data_list

    def ReadCsv(self):
        #print(self.company_info)
        df = pd.DataFrame(data= self.company_info,columns = ['公司地址','公司名称','公司规模','职称','招聘学历',
                                     '要求工作年限','薪资范围','福利待遇','工作领域',
                                     '工作类型','发布时间','具体工作'])
        df.to_csv(r'C:\Users\20312\Desktop\123.csv',index = False,encoding='gb2312')

        return '完成'

x = Lg_data()
x.ReadCsv()

