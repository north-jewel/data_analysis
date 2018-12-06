"""
@author:28646
@file: 2018.12.06前程无忧.py
@time: 2018/12/06
"""
from bs4 import BeautifulSoup
import requests
import glob
def get_url():
    urls = []
    for i in range(1,117):
        url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{}.html'.format(i)
        urls.append(url)
    print(urls)
    return urls

def get_content(url):
    a = 0
    url_list = []
    for i in url:
        res = requests.get(i)
        res.encoding = 'gbk'
        soup = BeautifulSoup(res.text,'html.parser')
        info = soup.select('#resultList > div.el > p > span > a')
        a += 1
        print('现在是第{}页'.format(a))
        for u in info:
            save(u.get('href'))
            print(a,'写入完成')
            #print(u.get('href'))

    # return url_list

def save(url_list):
    print(url_list)
    with open(r'C:\Users\28646\Desktop\各大招聘网爬取\qianchengwuyou.txt','a',encoding='utf-8') as f:
        f.write(url_list)

if __name__ == '__main__':
    get_content(get_url())