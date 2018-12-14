# -*- coding: utf-8 -*-
# @Time: 2018/12/14 16:16
# @File: PCauto_thread.py
import requests
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd


class PCT:
    type_url = 'https://price.pcauto.com.cn/top/oil/s1-t{}.html'
    type_page_url = 'https://price.pcauto.com.cn/top/oil/s1-t{}-p{}.html'
    home_url = 'https://price.pcauto.com.cn'

    def __init__(self):
        self.type_page = np.delete(np.arange(20), 12)

    def get_url(self, arg):
        res = requests.get(arg)
        res.encoding = 'gb2312'
        doc = res.text
        soup = BeautifulSoup(doc, 'html.parser')
        return soup

    def page_dispose(self, soup):
        for i in self.type_page:
            soup = self.get_url(self.type_url.format(i))
            pc_page = soup.find('div', class_='pcauto_page').find_all('a')[-1].text
            if pc_page == '下一页':
                # print('第{}种车型 第{}页'.format(i))
                max_page = int(soup.find('div', class_='pcauto_page').find_all('a')[-2].text)
                for x in range(1, max_page + 1):
                    if x == 1:
                        self.data_set(soup)
                    else:
                        self.data_set(self.get_url(self.type_page_url.format(i, x)))
            else:
                self.data_set(soup)

    def data_set(self, soup):
        data = []
        model_list = [i.find('a').text for i in soup.find_all('p', class_='sname')]  # 车型
        data.append(model_list)
        detail_url_list = [i.find('a')['href'] for i in soup.find_all('p', class_='sname')]
        #  车辆详细链接
        all_list = soup.find_all('p', class_='col')
        g_price_list = []  # 官方价
        owner_oil_list = []  # 车主平均油耗
        brand_list = []  # 品牌
        MIIT_oil_list = []  # 工信部油耗
        cc_list = []  # 排量
        rank_list = []  # 级别
        T = 0
        for i in range(len(all_list)):
            T += 1
            if T == 1:
                g_price_list.append(all_list[i].find('em', class_='red').text)
            if T == 2:
                owner_oil_list.append(all_list[i].find('em', class_='red').text)
            if T == 3:
                brand_list.append(all_list[i].text.replace('品牌：', ''))
            if T == 4:
                MIIT_oil_list.append(all_list[i].text.replace('工信部油耗：', ''))
            if T == 5:
                cc_list.append(all_list[i].text.replace('级别：', ''))
            if T == 6:
                o = ''
                b = [j for j in all_list[i].find_all('a')]
                for t in range(len(b)):
                    o = o + b[t].text + '/'
                rank_list.append(o)
        data.append(g_price_list)
        data.append(owner_oil_list)
        data.append(brand_list)
        data.append(MIIT_oil_list)
        data.append(cc_list)
        data.append(rank_list)
        #  dealer_price_list = []  # 经销商报价
        all_arg_list = []  #
        for i in detail_url_list:  #
            arg_list = []  #
            url = self.home_url + i
            doc = requests.get(url)
            doc.encoding = 'gb2312'
            doc = doc.text
            soup = BeautifulSoup(doc, 'html.parser')
            gearbox = ''  # 变速箱
            for i in range(1, 3):
                if len(gearbox) > 1:
                    gearbox = gearbox + soup.select('#bsx_{}'.format(i))[0].text  # 变速箱
                else:
                    gearbox = gearbox + soup.select('#bsx_{}'.format(i))[0].text + '|'  # 变速箱
            arg_list.append(gearbox)
            cartype = soup.find('ul', class_='des').find_all('a')[-1].text  # 车身类型
            arg_list.append(cartype)
            ranking = soup.select('.strength > .tip ')[0].text.replace('\n', '').replace('>', '')  # 排名
            arg_list.append(ranking)
            all_message = soup.select('.processBar-txt')
            for i in range(len(all_message)):
                if i == 0:
                    carstrength = all_message[i].em.text + all_message[i].p.text  # 车实力
                    arg_list.append(carstrength)
                if i == 1:
                    configuration = all_message[i].p.text  # 配置水平
                    arg_list.append(configuration)
                if i == 2:
                    major = all_message[i].p.text  # 专业测评
                    arg_list.append(major)
                if i == 3:
                    ownerevaluate = all_message[i].p.text  # 车主评价
                    arg_list.append(ownerevaluate)
                if i == 4:
                    price = all_message[i].p.text  # 价格
                    arg_list.append(price)
                if i == 5:
                    overall = all_message[i].p.text  # 综合评分
                    arg_list.append(overall)
            all_carlye = soup.find('div', class_='selCar').find_all('em')
            all_caprice = soup.find('div', class_='selCar').find_all('i')
            if len(all_carlye) >= 2:
                versions1 = all_carlye[0].text
                versionsp1 = all_caprice[0].text
                versions2 = all_carlye[1].text
                versionsp2 = all_caprice[1].text
                arg_list.append(versions1)
                arg_list.append(versionsp1)
                arg_list.append(versions2)
                arg_list.append(versionsp2)
                all_arg_list.append(arg_list)
                continue
            if len(all_carlye) <= 1:
                versions1 = all_carlye[0].text
                versionsp1 = all_caprice[0].text
                versions2 = ''
                versionsp2 = ''
                arg_list.append(versions1)
                arg_list.append(versionsp1)
                arg_list.append(versions2)
                arg_list.append(versionsp2)
                all_arg_list.append(arg_list)
                continue
            else:
                versions1 = ''
                versionsp1 = ''
                versions2 = ''
                versionsp2 = ''
                arg_list.append(versions1)
                arg_list.append(versionsp1)
                arg_list.append(versions2)
                arg_list.append(versionsp2)
                all_arg_list.append(arg_list)
            data.append(all_arg_list)
        return data

    def save_csv(self, data):
        columns = ['carname', 'officialprice', 'carfuelc', 'brand', 'MIITfuelc',
                   'displacement', 'rank', 'gearbox', 'cartype','ranking',
                   'carstrength', 'configuration', 'major', 'ownerevaluate', 'price',
                   'overall', 'versions1', 'versionsp1', 'versions2', 'versionsp2']
        data_set = []
        for i in range(len(data[0])):
            set = []
            for x in range(len(data)):
                set.append(x[i])
            data_set.append(set)
        data_all = []
        for i in data_set:
            p = i[:-1]
            for x in i[-1]:
                p.append(x)
            data_all.append(p)
        df = pd.DataFrame(data_all, columns=columns)
        df.to_csv('PCT.csv', index=False)