# -*- coding: utf-8 -*-
"""
   File Name：     jdspider
   Product:        PyCharm
   Project:    python4
   File:       jdspider.py
   Author :       ZXR
   date：          2018/12/14
   time:           11:23
"""
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import threading
import time

class pcautospider:
    header = {
        'Host': 'price.pcauto.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}

    def __init__(self):
        pass

    def get_url_list(self,
                     start_num = 2,
                     end_num = 20,
                     missing_num = 12,
                     url1 = 'https://price.pcauto.com.cn/top/oil/s1-t{}.html',
                     url2 = 'https://price.pcauto.com.cn/top/oil/s1-t{}-p{}.html',
                     encoding='gb2312'):
        url_list = []
        print('准备开始循环')
        for num in range(start_num,end_num + 1):
            if num != missing_num:
                one_url = url1.format(num)
                res_obj = requests.get(one_url, headers=self.header)
                print('请求完链接！')
                if res_obj.status_code == 200:
                    res_obj.encoding = encoding
                    soup = BeautifulSoup(res_obj.text, 'html.parser')
                    page_next = soup.find('a', class_='next')
                    print('请求成功！')
                    if page_next != None:
                        print(1)
                        page_total = page_next.find_previous('a').text
                        for i in range(1 , int(page_total) + 1):
                            i_url = url2.format(num,i)
                            url_list.append(i_url)
                    else:
                        print(2)
                        url_list.append(one_url)
                else:
                    print('请求失败！')
                    return None
        print(url_list)
        print('URL获取完毕！')
        return url_list

    def get_source_page(self,
                   url,):
        res_obj = requests.get(url,headers = self.header)
        if res_obj.status_code == 200:
            return res_obj.text
        else:
            return None

    def get_simple_info(self,
                        page_source):
        # soup = BeautifulSoup(page_source,'html.parser')
        url = 'https://price.pcauto.com.cn{}'
        print('准备匹配正则！')
        regex = '<div class="info">.*?<p class="sname"><a href="(.*?)" target="_blank">(.*?)</a></p>.*?<p class="col col1">官方价：<em class="red">(.*?)</em></p>.*?<p class="col">车主平均油耗：<em class="red">(.*?)</em></p>.*?<p class="col col1">品牌：(.*?)</p>.*?<p class="col">工信部油耗：(.*?)</p>.*?<p class="col col1">级别：(.*?)</p>.*?<p class="col">排量：(.*?)</p>'
        info_list = re.findall(regex,page_source,re.S)
        print('匹配完成！')
        new_list = []
        for i in info_list:
            soup = BeautifulSoup(i[-1],'html.parser')
            a_list = soup.find_all('a')
            num_list = []
            for a_tag in a_list:
                a_text = a_tag.text
                num_list.append(a_text)
            # info_list[info_list.index(i)] = list(i)
            list_i = list(i)
            list_i[0] = url.format(i[0])
            list_i[-1] = num_list
            print(len(list_i))
            new_list.append(list_i)
        info_list = []
        print(new_list)
        # print(car_list)

        return new_list

    def get_detail_info(self,
                        page_source):
        soup = BeautifulSoup(page_source,'html.parser')
        car_info_list = []
        # try:
        #     carname = soup.find('div',class_='head_name').text
        # except:
        #     carname = None
        # finally:
        #     car_info_list.append(carname)

        try:
            all_p = soup.find('ul',class_='des').find_all('p')
            gearbox = all_p[2].text.strip().replace('变\u2002速\u2002箱:','').strip().split('\n')
        except:
            gearbox = None
        finally:
            car_info_list.append(gearbox)

        try:
            all_p = soup.find('ul', class_='des').find_all('p')
            cartype = all_p[3].text.strip().replace('车身类型:','').strip()
        except:
            cartype = None
        finally:
            car_info_list.append(cartype)

        try:
            ranking = soup.find('div',class_='processBar processBarBig').find_next('p',class_='tip').text.replace('\r\n','').replace('查看详情>>','')
        except:
            ranking = None
        finally:
            car_info_list.append(ranking)

        try:
            carstrength = soup.find('div',class_='processBar processBarBig').find('div',class_='processBar-txt').text.replace('\n','').replace('车实力','')
        except:
            carstrength = None
        finally:
            car_info_list.append(carstrength)

        try:
            car_info = soup.find('div', class_='processBarWrap').find_all('div', class_='processBar')
            for i in car_info:
                x = i.find('p').text
                car_info[car_info.index(i)] = x
                # car_info_list.append(x)
        except:
            car_info = [None,None,None,None]
        finally:
            car_info_list.extend(car_info)


        try:
            version_list = []
            version_price1 = soup.find('div', class_='selCar').find_next('a').text.strip().split('\n')
            version1 = version_price1[0]
            versionsp1 = version_price1[1]
            version_list.append(version1)
            version_list.append(versionsp1)
            version_price2 = soup.find('div', class_='selCar').find_next('a').find_next('a').text.strip().split('\n')
            version2 = version_price2[0]
            versionsp2 = version_price2[1]
            version_list.append(version2)
            version_list.append(versionsp2)
        except:
            version_list = [None,None,None,None]
        finally:
            car_info_list.extend(version_list)
        print(car_info_list)
        return car_info_list


    def data_csv(self,
                 data,
                 columns = ['car_url','carname','officialprice','carfuelc','brand',
                            'MIITfuelc','rank','displacement','gearbox','cartype',
                            'ranking','carstrength','configuration','major','ownerevaluate',
                            'price','versions1','versionsp1','versions2','versionsp2',
                            ],
                 ):
        df = pd.DataFrame(data,columns = columns)
        print('准备写入！')
        thread_lock.acquire()
        try:
            pd.read_csv('pcauto.csv')
        except FileNotFoundError:
            print('第一次写入')
            df.to_csv('pcauto.csv',index = False,encoding = 'utf-8')
        else:
            print('追加写入！')
            df.to_csv('pcauto.csv',index = False,header = None,encoding = 'utf-8',mode = 'a')
        thread_lock.release()


def crawl(i,info_list1,a = pcautospider()):
    page_source2 = a.get_source_page(url=i[0])
    print('正在请求链接：')
    print(i[0])
    info_list2 = a.get_detail_info(page_source=page_source2)
    info_list1[info_list1.index(i)].extend(info_list2)
    # data_list = [info_list1[info_list1.index(i)]]
    # a.data_csv(data_list)
    # print('写入完成！')
    return info_list1

# a = pcautospider()
# b = a.get_source_page(url = 'https://price.pcauto.com.cn/sg10109/')

thread_lock = threading.Lock()
thread_pool = []
a = pcautospider()
url_list = a.get_url_list()
for url in url_list:
    print('正在请求页面链接:')
    print(url)
    page_source1 = a.get_source_page(url=url)
    info_list1 = a.get_simple_info(page_source = page_source1)
    for i in info_list1:
        t = threading.Thread(target=crawl,args=(i,info_list1))
        thread_pool.append(t)
    for t in thread_pool:
        t.start()
    for t in thread_pool:
        t.join()
    a.data_csv(info_list1)
    print('写入完成！')
    # time.sleep(3)
    thread_pool = []
