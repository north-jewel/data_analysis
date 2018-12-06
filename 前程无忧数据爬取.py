import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd
from 前程无忧2 import *
import _thread
import threading
import time
class Data:
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    def __init__(self):
        self.page_list = self.page()
    def h5(self,url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='):
        response = requests.get(url,headers = self.header)
        response.encoding = 'gbk '
        h5 = response.text
        return h5
    def page(self):
        h5 = self.h5()
        soup = BeautifulSoup(h5,'html.parser')
        page_num = soup.find('span', class_='td').text[1:4]
        print(page_num)
        page_list = []
        for i in range(1,int(page_num)+1):
            #print(i)
            page_list.append(i)
        #print(page_list)
        page_list.sort(reverse=True)
        #print(page_list)
        return page_list
    def details_url(self):
        #page_num = self.page()
        while True:
            try:
                print(threading.active_count())
                #print(self.page_list)
                page = self.page_list.pop()
            except IndexError:
                if threading.active_count() == 2:
                    print('下载完成')
            url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(page)
            html = self.h5(url)
            soup = BeautifulSoup(html,'html.parser')
            url_list = soup.find_all('p',class_ = 't1')
            print(len(url_list))
            url_info_list = []
            for i in url_list:
                url_info = i.a.get('href')
                #if url_info[8:22] == 'jobs.51job.com':
                url_info_list.append(url_info)
            self.save_url(url_info_list)
            print('第{}页保存完成'.format(page))
            if threading.active_count() < 10:
                self.multiconductor()
    def save_url(self,url_info_list):
        df = pd.DataFrame(url_info_list,columns = ['详细页面的链接'])
        location = r'C:\Users\16677\Desktop\qianchengwuyou\xiangxiyemian_url3.csv'
        try:
            pd.read_csv(location)
            df.to_csv(location,index=None,header=None,mode='a')
        except FileNotFoundError:
            df.to_csv(location,index=None)
    def multiconductor(self):
        for i in range(5):
            threading.Thread(target=self.details_url, args=()).start()
            time.sleep(3)

if __name__ == '__main__':

    x = Data()
    x.multiconductor()