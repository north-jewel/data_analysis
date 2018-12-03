import requests
import pandas as pd
import urllib.parse
import time
import glob
import os
import re
import numpy as np
#from ip_rinse import *
# class Agency_IP():
#     def __init__(self):
#         self.url = 'http://www.xicidaili.com/'
#         self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
#
#     def html(self):
#         h5 = requests.get(self.url,headers = self.header).text
#         #print(h5)
#         return h5
#     def ip(self):
#         h5 = self.html()
#         ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", h5, re.S)
#         #print(ip_list)
#         return ip_list
#     def rinse(self):
#         httpResult = self.ip()[:10]
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
#             'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='}
#         usable_ip = []
#         for i in httpResult:
#             proxies = {
#                 'http': '{}:{}'.format(i[0],i[1]),
#                 'https': '{}:{}'.format(i[0],i[1])
#             }
#             try:
#                 print(proxies)
#                 response = requests.get(url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',
#                                         proxies=proxies, headers=headers)
#                 usable_ip.append(i)
#             except:
#                 print('{} ip报错'.format(i))
#         print(usable_ip)
#         return usable_ip
class Data:
    headers_list = [
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
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='}
    def __init__(self,keyword,page):
        # self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        # 'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='}
        self.page = page
        self.keyword = keyword
        self.url = self.interface_judge()
        #self.ip_list = self.Agency_IP()
    def interface_judge(self):
        '''
        判断是全国性爬取还是地区性
        :return:url 返回数据的接口
        '''
        if self.keyword == None:
            url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        else:
            coding = urllib.parse.quote(self.keyword)
            url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false'.format(coding)
            print(url)
        return url
    def Agency_IP(self):
        url = 'http://www.xicidaili.com/'
        header = {}
        header['User-Agent'] = self.headers_list[np.random.randint(0,len(self.headers_list))]
        h5 = requests.get(url, headers=header).text
        ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", h5, re.S)
        return ip_list
    def rinse(self):
        ip_list = self.Agency_IP()[:9]
        print('正在清理ip池')
        #httpResult = self.Agency_IP().rinse()[:30]
        usable_ip = []
        for i in ip_list:
            proxies = {
                'http': '{}:{}'.format(i[0],i[1]),
                'https': '{}:{}'.format(i[0],i[1])
            }
            try:
                print(proxies)
                response = requests.get(url = 'http://2018.ip138.com/ic.asp',
                                        proxies=proxies, headers=self.headers)
                usable_ip.append(i)
            except:
                print('{} ip报错'.format(i))
        #print(usable_ip)
        return usable_ip
        # ip = ip_list[np.random.randint(0,len(ip_list))]
    def request(self):

        '''
        用代理ip请求要爬取数据的接口
        :return:
        '''
        ip_list = self.rinse()
        print(ip_list)
        for i in ip_list:
        #num = np.random.randint(0, len(ip_list))
        #ip = ip_list[num]
        #print(ip)
            params = {'pn': self.page,
                        'kd': 'python'}
            proxies = {
                    'http': '{}:{}'.format(i[0], i[1]),
                    'https': '{}:{}'.format(i[0], i[1])
                }
            try:
                res = requests.post(self.url,headers = self.headers,proxies = proxies ,params = params)
                info_list = res.json()['content']['positionResult']['result']
                print(info_list)
                return info_list
            except KeyError:
                pass

    def data_extract(self):
        '''
        将需要的数据进行整合
        :return: info_dict 所有需求的数据整合成一个字典
        '''
        info_list = self.request()
        info_dict = {}
        city_list = []
        company_size_list = []
        experience_required_list = []
        edu_required_list = []
        company_name_list = []
        company_location_list = []
        positionId_list = []
        for i in info_list:
            city_list.append(i['city'])
            company_size_list.append(i['companySize'])
            experience_required_list.append(i['workYear'])
            edu_required_list.append(i['education'])
            company_name_list.append(i['companyFullName'])
            company_location_list.append((i['district'],i['linestaion']))
            positionId_list.append(i['positionId'])
        info_dict['city'] = city_list
        info_dict['company_size'] = company_size_list
        info_dict['positionId'] = positionId_list
        info_dict['experience_required'] = experience_required_list
        info_dict['edu_required'] = edu_required_list
        info_dict['company_name'] = company_name_list
        info_dict['company_location'] = company_location_list
        return info_dict
    def save_data(self):
        '''
        将获取到的数据保存成csv格式
        :return:
        '''
        info_dict = self.data_extract()
        df = pd.DataFrame(info_dict)
        if self.keyword == None:
            location = r'C:\Users\16677\Desktop\drag_hook_data\全国拉勾网数据.csv'
        else:
            location = r'C:\Users\16677\Desktop\drag_hook_data\{}拉勾网数据.csv'.format(self.keyword)
        try:
            pd.read_csv(location)
            if self.page >=1:
                df.to_csv(location,index=None,header=None,mode='a')
        except FileNotFoundError:
            df.to_csv(location,index=None)
        #self.merge()
    def merge(self):
        '''
        将爬取到的数据合并成一个csv文件
        :return:
        '''
        merge_list = []
        self.csv_list = glob.glob('*.csv')
        print(self.csv_list)
        for i in self.csv_list:
            f = open(i,encoding='utf-8')
            df = pd.read_csv(f)
            #print(df)
            merge_list.append(df)
        #print(merge_list)
        data_csv = pd.concat(merge_list,ignore_index=True)
        if self.keyword == None:
            location = r'C:\Users\16677\Desktop\drag_hook_data\全国拉勾网数据合并{}.csv'.format(self.page)
        else:
            location = r'C:\Users\16677\Desktop\drag_hook_data\{}拉勾网数据合并'.format(self.keyword)
        data_csv.to_csv(location)
        print(data_csv)
    #     self.delete()
    # def delete(self):
    #     for i in self.csv_list:
    #         os.remove(i)

if __name__ == '__main__':
    for i in range(1,5):
        Data(keyword=None,page=i).save_data()
        print('第{}页数据爬取完成'.format(i))
        #time.sleep(10)

