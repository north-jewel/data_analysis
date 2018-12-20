import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

class Data:
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    # def __init__(self):
    #     self.url = 'https://price.pcauto.com.cn/top/oil/s1-t2.html'
    #     # self.url = 'https://price.pcauto.com.cn/top/oil/s1-t4.html'
    #               #'https://price.pcauto.com.cn/top/oil/s1-t4-p2.html'
    #     #self.h5 = self.h5(self.url)
    def h5(self,url):
        res = requests.get(url,headers = self.header)
        return res.text
    def page_info(self,url):
        #url = 'https://price.pcauto.com.cn/top/oil/s1-t3.html'
        h5 = self.h5(url)
        soup = BeautifulSoup(h5, 'html.parser')
        try:
            page_info = soup.find('div', class_='pcauto_page').text[-4]
            print(page_info)
            return int(page_info)
            #self.data_capture(int(page_info))
        except AttributeError:
            return 1
            #self.data_capture(1)

    def data_capture(self,url):
        #for p in range(1,page+1):
        #url = 'https://price.pcauto.com.cn/top/oil/s1-t3-p{}.html'.format(p)
        h5 = self.h5(url)
        soup = BeautifulSoup(h5,'html.parser')
        car_name = []
        official_price = []
        brand_list = []
        rank_list = []
        carfuelc_list = []
        MIITfuelc_list = []
        displacement_list = []

        car_info = soup.find_all('p',class_ = 'sname')
        for i in car_info:
            car_name.append(i.text)

        carfuelc_info = soup.find_all('p',class_ = 'col')
        for i in carfuelc_info:
            info = i.text
            if info[0:6] == '车主平均油耗':
                carfuelc_list.append(info.split('：')[1])
            if info[0:5] == '工信部油耗':
                MIITfuelc_list.append(info.split('：')[1])
            if info[0:2] == '排量':
                displacement_list.append(info.split('：')[1].replace('\n',''))
            if info[0:2] == '官方':
                official_price.append(info.split('：')[1])
            if info[0:2] == '品牌':
                brand_list.append(info.split('：')[1])
            if info[0:2] == '级别':
                rank_list.append(info.split('：')[1])
                #print(rank_list)
        # print(official_price)
        # print(brand_list)
        # print(rank_list)
        # print(displacement_list)
        # print(MIITfuelc_list)
        # print(carfuelc_list)
        url_list = []
        url_info = soup.find_all('div', class_='pic')
        for i in url_info:
            url_list.append(i.a.get('href'))
        data_tuple = self.detail_data(url_list)
        #print(url_list)
        # page_info = soup.find('div',class_ = 'pcauto_page').text[-4]
        # print(page_info)
        data_dict = {}
        data_dict = {'car_name':car_name,
                         'official_price':official_price,
                         'brand':brand_list,
                         'rank':rank_list,
                         'displacement':displacement_list,
                         'MIITfuelc':MIITfuelc_list,
                         'carfuelc':carfuelc_list,
                         'car_type':data_tuple[0],
                         'gearbox': data_tuple[1],
                         'ranking': data_tuple[2],
                         'car_strength': data_tuple[3],
                         'configuration': data_tuple[4],
                         'major': data_tuple[5],
                         'owner_evaluate': data_tuple[6],
                         'price': data_tuple[7],
                    }
        self.save_data(data_dict)
        #print('{}-第{}页爬取完成'.format(rank_list[0],p))
    def detail_data(self,detail_utl_list):
        #self.detail_url = self.detailed_info()
        car_type_list = []
        gearbox_list = []
        ranking_list = []
        car_strength_list = []
        configuration_list = []
        major_list = []
        owner_evaluate_list = []
        price_list = []
        for i in detail_utl_list:
            #info_list = []
            url = 'https://price.pcauto.com.cn' + i
            res = requests.get(url, headers=self.header).text
            soup = BeautifulSoup(res,'html.parser')
            car_type_info = soup.find('ul',class_ = 'des').text.replace('\n','').split(':')
            #soup2 = BeautifulSoup(car_type_info,'html.parser')
            #car_info = car_type_info.find_all('a')
            car_type_list.append(car_type_info[-1])
            gearbox_list.append(car_type_info[-2].replace('车身类型',''))
            #print(car_type_info)
            # print(car_type_list)
            # print(gearbox_list)

            ranking_info = soup.select_one('#strengthProcess > p').text.split('\n')[1].replace('\r','')
            ranking_list.append(ranking_info)
            #print(ranking_list)

            car_strength_info = soup.find_all('p',class_ = 'score')
            strength_list = []
            for i in car_strength_info:
                strength_list.append(i.text)
            car_strength_list.append(strength_list[0])
            configuration_list.append(strength_list[1])
            major_list.append(strength_list[2])
            owner_evaluate_list.append(strength_list[3])
            price_list.append(strength_list[4])
        # print(car_type_list)
        # print(gearbox_list)
        # print(ranking_list)
        # print(car_strength_list)
        # print(configuration_list)
        # print(major_list)
        # print(owner_evaluate_list)
        # print(price_list)
        #print('*'*20)
        return (car_type_list,gearbox_list,ranking_list,car_strength_list,configuration_list,major_list,owner_evaluate_list,price_list)
    def save_data(self,dict):
        df = pd.DataFrame(dict)
        try:
            pd.read_csv('taipingyangqiche.csv')
            df.to_csv('taipingyangqiche.csv',index = None,header=None,mode='a')
        except FileNotFoundError:
            df.to_csv('taipingyangqiche.csv',index=None)
    def paqu(self):
        for i in range(20,21):
            url = 'https://price.pcauto.com.cn/top/oil/s1-t{}.html'.format(i)
            page = self.page_info(url)
            for p in range(1,page+1):
                url = 'https://price.pcauto.com.cn/top/oil/s1-t{}-p{}.html'.format(i,p)
                self.data_capture(url)
                print('{}-第{}页爬取完成'.format(i, p))
if __name__ == '__main__':
    Data().paqu()