# -*- coding: utf-8 -*-
# @Time: 2018/11/30 16:00
# @File: 拉钩.py

import random
import re

import pandas as pd
import requests


class LaGor:
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    headers = {
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&city={}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.67 Safari/537.36',
    }

    def __init__(self, pg, kd, city=None):

        self.city = city
        self.pg = pg
        self.kd = kd
        self.data = dict(first='true', pn=self.pg, kd=self.kd)
        self.s = requests.Session()
        self.num = 1
        self.proxy_list = self.test_proxy()
        print(self.proxy_list)
        print('代理请求完成！')
        self.get_json = self.get_json()
        print('数据请求完成')

    def get_json(self):
        if self.city is None:
            pass
        else:
            self.url = self.url + '&city={}'.format(self.city)
            # self.url = self.url + '&city={}'.format(urllib.parse.quote(self.city))
        while True:
            i = random.randint(0, 1)
            print({self.proxy_list[1][i]: self.proxy_list[0][i]})
            try:
                res_text = self.s.post(self.url,
                                       headers=self.headers,
                                       data=self.data,
                                       proxies={
                                           self.proxy_list[1][i]: self.proxy_list[1][i] + '://' + self.proxy_list[0][
                                               i]})
                print('拉勾网第{}请求数据'.format(self.num))
                break
            except Exception:
                self.num += 1
                i = random.randint(0, 99)
                res_text = self.s.post(self.url,
                                       headers=self.headers,
                                       data=self.data,
                                       proxies={self.proxy_list[1][i]: self.proxy_list[0][i]})
                print('拉勾网第{}请求数据'.format(self.num))
                if Exception:
                    continue
                else:
                    break
        res_text.encoding = 'utf-8'
        json_info = res_text.json()
        return json_info['content']['positionResult']['result']

    def data_set(self):
        set_all = []
        for i in self.get_json:
            info = []
            info.append(i['city'])  # 城市
            info.append(i['companyFullName'])  # 公司名
            info.append(i['positionName'])  # 职位名称
            info.append(i['workYear'])  # 工作经验
            info.append(i['salary'])  # 薪资待遇
            info.append(i['education'])  # 学历要求
            info.append(i['companyLabelList'])  # 公司福利
            info.append(i['firstType'])  # 技能类型
            info.append(i['thirdType'])  # 技能类
            info.append(i['positionLables'])  # 职位标记
            info.append(i['skillLables'])  # 技能标记
            info.append(i['companySize'])  # 公司规模
            info.append(i['industryField'])  # 公司领域
            info.append(i['positionAdvantage'])  # 公司优势
            info.append(i['district'])  # 所在地区
            info.append(i['companyShortName'])  # 公司简称
            info.append(i['companyId'])  # 公司id
            info.append(i['positionId'])  # 职位id
            set_all.append(info)
        return set_all

    def save_csv(self):
        columns = ['城市', '公司名', '职位名称', '工作经验', '薪资待遇', '学历要求', '公司福利',
                   '技能类型', '技能类', '职位标记', '技能标记', '公司规模', '公司领域', '公司优势',
                   '所在地区', '公司简称', '公司id', '职位id']
        df = pd.DataFrame(self.data_set(), columns=columns)
        try:
            pd.read_csv(r'C:\Users\48170\Desktop\拉钩网.csv')
            df.to_csv(r'C:\Users\48170\Desktop\拉钩网.csv', index=False)
        except FileNotFoundError:
            df.to_csv(r'C:\Users\48170\Desktop\拉钩网.csv', index=False, mode='a')


# x = LaGor(1, 'Python', )


class IP_Proxy:
    ip_url = 'http://www.xicidaili.com/nn/'
    get_ip_re = '(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)'
    ip_port_re = '<td>([0-9]|[1-9]\d{1,3}|[1-6]\d{4}|6[0-6]{2}[0-3][0-9])</td>'
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
    headers = {
        'Host': 'www.xicidaili.com',
        'Referer': 'http: // www.xicidaili.com / nn /',
        'User-Agent': random.choice(browser),
    }

    def __init__(self):
        pass

    def get_proxy(self):
        res = requests.get(self.ip_url, headers=self.headers)
        res.encoding = 'utf-8'
        if res.status_code is 200:
            res_text = res.content
            ip = re.findall(self.get_ip_re, str(res_text))
            ip_port = re.findall(self.ip_port_re, str(res_text))
            ip_type = [i.replace('<td>', '').replace('</td>', '') for i in
                       re.findall('<td>[A-Z]+</td>', str(res_text))]
            proxy_list = []
            for i in range(len(ip)):
                y = ''
                for x in range(4):
                    y = y + '.' + ip[i][x]
                y = y + ':' + ip_port[i]
                proxy_list.append(y[1:])
            proxy = []
            for i in range(100):
                proxy.append([ip_type[i], proxy_list[i]])
            return proxy
        else:
            return

    def save_csv(self):
        columns = ['Host', 'ip']
        print(self.get_proxy())
        df = pd.DataFrame(self.get_proxy(), columns=columns)
        df.to_csv(r'C:\Users\48170\Desktop\XC_IP.csv')
        return True

    def test_proxy(self):
        proxy = pd.read_csv(r'C:\Users\48170\Desktop\XC_IP.csv')
        proxy.Host = proxy.Host.str.lower()
        url = 'http://2018.ip138.com/ic.asp'
        print('代理测试开始')
        print('测试链接：http://2018.ip138.com/ic.asp')
        for i in range(100):
            header = {}
            header['User-Agent'] = random.choice(self.browser)
            proxies = {proxy.Host[i]: proxy.Host[i] + '://' + proxy.ip[i]}
            try_ip = proxy.ip[i].split(':')[0]
            try:
                r = requests.get(url, headers=header, proxies=proxies,timeout = 50)
                if r.status_code is 200:
                    r.encoding = 'gbk'
                    result = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', r.text)
                    result = result.group()
                    if result[:9] == try_ip[:9]:
                        print('%s:%s 测试通过' % (proxy.Host[i] + '://', proxy.ip[i]))
                        continue
                    else:
                        print('%s:%s 携带代理失败,使用了本地IP' % (proxy.Host[i] + '://', proxy.ip[i]))
                        continue
                else:
                    print('%s:%s 访问失败' % (proxy.Host[i] + '://', proxy.ip[i]))
                    continue
            except:
                print('{}://{}经测试不可用'.format(proxy.Host[i], proxy.ip[i]))
                continue
        print('测试完成')


x = IP_Proxy()
#x.get_proxy()
#x.save_csv()
x.test_proxy()
