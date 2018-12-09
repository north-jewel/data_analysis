import requests
import re
from bs4 import BeautifulSoup
from secondurlpy import Result
from cityinfo import city_info

class Job:
    result = Result()
    CITY = city_info()

    def __init__(self, city, job, encoding='gbk'):
        self.city = city
        self.job = job
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
        self.encoding = encoding
        self.first_url = self.first_url()

    def first_url(self,):
        num = self.CITY[self.city]
        print(num)
        print(self.job)
        url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,1.html'.format(num, self.job)
        url_res = requests.get(url, headers=self.header)
        url_res.encoding = self.encoding
        page = '<span class="td">共(.*?)页，到第</span>'

        page = re.findall(page, url_res.text)[0]
        print (page)
        job_url_list = []
        for i in range(1, 6):
            if i > 2:
                url = url.replace('2,{}.'.format(i - 1), '2,{}'.format(str(i) + '.'))
            else:
                url = url.replace('1.', '{}'.format(str(i) + '.'))

            job_url_list.append(url)
        print(job_url_list)
        return job_url_list

    def second_url(self):
        for every_page_url in self.first_url:
            url_res = requests.get(every_page_url, headers=self.header)
            url_res.encoding = self.encoding
            soup = BeautifulSoup(url_res.text,'html.parser')
            every_url_list = soup.select('p.t1 > span  > a')
            every_url_list = [i.get('href') for i in every_url_list]
            print(every_url_list)
j = Job('北京','python')
j.second_url()




