import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd

class Data:

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    def __init__(self):
        self.url = 'https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0'
        self.h5 = self.reques()
    def reques(self):
        res = requests.get(self.url,headers = self.headers)
        return res.text
    def seek_data(self):
        soup = BeautifulSoup(self.h5,'html.parser')
        title = soup.find('h1').text.strip() #<class 'str'>
        company_name = soup.select_one('a.catn').get('title')
        salary = soup.select('div.cn > strong')[0].text
        #'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob.fix > div > div.cn > strong'
        company_site_info = soup.find(class_ = 'msg ltype').get('title').split()
        company_site = company_site_info[0]
        experience_required = company_site_info[2]
        edu_required = company_site_info[4]
        release_time = company_site_info[8]
        company_welfare_list = soup.select('span.sp4')
        company_welfare = []
        for i in company_welfare_list:
            company_welfare.append(i.text)
        job_info_list = soup.find(class_ = 'bmsg job_msg inbox').select('p')
        job_info = []
        for i in job_info_list[:-1]:
            job_info.append(i.text.replace(' ',''))
        company_location= soup.find(class_ = 'icon_b i_map').get('onclick').split(',')[1].replace(');return false;','')
        company_info = soup.find(class_ = 'tmsg inbox').text.strip()
        recruitment_info_dict = {}
        recruitment_info_dict['title'] = title
        recruitment_info_dict['company_name'] = company_name
        recruitment_info_dict['salary'] = salary
        recruitment_info_dict['company_site'] = company_site
        recruitment_info_dict['experience_required'] = experience_required
        recruitment_info_dict['edu_required'] = edu_required
        recruitment_info_dict['release_time'] = release_time
        recruitment_info_dict['company_welfare'] = [company_welfare]
        recruitment_info_dict['job_info'] = [job_info]
        recruitment_info_dict['company_location'] = company_location
        recruitment_info_dict['company_info'] = company_info
        #print(recruitment_info_dict)
        return recruitment_info_dict
    def save(self):
        recruitment_info_dict = self.seek_data()
        df = pd.DataFrame(recruitment_info_dict)
        df.to_csv(r'C:\Users\16677\Desktop\qianchengwuyou\qiancheng_data.csv',index=None)
if __name__ == '__main__':
    Data().save()