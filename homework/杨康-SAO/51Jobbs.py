from job_spider import *
from argfile import *
from bs4 import BeautifulSoup
import _thread
import threading
import pandas as pd

class JobSpider:
    def __init__(self, area_word, key_word):
        self.area_word = area_word
        self.key_word = key_word



    def job_info(self, job_url):

        job_dict = {}
        try:
            job_obj = Spider(url=job_url)
            job_text = job_obj.html5()
            soup = BeautifulSoup(job_text, 'html.parser')

            skill_type = soup.h1.text.strip()
            #print(skill_type)
            city = soup.find('p', class_='msg ltype').text.strip().split('|')[0]

            company_name = soup.find('div', class_='com_msg').text.strip()

            company_size = soup.select('div.com_tag > p')[1].text

            company_type = soup.select('div.com_tag > p')[2].text.strip()

            company_description = soup.find('div', class_='tmsg inbox').text.strip()

            company_location = soup.find('div', class_='bmsg inbox').text.replace('地图','').strip()

            salary = soup.select_one('div.cn > strong').text

            g = soup.find('div', class_='mt10').text
            job_required = soup.find('div',class_='bmsg job_msg inbox').text.replace(g,'').replace('微信分享','').strip()

            experience_required = soup.find('p', class_='msg ltype').text.strip().split('|')[1]

            company_welfare = soup.find('div', class_='t1').text.strip()
        except AttributeError:
            job_dict[self.key_word] = {'key_word':self.key_word,
                                       'skill_type': None,
                                       'city': None,
                                       'company_name': None,
                                       'company_size': None,
                                       'company_type': None,
                                       'company_description': None,
                                       'company_location': None,
                                       'salary': None,
                                       'job_required': None,
                                       'experience_required': None,
                                       'company_welfare': None,
                                       'job_url': job_url, }
            return job_dict[self.key_word]
        else:
            job_dict[self.key_word] = {'key_word':self.key_word,
                                       'skill_type': skill_type,
                                       'city': city,
                                       'company_name': company_name,
                                       'company_size': company_size,
                                       'company_type': company_type,
                                       'company_description': company_description,
                                       'company_location': company_location,
                                       'salary': salary,
                                       'job_required': job_required,
                                       'experience_required': experience_required,
                                       'company_welfare': company_welfare,
                                       'job_url': job_url, }
            return job_dict[self.key_word]



    def spider_51Job(self):

        area_word = list(area.keys())[list(area.values()).index(self.area_word)]
        job_obj = Spider(url='https://search.51job.com/list/{},000000,0000,00,9,99,{},2,1.html?'.format(area_word, self.key_word, ))
        job_text = job_obj.html5()
        # print(job_url)
        soup = BeautifulSoup(job_text, 'html.parser')
        page = soup.find('span', class_='td').text.replace('共', '').replace('页，到第', '').strip()
        # page = 2
        for i in range(int(page)):
            home_page_url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html?'.format(area_word, self.key_word, i + 1)
            job_obj = Spider(url=home_page_url)
            job_text = job_obj.html5()
            # print(job_url)
            soup = BeautifulSoup(job_text, 'html.parser')
            soup_url = soup.find_all('p', class_='t1')
            for index in range(len(soup_url)):
                job_info_dict = self.job_info(soup_url[index].a.get('href'))
                print(job_info_dict['company_location'])
                df = pd.DataFrame.from_dict(job_info_dict, orient='index').T

                try:
                    pd.read_csv(r'C:\Users\yk\Desktop\51Job_info.csv')
                except FileNotFoundError:
                    df.to_csv(r'C:\Users\yk\Desktop\51Job_info.csv', index=False, encoding='utf_8_sig')
                else:
                    df.to_csv(r'C:\Users\yk\Desktop\51Job_info.csv', index=False, header=None, mode='a',
                              encoding='utf_8_sig')






if __name__ == '__main__':
    x = JobSpider('北京', 'python')
    n = x.spider_51Job()

