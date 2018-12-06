import requests
import re
from bs4 import BeautifulSoup
url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python,2,1.html'
res = requests.get(url)
res.encoding = 'gbk'
soup = BeautifulSoup(res.text, 'html.parser')
page_re = '<span class="td">共(.*?)页，到第</span>'
page = re.findall(page_re, res.text)[0]

def first_url(page):

    big_url = []
    for i in range(1, int(page)+1):
        shouye_url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python,2,{}.html'.format(i)
        big_url.append(shouye_url)
    return big_url

def second_url(page):

    big_url = first_url(page)
    for zong_url in range(len(big_url)):
        res_1 = requests.get(big_url[zong_url])
        res_1.encoding = 'gbk'
        soup1 = BeautifulSoup(res_1.text, 'html.parser')
        url_job_list = soup1.select('p.t1 > span > a')

        for url_job in url_job_list:
            url = url_job.get('href')
            res1 = requests.get(url)
            res1.encoding = 'gbk'
            soup_1 = BeautifulSoup(res1.text, 'html.parser')
            title = soup_1.select_one('h1').get('title')
            company_name = soup_1.select_one('a.catn').get('title')
            info_list = soup_1.select_one('p.msg').get('title').split()
            [info_list.remove(i) for i in (soup_1.select_one('p.msg').get('title').split()) if i is '|']
            company_description = soup_1.select('p.at')
            for i in company_description:
                print(i.get_text())
            company_welfare = soup_1.select('span.sp4')
            for y in company_welfare:
                print(y.text)

            info = soup_1.select_one('p.msg').text.split('|')
            salary = soup_1.select('div.cn > strong')
            for i in salary:
                print(i.text)
            print(salary)
            job_require = soup_1.select_one('div.bmsg').text
            print(job_require)
second_url(page)