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
        self.get_ip = self.get_ip()
        self.get_info = self.get_url()['content']['positionResult']
        self.lg_data = self.lg_data()
        self.company_info = self.company_info()
        self.get_company = self.get_company()

    def get_ip(self):
        ip_list = []
        for i in range(5):
            url = 'https://www.kuaidaili.com/free/inha/{}/'.format(i+1)
            info = requests.get(url)
            info.encoding = 'utf-8'
            info_text = info.text

            ip = '<td data-title="IP">(.*?)</td>'

            ip = re.findall(ip,info_text)
            ip_list.append(ip)
        return ip_list

    def get_url(self):  #请求访问页面

        #headers请求头
        headers = {
            'Host': 'www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/70.0.3538.110 Safari/537.36',
        }
        proxies = {
            'http': '140.143.96.216:80', 'https': '140.143.96.216:80',
            'http': '119.27.177.169:80', 'https': '119.27.177.169:80',
            'http': '221.7.255.168:8080', 'https': '221.7.255.168:8080',
        }

        url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.\
            format(self.city)
        info = requests.get(url,headers = headers,proxies = proxies)
        info.encoding = 'utf-8'
        lg_info = info.json()
        return lg_info

    def lg_data(self):   #获取所有招聘信息
        data_num = self.get_info['resultSize']
        company = []
        for i in range(data_num):
            lagou_data = self.get_info['result'][i]
            company.append(lagou_data)
        return company

    def company_info(self):  #获取招聘公司的各项信息
        company_data = []
        for i in self.lg_data:
            # 公司地址
            company_data.append(i['businessZones'])
            # 公司简称
            company_data.append(i['companyShortName'])
            # 公司规模
            company_data.append(i['companySize'])
            # 融资
            company_data.append(i['financeStage'])
            # 所属区域
            company_data.append(i['district'])
            # 职称
            company_data.append(i['positionName'])
            # 招聘学历
            company_data.append(i['education'])
            # 要求工作年限
            company_data.append(i['workYear'])
            # 薪资范围
            company_data.append(i['salary'])
            # 福利待遇
            company_data.append(j['positionAdvantage'])
            # 工作领域
            company_data.append(i['industryField'])
            # 工作类型
            company_data.append(i['industryLables'])
            # 发布时间
            company_data.append(i['createTime'])
            # 工作全职
            company_data.append(i['jobNature'])
            # 具体工作
            company_data.append(i['secondType'])
            # 地铁线路
            company_data.append(i['linestaion'])

        company_data_list = []
        x = 0
        for i in range(len(company_data)//16):
            company_data_list.append([z for z in company_data[x:x+16]])
            x = x+16
        return company_data_list

    def ReadCsv(self):
        for i in self.company_info:
            df = pd.DataFrame({'公司全名':'i[0]','公司简称':'i[1]','公司规模':'i[2]','融资阶段':'i[3]','区域':'i[4]',
                                    '职位名称':'i[5]','工作经验':'i[6]','学历要求':'i[7]','工资':'i[8]','职位福利':'i[9]'})
        pd.read_csv('lagou{}.csv'.format(self.skill_type))

        return '完成'

x = Lg_data()
print(x.company_info())