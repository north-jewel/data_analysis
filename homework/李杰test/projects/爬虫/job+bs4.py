from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import numpy as np

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}


class Bs4test:
    def __init__(self,url):
        self.url = url
    def Company_code(self):
        html_doc = requests.get(self.url, headers=headers)
        html_doc.encoding = 'gbk'
        html_doc = html_doc.text

        return html_doc
    def Company_info(self):

        soup = BeautifulSoup(self.Company_code(),'html.parser')
        #职位名称
        title = soup.find(class_='cn').h1.get('title')
        title_2 = soup.find('h1').text.strip()
        #公司名称
        company = soup.find(class_='catn').text.strip()
        company_2 = soup.find(class_='catn').get('title')
        company_3 = soup.find()
        #公司url
        company_url = soup.find(class_='catn').get('href')
        #公司福利
        company_weafer = soup.find_all(class_='sp4')
        welfare =[]
        for i in company_weafer:
            welfare.append(i.text.strip())
        #职位要求
        company_re = soup.find(class_='bmsg job_msg inbox').find_all('p')
        ask_for = []
        for i in company_re:
            ask_for.append(i.text.strip())
        #招聘需求
        company_post = soup.find(class_='msg ltype').text.strip()
        post = str(company_post.split('|')).replace(r'\xa0\xa0','')
        #月薪
        monthly_pay = soup.find(class_='cn').find('strong').text
        #公司地址

        #company_address = soup.find(class_='bmsg inbox').find(class_='fp').text
        company_address_2 = soup.select('div.tCompany_main > div:nth-of-type(2) > div > p')[0].text.strip()
        #公司类型
        company_message = soup.find(class_='tmsg inbox').text.strip()
        company_message_2 = soup.find(class_='com_tag').find_all('p')
        message = []
        for i in company_message_2:
            message.append(i.text.strip())
        company_post = str(company_post.split('|')).replace(r'\xa0\xa0','')
        company_postt = eval(company_post)
        if company_postt[2][0] =='招':
            company_postt.insert(2, '无学历要求')

        a = np.array([title,company_2,company_url,str(welfare),str(ask_for),str(company_post.split('|')).replace(r'\xa0\xa0',''),monthly_pay,company_address_2,company_message,message[0],company_postt[2]])
        df = pd.DataFrame(a).T
        print(a)
        df.to_csv('zhaopin.csv', mode='a', index=False, header=None, encoding='utf-8-sig')

        return 'over'

url = 'https://jobs.51job.com/beijing-xcq/99999944.html'
class Company_page:
    def __init__(self,url):
        self.url = url
    def Page(self):
        html_doc= requests.get(self.url,headers=headers)
        html_doc.encoding='gbk'
        html_doc = html_doc.text
        soup = BeautifulSoup(html_doc,'html.parser')
        company_page = soup.find_all(class_='t1 ')

        # company_name=soup.select('#resultList > div > span.t2 > a')[0]
        # print(company_name.get('href'))
        # print(company_name.text)
        #
        # company_site = soup.find_all('span',class_='el')
        # print(company_site)
        # for i in company_site:
        #     print(i.find())
        page_list = []
        for i in company_page:
            #print(i.find('a').get('href'))
            #print(i.find('a').text.strip())

            # page_list[i.find('a').get('href')]=i.find('a').text.strip()
            # with open('info.txt','a') as f:
            #     f.write(i.find('a').get('href'))
            page_list.append(i.find('a').get('href'))
        return page_list
for i in range(1,3):
    page_url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(i)
    uel = Company_page(page_url).Page()
    #print(uel)
    for i in uel:
        Bs4test(i).Company_info()

















