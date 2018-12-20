# -*- coding: utf-8 -*-
"""
   File Name：     manageip
   Product:        PyCharm
   Project:    python4
   File:       manageip.py
   Author :       ZXR
   date：          2018/12/4
   time:           14:53
"""
import requests
import re
import random
import time
import threading
from bs4 import BeautifulSoup
import pandas as pd

class disposeip:
    agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    ]

    # def __init(self,
    #            name,
    #            page_num,
    #            scraw_url="http://www.xicidaili.com/nn/",
    #            encoding='utf-8',
    #            regex='<td class="country">.*?alt="Cn" />.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',
    #            ):
    #     self.name=name
    #     self.page_num = page_num
    #     self.scraw_url = scraw_url
    #     self.encoding = encoding
    #     self.regex = regex
        #self.thread_pool = []

    def get_random_header(self):
        headers = {'User-Agent': random.choice(self.agent_list),
                   'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   'Accept-Encoding': 'gzip'}
        return headers

    def get_ips(self, pn):
        print('正在获取代理列表...')
        url = 'https://www.kuaidaili.com/free/inha/{}/'.format(pn)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        html = requests.get(url=url, headers=self.get_random_header()).text
        soup = BeautifulSoup(html, 'lxml')
        ips = soup.find(id='list').find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append((tds[0].text, tds[1].text))
        print('代理列表抓取成功！')
        test_url = 'http://2018.ip138.com/ic.asp'
        return ip_list

    def scraw_proxies(self,
                      page_num,
                      scraw_url="http://www.xicidaili.com/nn/",
                      encoding = 'utf-8',
                      regex = '<td class="country">.*?alt="Cn" />.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',
                      filename = 'xiciip.csv',
                      ):
        # page_num = self.page_num
        # scraw_url = self.scraw_url
        # encoding = self.encoding
        # regex = self.regex
        scraw_ip = list()
        available_ip = list()
        for page in range(1, page_num+1):
            print("抓取第%d页代理IP" % page)
            url = scraw_url + str(page)
            print(url)
            r = requests.get(url, headers= self.get_random_header())
            r.encoding = encoding
            pattern = re.compile(regex, re.S)
            scraw_ip = re.findall(pattern,r.text)
            print(scraw_ip)
            for ip in scraw_ip:
                if (self.test_ip(ip) == True):
                    print('%s:%s通过测试，添加进可用代理列表' % (ip[0], ip[1]))
                    available_ip.append([ip[0],ip[1]])
                else:
                    pass
            print("代理爬虫暂停10s")
            time.sleep(10)
            print("爬虫重启")
        print('抓取结束')
        self.to_datacsv(data=available_ip,filename=filename)
        return available_ip

    def test_ip(self, ip, test_url='http://2018.ip138.com/ic.asp', time_out=3):
        proxies = {'http': ip[0] + ':' + ip[1],
                   'https':ip[0] + ':' + ip[1]}
        try_ip = ip[0]
        print(try_ip)
        try:
            r = requests.get(test_url, headers=self.get_random_header(), proxies=proxies, timeout=time_out)
            if r.status_code == 200:
                r.encoding = 'gbk'
                result = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', r.text)
                result = result.group()
                if result[:9] == try_ip[:9]:
                    print(r.text)
                    print('测试通过')
                    return True
                else:
                    print('%s:%s 携带代理失败,使用了本地IP' % (ip[0], ip[1]))
                    return False
            else:
                print('%s:%s 请求码不是200' % (ip[0], ip[1]))
                return False
        except:
            print('%s:%s 请求过程错误' % (ip[0], ip[1]))
            return False

    def to_datacsv(self,
                   data,
                   columns = ['ip','port'],
                   filename = 'xiciip.csv'):
        df = pd.DataFrame(data=data, columns=columns)
        try:
            pd.read_csv(filename)
            print(1)
        except:
            print(2)
            df.to_csv(filename, index=False, encoding='utf-8-sig')
        else:
            df.to_csv(filename, mode='a', index=False, header=False, encoding='utf-8-sig')
        print('保存完成！')
        return '保存完成！'


if __name__=="__main__":
    # dis_obj = disposeip()
    # regex = '<tr>.*?<td data-title="IP">(.*?)</td>.*?<td data-title="PORT">(.*?)</td>'
    # available_ip=dis_obj.scraw_proxies(3,
    #                                    scraw_url = 'https://www.kuaidaili.com/free/inha/',
    #                                    regex = regex,
    #                                    )
    # print(available_ip)
    # dis_obj.to_datacsv(available_ip)
    thread_pool = []
    dis_obj = disposeip()
    thread1 = threading.Thread(target=dis_obj.scraw_proxies,args=(2,))
    thread2 = threading.Thread(target=dis_obj.scraw_proxies,args=(4,'https://www.kuaidaili.com/free/inha/','utf-8',
                                                                  '<tr>.*?<td data-title="IP">(.*?)</td>.*?<td data-title="PORT">(.*?)</td>',
                                                                  'kuaidaili.csv'))
    thread_pool.append(thread1)
    thread_pool.append(thread2)
    for i in thread_pool:
        i.start()
    for t in thread_pool:
        t.join()


