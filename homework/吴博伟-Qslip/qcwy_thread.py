# -*- coding: utf-8 -*-
# @Time: 2018/12/5 15:12
# @File: qcwy.py

import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import threading

class P51job:
    first_url = "https://search.51job.com/list/010000,000000,0000,00,9,99,Python,2,{}.html"

    def get_data(self, url):
        res = requests.get(url)
        res.encoding = 'gb2312'
        res_text = res.text
        return res_text

    def data_clear(self, pg=None):
        link_list = self.pg_link(pg)
        data_list = []
        for i in link_list:
            print(i)
            data=[]
            soup = BeautifulSoup(self.get_data(i), 'html.parser')
            # 工作名称
            try:
                job_name = soup.find('h1')['title']
                data.append(job_name)
            except:
                data.append(None)
            # 公司名称
            try:
                cpy_name = soup.select_one('.cname > a')['title']
                data.append(cpy_name)
            except:
                data.append(None)

            try:
                place_exp_edu_num_tm = soup.find(class_='msg ltype')['title'].replace('\xa0', '').split('|')
                if len(place_exp_edu_num_tm) >= 5:
                    place = place_exp_edu_num_tm[0]  # 工作地址
                    data.append(place)
                    exp = place_exp_edu_num_tm[1]  # 工作经验
                    data.append(exp)
                    edu = place_exp_edu_num_tm[2]  # 学历
                    data.append(edu)
                    num = place_exp_edu_num_tm[3]  # 招聘人数
                    data.append(num)
                    tm = place_exp_edu_num_tm[4]  # 招聘发布时间
                    data.append(tm)
                if len(place_exp_edu_num_tm) == 4:
                    place = place_exp_edu_num_tm[0]  # 工作地址
                    data.append(place)
                    exp = place_exp_edu_num_tm[1]  # 工作经验
                    data.append(exp)
                    data.append(None)  # 学历
                    num = place_exp_edu_num_tm[2]  # 招聘人数
                    data.append(num)
                    tm = place_exp_edu_num_tm[3]  # 招聘发布时间
                    data.append(tm)
                else:
                    pass
            except:
                data.append(None)
                data.append(None)
                data.append(None)
                data.append(None)
                data.append(None)
            # 公司信息
            try:
                scale = [z['title'] for z in soup.find(class_='com_tag').find_all('p', class_='at')]
                data.append(scale)
            except:
                data.append(None)
            # 薪资
            try:
                wage = soup.find(class_='cn').find('strong').text
                data.append(wage)
            except:
                data.append(None)
            # 福利
            try:
                welfare = [i.text for i in soup.find_all(class_='sp4')]
                data.append(welfare)
            except:
                data.append(None)
            # 职位信息
            try:
                position_data = soup.find(class_='bmsg job_msg inbox').text.replace('\n', '').replace('\t', '').replace('微信分享','')
                data.append([position_data])
            except:
                data.append(None)
            # 上班地址
            try:
                contact = soup.find(class_='bmsg inbox').find('p').text.replace('\n', '').replace('\t', '')
                data.append(contact)
            except:
                data.append(None)

            data_list.append(data)
            time.sleep(0.5)
        self.save_data(data_list)
        return True

    def save_data(self, data):

        columns = ['工作名称', '公司名称', '工作地址', '工作经验', '学历', '招聘人数',
                   '招聘发布时间', '公司信息', '薪资', '福利', '职位信息', '上班地址']
        df = pd.DataFrame(data, columns=columns)
        print(df)
        try:
            pd.read_csv(r'C:\Users\48170\Desktop\QCWY.csv', encoding='utf-8')
            df.to_csv(r'C:\Users\48170\Desktop\QCWY.csv', encoding='utf-8', index=False, mode='a')
        except FileNotFoundError:
            df.to_csv(r'C:\Users\48170\Desktop\QCWY.csv', encoding='utf-8', index=False)
        return True

    def pg_link(self, pg=None):
        if pg is None:
            pg = 1
            first_url = self.first_url.format('1')
        else:
            first_url = self.first_url.format(str(pg))
        print('正在爬取第{}页数据。。。'.format(pg))
        res = requests.get(first_url)
        res.encoding = 'gbk'
        soup = BeautifulSoup(res.text, 'html.parser')
        link_list = [i.find('a')['href'] for i in soup.find_all('p',class_='t1')]
        return link_list

    def thread(self, td = 10):
        while True:
            pool = []
            for i in range(td-10,td):
                if i == 0:
                    pass
                else:
                    print('线程{}启动'.format(str(i)))
                    pool.append(threading.Thread(target=self.data_clear, args=(str(i),)))
            for i in pool:
                i.start()
            for i in pool:
                i.join()
            td += 10
            if td == 116:
                break
            time.sleep(10)

x = P51job()
x.thread()


