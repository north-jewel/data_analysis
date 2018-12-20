# -*- coding: utf-8 -*-
"""
   File Name：     wawjpro
   Product:        PyCharm
   Project:    python4
   File:       wawjpro.py
   Author :       ZXR
   date：          2018/12/16
   time:           18:44
"""
import requests
import re
from bs4 import BeautifulSoup
import random
import time
import pandas as pd
import threading
from fake_useragent import UserAgent

# url = 'https://bj.5i5j.com/zufang/n65/?wscckey=59321b67b0834dcc_1544958969'
# url = 'https://bj.5i5j.com/zufang/n69/?wscckey=3ac998f213be8c6f_1544958995'
class wawjspider:

    # header = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
    ua = UserAgent()
    header = {
        'User-Agent':ua.random,
    }
    def __init__(self):
        # self.s = requests.Session()
        pass

    def get_url_list(self,
                     start_num = 2,
                     end_num = 80,):
        url = 'https://bj.5i5j.com/zufang/n{}'
        url_list = []
        url_list.append('https://bj.5i5j.com/zufang/')
        for i in range(start_num,end_num+1):
            url_list.append(url.format(i))

        return url_list

    def get_page_source(self,
                        url,
                        encoding = 'UTF-8'):
        s = requests.Session()
        headers = {
            'User-Agent':self.ua.random,
        }
        # headers = self.header
        print(headers)

        time.sleep(random.choice([2, 2.5, 2.8, 2.2, 2.5, 1.9, 1.75, 1.83, 1.98, 2.68, 3.0, 3.3, 3.6]))

        res_obj = s.get(url,headers = headers)
        if res_obj.status_code == 200:
            res_obj.encoding = encoding
            print(res_obj.text)
            regex = '<script>window.location.href=(.*?);</script>'
            try:
                new_url = re.findall(regex,res_obj.text)[0]
                new_url = eval(new_url)
                # headers = self.header
                # print(headers)
                new_obj = s.get(new_url,headers = headers)
                if new_obj.status_code == 200:
                    new_obj.encoding = encoding
                    return new_obj.text
                else:
                    print('2,新链接请求失败！')
                    return None
            except IndexError:
                return res_obj.text
        else:
            print('1,原链接请求失败！')
            return None

    def get_all_url(self,
                    page_source,
                    url):
        try:
            soup = BeautifulSoup(page_source,'html.parser')
        except TypeError:
            time.sleep(random.choice([2, 2.5, 2.8, 1.2, 2.3, 1.9, 1.75, 1.83, 1.98, 2.68, 3.0, 3.3, 3.6]))
            page_source = self.get_page_source(url = url,)
            try:
                soup = BeautifulSoup(page_source,'html.parser')
            except TypeError:
                time.sleep(random.choice([2, 2.5, 2.8, 1.2, 2.3, 1.9, 1.75, 1.83, 1.98, 2.68, 3.0, 3.3, 3.6]))
                page_source = self.get_page_source(url=url,)
                try:
                    soup = BeautifulSoup(page_source, 'html.parser')
                except TypeError:
                    url_list = []
                    return url_list
                else:
                    url_list = self.soup_all_url(soup=soup)
                    return url_list
            else:
                url_list = self.soup_all_url(soup=soup)
                return url_list
        else:
            url_list = self.soup_all_url(soup = soup)
            return url_list


    def soup_all_url(self,
                     soup):
        all_tag = soup.find_all('h3', class_='listTit')
        url_list = []
        url = 'https://bj.5i5j.com{}'
        for i in all_tag:
            i_list = []
            i_a_href = url.format(i.find('a').get('href'))
            i_a_text = i.find('a').text
            i_list.append(i_a_href)
            i_list.append(i_a_text)
            url_list.append(i_list)

        print(url_list)
        return url_list

    def get_detail_info(self,
                        page_source,
                        url):
        # count_num = 5
        # while True:
        #     try:
        #         # count_num-=1
        #         soup = BeautifulSoup(page_source, 'html.parser')
        #     except TypeError:
        #         time.sleep(random.choice([2, 2.5, 2.8, 2.2, 2.5, 1.9, 1.75, 1.83, 1.98, 2.68, 3.0, 3.3, 3.6]))
        #         page_source = self.get_page_source(url=url, )
        #         # self.get_detail_info(page_source,url = url)
        #     else:
        #         house_info = self.soup_methods(soup=soup)
        #         return house_info

        try:
            soup = BeautifulSoup(page_source,'html.parser')
        except TypeError:
            time.sleep(random.choice([3, 3.5, 3.8, 3.2, 3.3, 3.9, 3.75, 2.83, 2.98, 2.68, 3.0, 3.3, 3.6]))
            page_source = self.get_page_source(url = url,)
            try:
                soup = BeautifulSoup(page_source,'html.parser')
            except TypeError:
                time.sleep(random.choice([3, 3.5, 3.8, 3.2, 3.3, 3.9, 3.75, 2.83, 2.98, 2.68, 3.0, 3.3, 3.6]))
                page_source = self.get_page_source(url=url, )
                try:
                    soup = BeautifulSoup(page_source, 'html.parser')
                except TypeError:
                    time.sleep(random.choice([3, 3.5, 3.8, 3.2, 3.3, 3.9, 3.75, 2.83, 2.98, 2.68, 3.0, 3.3, 3.6]))
                    page_source = self.get_page_source(url=url, )
                    try:
                        soup = BeautifulSoup(page_source, 'html.parser')
                    except TypeError:
                        house_info = [None]*19
                        return house_info
                    else:
                        house_info = self.soup_methods(soup=soup)
                        return house_info
                else:
                    house_info = self.soup_methods(soup=soup)
                    return house_info
            else:
                house_info = self.soup_methods(soup = soup)
                return house_info
        else:
            house_info = self.soup_methods(soup = soup)
            return house_info


    def soup_methods(self,
                    soup):
        house_info = []
        try:
            rent = soup.find('div', class_='jlquannei fontbaise').find('p', class_='jlinfo').text
        except:
            rent = None
        finally:
            house_info.append(rent)

        try:
            fonthongse = soup.find_all('div', class_='jlquannei fonthongse')
            housetype = fonthongse[0].find('p').text
        except:
            housetype = None
        finally:
            house_info.append(housetype)

        try:
            fonthongse = soup.find_all('div', class_='jlquannei fonthongse')
            area = fonthongse[1].find('p').text
        except:
            area = None
        finally:
            house_info.append(area)

        try:
            fonthongse = soup.find_all('div', class_='jlquannei fonthongse')
            payment = fonthongse[2].find('p').text
        except:
            payment = None
        finally:
            house_info.append(payment)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            district = zushous[0].find('a').text
        except:
            district = None
        finally:
            house_info.append(district)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            tage = zushous[1].text.replace('楼层：', '')
        except:
            tage = None
        finally:
            house_info.append(tage)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            orientation = zushous[2].text.replace('朝向：', '')
        except:
            orientation = None
        finally:
            house_info.append(orientation)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            decoration = zushous[3].text.replace('装修：', '')
        except:
            decoration = None
        finally:
            house_info.append(decoration)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            towertype = zushous[4].text.replace('楼型：', '')
        except:
            towertype = None
        finally:
            house_info.append(towertype)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            heating = zushous[5].text.replace('供暖：', '')
        except:
            heating = None
        finally:
            house_info.append(heating)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            rentway = zushous[6].text.replace('出租方式：', '')
        except:
            rentway = None
        finally:
            house_info.append(rentway)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            looktime = zushous[7].text.replace('看房时间：', '')
        except:
            looktime = None
        finally:
            house_info.append(looktime)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            tradingarea = zushous[8].text.replace('商圈：', '')
        except:
            tradingarea = None
        finally:
            house_info.append(tradingarea)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            metro = zushous[9].text.replace('地铁：', '')
        except:
            metro = None
        finally:
            house_info.append(metro)

        try:
            fysty = soup.find('ul', class_='fysty').find_all('li')
            fy_str = ''
            for i in fysty:
                fy_str += i.text + ','
        except:
            fy_str = None
        finally:
            house_info.append(fy_str)

        try:
            dk_list = soup.find_all('div', class_='dknquan fonthongse')
            last_time = dk_list[0].find('p', class_='jlinfo jtoppad').text
        except:
            last_time = None
        finally:
            house_info.append(last_time)

        try:
            dk_list = soup.find_all('div', class_='dknquan fonthongse')
            seven_days = dk_list[1].find('p', class_='jlinfo jtoppad').text
        except:
            seven_days = None
        finally:
            house_info.append(seven_days)

        try:
            dk_list = soup.find_all('div', class_='dknquan fonthongse')
            thirty_days = dk_list[2].find('p', class_='jlinfo jtoppad').text
        except:
            thirty_days = None
        finally:
            house_info.append(thirty_days)

        try:
            developers = soup.find('li', class_='w100').text.replace('开发商', '')
        except:
            developers = None
        finally:
            house_info.append(developers)

        # print(house_info)
        return house_info

    def data_csv(self,
                 data,
                 columns = ['url','houskeyword','rent','housetype','area','payment','district','tage',
                            'orientation','decoration','towertype','heating','rentway','looktime',
                            'tradingarea','metro','housingfacilities','last_time','seven_days','thirty_days',
                            'developers']):
        df = pd.DataFrame(data,columns = columns)
        print('准备写入！')
        try:
            pd.read_csv('wawj.csv')
        except FileNotFoundError:
            print('1，开始写入！')
            df.to_csv('wawj.csv',index = False,encoding = 'utf-8')
        else:
            print('2，开始写入！')
            df.to_csv('wawj.csv',index = False,header = None,encoding = 'utf-8',mode = 'a')
        print('写入完成！')

def crawl(i,a=wawjspider()):
    print('正在请求详情页面：')
    print(i[0])
    new_source = a.get_page_source(url=i[0])
    detail_info = a.get_detail_info(page_source=new_source,url=i[0])
    i.extend(detail_info)
    print('请求完毕！')
    print(i)


thread_pool = []
a = wawjspider()
url_list = a.get_url_list()
print('所有页面链接生成完毕！')
for url in url_list:
    print('正在请求：')
    print(url)
    print('请求页码全部URL')
    page_source = a.get_page_source(url=url)
    page_all_url = a.get_all_url(page_source = page_source,url = url)
    if len(page_all_url) == 0:
        continue
    for i in page_all_url:
        t = threading.Thread(target=crawl,args=(i,))
        thread_pool.append(t)
    for t in thread_pool:
        t.start()
    for t in thread_pool:
        t.join()

        # print('正在请求详情页面：')
        # print(i[0])
        # new_source = a.get_page_source(url = i[0])
        # detail_info = a.get_detail_info(page_source = new_source,url = i[0])
        # i.extend(detail_info)
        # print(i)
    # time.sleep(random.choice([2,2.5,2.8,1.2,2.3,1.9,1.75,1.83,1.98,2.68,3.0,3.3,3.6]))
    a.data_csv(page_all_url)
    print('写入完成！')
    thread_pool = []








# page_source = a.get_page_source(url = 'https://bj.5i5j.com/zufang/42119308.html')
# soup = a.get_all_url(page_source = page_source)
# soup = a.get_detail_info(page_source = page_source)

