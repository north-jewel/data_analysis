"""
@author:Sbaix
@file: Taipingyang.py
@time: 2018/12/14
"""
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import os
from pathlib import Path

class TaiPingYange:
    def __init__(self,url):
        self.url=url
        self.html=self.top(self.url)
        self.car_rank=self.car_rank()
    def top(self,link):
        con=requests.get(link)
        con.encoding='gb2312'
        return con.text
    def car_rank(self):
        '''
        :return:各种车型的链接
        '''
        soup=BeautifulSoup(self.html,'html.parser')
        ul=soup.find('ul',class_="").find_all('a',class_='dd')
        l='https://price.pcauto.com.cn{}'
        url_list=[]
        for i in ul:
            links=i.get('href')
            #print(type(links))
            link=l.format(links)
            url_list.append(link)
        #print(url_list)
        return url_list

    def page_info(self):
        page_url = []
        car_rank=self.car_rank
        for url in car_rank:

            soup=BeautifulSoup(self.top(url),'html.parser')
            try:
                page=soup.find('div',class_='pcauto_page').find_all('a')
            except AttributeError:
                pass
            else:
                for link in page:
                    link = link.get('href')
                    links='https://price.pcauto.com.cn{}'.format(link)
                    page_url.append(links)
                page_url=list(set(page_url))
        self.car_rank.extend(page_url)
        page_rank=self.car_rank
        return page_rank
    def car_info(self):
        '''
        :return: 全部车的信息,保存为df
        '''

        n=1
        page_rank=self.page_info()
        print('共46页')
        for url in page_rank:
            carname_list = []
            gearbox_list = []
            cartype_list = []
            carstrength_list = []
            configuration_list = []
            major_list = []
            ownerevaluate_list = []
            price_list = []
            # versions_list=[]
            # versionsp_list=[]
            officialprice_list = []
            carfuelc_list = []
            brand_list = []
            MIITfuelc_list = []
            rank_list = []
            displacement_list = []
            ranking_list = []
            time.sleep(3)
            print('爬取第{}页'.format(n))
            soup=BeautifulSoup(self.top(url),'html.parser')
            div=soup.find_all('div',class_='info')
            for i in div:
                #车名
                carname=i.find('p',class_='sname').text
                # *********************************************************************************************
                #官方价
                officialprice=i.find('p',class_='col col1').em.text
                #车主平均油耗
                carfuelc=i.select('p.col > em')[1].text
                #品牌
                brand=i.find_all('p',class_='col col1')[1].text.replace('品牌：','')
                #工信部油耗
                MIITfuelc=i.find_all('p',class_='col')[3].text
                #级别
                rank=i.find_all('p',class_='col')[4].text.replace('级别：','')
                #排量
                displacement=i.find_all('p',class_='col')[5].text.replace('排量：','')
                #print(page)
                # 车名链接
                car_url = i.find('p', class_='sname').a.get('href')
                carname_url = 'https://price.pcauto.com.cn{}'.format(car_url)
                sop = BeautifulSoup(self.top(carname_url), 'html.parser')
                ul = sop.find('ul', class_='des')
                # 变速箱
                gearbox = ul.find_all('p')[2].find('a').text.strip()
                # 车身类型
                cartypes = sop.select('#detail > div.box-b > div.infor > div.price > ul > li:nth-of-type(2) > p:nth-of-type(2) > em > a:nth-of-type(1)')
                cartype = cartypes[0].text.strip()
                # 排名
                ranking = sop.find('div', class_='strength').find('p',class_='tip').text.replace('查看详情>>','')
                #print(ranking)
                # 车实力
                carstrength = sop.find('p', class_='score').text
                # 配置水平
                four_div = sop.find('div', class_='processBarWrap').find_all('p', class_='blue score')
                configuration = four_div[0].text
                # 专业测评
                major = four_div[1].text
                # 车主评价
                ownerevaluate = four_div[2].text
                # 价格
                price = four_div[3].text
                # #版本
                # versions=
                # #版本售价
                # versionsp=
                # ********************************************************************************************

                carname_list.append(carname)
                gearbox_list.append(gearbox)
                cartype_list.append(cartype)
                carstrength_list.append(carstrength)
                configuration_list.append(configuration)
                major_list.append(major)
                ownerevaluate_list.append(ownerevaluate)
                price_list.append(price)
                rank_list.append(rank)
                ranking_list.append(ranking)
                # versions_list.append(versions)
                # versionsp_list.append(versionsp)
                officialprice_list.append(officialprice)
                carfuelc_list.append(carfuelc)
                brand_list.append(brand)
                MIITfuelc_list.append(MIITfuelc)
                displacement_list.append(displacement)

            df=pd.DataFrame({'carname':carname_list,
                        'gearbox':gearbox_list,
                        'cartype':cartype_list,
                        'carstrength':carstrength_list,
                        'configuration':configuration_list,
                        'major':major_list,
                        'ranking':ranking_list,
                        'ownerevaluate':ownerevaluate_list,
                        'price':price_list,
                        'officialprice':officialprice_list,
                        'carfuelc':carfuelc_list,
                        'brand':brand_list,
                        'MIITfuelc':MIITfuelc_list,
                        'rank':rank_list,
                        'displacement':displacement_list})
            #print(df)
            print('正在写入第{}页'.format(n))
            n=n+1
            if n>1:
                df.to_csv(r'C:\Users\Sbaix\Desktop\太平洋汽车网数据.csv', header=None, index=False, mode='a',encoding='utf-8-sig')
            else:
                df.to_csv(r'C:\Users\Sbaix\Desktop\太平洋汽车网数据.csv', index=False, mode='a', encoding='utf-8-sig')


if __name__ == '__main__':
    url='https://price.pcauto.com.cn/top/oil/s1-t2.html'
    x=TaiPingYange(url).car_info()

