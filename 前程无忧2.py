import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd

class Data2:

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    # def __init__(self,url = 'https://jobs.51job.com/beijing/108038642.html?s=01&t=0'):
    #     self.url = url
    #     self.h5 = self.reques()
    def reques(self,url):
        res = requests.get(url,headers = self.headers)
        return res.text
    def seek_data(self,h5):
        soup = BeautifulSoup(h5,'html.parser')
        title = soup.find('h1').text.strip() #<class 'str'>
        company_name = soup.select_one('a.catn').get('title')
        salary = soup.select('div.cn > strong')[0].text
        #'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob.fix > div > div.cn > strong'
        company_site_info = soup.find(class_ = 'msg ltype').get('title').split()
        company_site = company_site_info[0]
        experience_required = company_site_info[2]
        edu_required = company_site_info[4]
        try:
            release_time = company_site_info[8]
        except IndexError:
            release_time = company_site_info[6]
        try:
            company_welfare_list = soup.select('span.sp4')
            company_welfare = []
            for i in company_welfare_list:
                company_welfare.append(i.text)
        except:
            company_welfare = None
        job_info_list = soup.find(class_ = 'bmsg job_msg inbox').select('p')
        job_info = []
        for i in job_info_list[:-1]:
            job_info.append(i.text.replace(' ',''))
        try:
            company_location= soup.find(class_ = 'icon_b i_map').get('onclick').split(',')[1].replace(');return false;','')
        except AttributeError:
            company_location = None
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
    def save(self,recruitment_info_dict):
        #recruitment_info_dict = self.seek_data()
        df = pd.DataFrame(recruitment_info_dict)
        location = r'C:\Users\16677\Desktop\qianchengwuyou\qiancheng_data2.csv'
        #df.to_csv(location,index=None,made = 'a')
        try:
            pd.read_csv(location)
            df.to_csv(location,index=None,header=None,mode='a')
        except FileNotFoundError:
            df.to_csv(location,index=None)
    def read_url(self):
        df_url = pd.read_csv(r'C:\Users\16677\Desktop\qianchengwuyou\xiangxiyemian_url2.csv')

        for url in df_url.values[5252:]:
            if url[0][8:22] == 'jobs.51job.com':
                h5 = self.reques(url[0])
                try:
                    recruitment_info_dict = self.seek_data(h5)
                    self.save(recruitment_info_dict)
                    print('{}链接爬取完成'.format(url[0]))
                except:
                    #recruitment_info_dict = None
                    try:
                        df = pd.read_csv(r'C:\Users\16677\Desktop\qianchengwuyou\error.csv')
                        #df = pd.DataFrame(url,columns=['报错链接'],mode='a')
                        df.to_csv(r'C:\Users\16677\Desktop\qianchengwuyou\error.csv',index=None,header=None,mode='a')
                        print('{}报错已保存'.format(url[0]))
                    except FileNotFoundError:
                        df = pd.DataFrame(url, columns=['报错链接'])
                        print('{}报错已保存'.format(url[0]))
            else:
                pass
if __name__ == '__main__':
    Data2().read_url()