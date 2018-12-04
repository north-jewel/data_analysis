import requests,re
import math
import pandas as pd
from bs4 import BeautifulSoup
import time
import urllib.parse

class lagou():
    headers = {  
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',  
            'Host':'www.lagou.com',  
            'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',  
            'X-Anit-Forge-Code':'0',  
            'X-Anit-Forge-Token': 'None',  
            'X-Requested-With':'XMLHttpRequest'  
            } 
    def __init__(self,key_word,city):
        self.key_word = key_word
        self.city = city
        
    def get_json(self,url,num):
        
        my_data = {
            'first':'true',
            'pn':num,
            'kd':self.key_word}
        res = requests.post(url,headers = self.headers,data = my_data)
        res.encoding = 'utf-8'
        page = res.json()
        return page
    def get_page_num(self,count):
        res = math.ceil(count/15)
        if res>30:
            return 30
        else:
            return res
    def get_page_info(self,job_list):
        page_info_list = []
        for i in job_list:
            job_info = []  
            job_info.append(i['companyFullName'])  
            job_info.append(i['companyShortName'])  
            job_info.append(i['companySize'])  
            job_info.append(i['financeStage'])  
            job_info.append(i['district'])  
            job_info.append(i['positionName'])  
            job_info.append(i['workYear'])  
            job_info.append(i['education'])  
            job_info.append(i['salary'])  
            job_info.append(i['positionAdvantage'])
            
            page_info_list.append(job_info)
        print(page_info_list)

        return page_info_list
    def get_page_demand(self,job_list):
        possionId_list = []
        for i in job_list:

            possionId_list.append(i['positionId'])
        content = []
        for a in possionId_list:
            url = 'https://www.lagou.com/jobs/.html'.format(a)
            res = requests.get(url)
            #res = BeautifulSoup(res.content,'html.parser')
            #print(res.status_code)
            res.encoding = 'utf-8'
            con = res.text
            demand = '''<div>
        <p>职位描述：</p>
(.*?)
        </div>'''
            #demand = res.find('dd',{'class','job_bt'}).find_all('p')
            demand = re.findall(demand,con,re.S)
            content.append(demand)
        print(content)
        print(possionId_list)

    def main(self):
        city = urllib.parse.quote(self.city)
        url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(city)
        page1 = self.get_json(url,1)
        total_count = page1['content']['positionResult']['totalCount']
        num = self.get_page_num(total_count)
        print('职位总数:{},页数:{}'.format(total_count,num))
        total = []
        for i in range(1,2):
            page = self.get_json(url,i)
            job_list = page['content']['positionResult']['result']
            page_info = self.get_page_info(job_list)
            total +=page_info
            self.get_page_demand(job_list)
        print(total)
        df = pd.DataFrame(data = total,columns = ['公司全名','公司简称','公司规模','融资阶段','区域','职位名称','工作经验','学历要求','工资','职位福利'])

        df.to_excel(r'C:\Users\hp\Desktop\拉钩.xlsx',sheet_name = 'jobs',index = False)
        #df.to_csv('拉钩招聘.csv', index=False, encoding='utf-8-sig')
        print('已保存为excel文件.')
if __name__ == '__main__':
    lagou('python','北京').main()

        
        
