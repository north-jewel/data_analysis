# -*- coding: utf-8 -*-
# @Time: 2018/12/4 20:51
# @File: 代理测试.py

import random
import re

import pandas as pd
import requests
global browser
browser = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 "
    "Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 "
    "Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

class IP_Proxy:
    ip_url = 'http://www.xicidaili.com/nn/{}'
    get_ip_re = '(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)'
    ip_port_re = '<td>([0-9]|[1-9]\d{1,3}|[1-6]\d{4}|6[0-6]{2}[0-3][0-9])</td>'
    headers = {
        'Host': 'www.xicidaili.com',
        'Referer': 'http: // www.xicidaili.com / nn /',
        'User-Agent': random.choice(browser),
    }

    def get_proxy(self, pg=None):

        if pg is None:
            res = requests.get(self.ip_url, headers=self.headers)
        else:
            res = requests.get(self.ip_url.format(str(pg)), headers=self.headers)
        res.encoding = 'utf-8'
        if res.status_code is 200:
            res_text = res.content
            ip = re.findall(self.get_ip_re, str(res_text))
            ip_port = re.findall(self.ip_port_re, str(res_text))
            # ip_type = [i.replace('<td>', '').replace('</td>', '') for i in
            #            re.findall('<td>[A-Z]+</td>', str(res_text))]
            proxy_list = []
            for i in range(len(ip)):
                y = ''
                for x in range(4):
                    y = y + '.' + ip[i][x]
                proxy_list.append([y[1:], ip_port[i]])
            return proxy_list
        else:
            return

    def save_csv(self, pg=None):
        columns = ['ip', 'port']
        if pg is None:
            df = pd.DataFrame(self.get_proxy(), columns=columns)
        else:
            df = pd.DataFrame(self.get_proxy(pg), columns=columns)
        try:
            pd.read_csv(r'C:\Users\48170\Desktop\XC_IP.csv')
            df.to_csv(r'C:\Users\48170\Desktop\XC_IP.csv', index=False, header=False, mode='a')
        except FileNotFoundError:
            df.to_csv(r'C:\Users\48170\Desktop\XC_IP.csv', index=False)
        print('代理保存完成')
        return True

    def test_proxy(self):
        proxy = pd.read_csv(r'C:\Users\48170\Desktop\XC_IP.csv')
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        print('代理测试开始')
        print('测试链接：https://www.lagou.com/')
        proxy_list = []
        columns = ['ip', 'port']
        for i in range(len(proxy)):
            header = {
                      'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
                      'User-Agent': random.choice(browser),
                      }
            proxies = {'http':  proxy.ip[i] + ':' + str(proxy.port[i]),
                       'https': proxy.ip[i] + ':' + str(proxy.port[i])}
            try:
                r = requests.get(url, headers=header, proxies=proxies, timeout=3)
                print(r.status_code)
                print(r.text)
                if r.status_code is 200:
                    # r.encoding = 'gbk'
                    # result = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', r.text)
                    # result = result.group()
                    #if result[:9] == try_ip[:9]:
                    print('%s:%s 测试通过' % (proxy.ip[i], str(proxy.port[i])))
                    proxy_list.append([proxy.ip[i], proxy.port[i]])
                    continue
                else:
                    print('%s:%s 携带代理失败,使用了本地IP' % (proxy.ip[i], str(proxy.port[i])))
                    continue
                # else:
                #     print('%s:%s 访问失败' % (proxy.ip[i], str(proxy.port[i])))
                #     continue
            except:
                print('{}:{}经测试不可用'.format(proxy.ip[i], proxy.port[i]))
                continue
        print('测试完成')
        df = pd.DataFrame(proxy_list, columns=columns)
        try:
            pd.read_csv(r'C:\Users\48170\Desktop\XC_IP_USABLE.csv')
            df.to_csv(r'C:\Users\48170\Desktop\XC_IP_USABLE.csv', mode='a', header=False, index=False)
        except FileNotFoundError:
            df.to_csv(r'C:\Users\48170\Desktop\XC_IP_USABLE.csv', index=False)
        return True

x = IP_Proxy()
for i in range(1,5):
    if i < 2:
        x.save_csv()
    else:
        x.save_csv(i)
x.test_proxy()
