# !usr/bin/env python
# -*- coding:utf-8 -*-
# author: 随风
# time: 2018/12/16

import requests
import re
from bs4 import BeautifulSoup
import time
import pandas as pd

class w5i5j:
    def __init__(self,num):
        self.num = num

    def request(self,url,head = None):
        res = requests.get(url,headers = head)
        res.encoding = 'utf-8'
        html = res.text
        return html

    def regex(self,html, **kwargs):
        a = []
        for x, y in kwargs.items():
            x = re.findall(y, html)
            if len(x) == 0:
                info = ''
            else:
                info = x[0]
            a.append(info)
            print(a)
        return a


    def urls(self,url):
        html = self.request(url)
        urls_regex = '<div class="listImg"><a href="(.*?)" target="_blank">'
        urls = re.findall(urls_regex, html)
        return urls


    def info(self,url):
        print(url)
        head = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'PHPSESSID=439je1e2ikqd8slqo6gbdohdkk; yfx_c_g_u_id_10000001=_ck18121519395613061131307175552; _ga=GA1.2.1700306047.1544873996; _gid=GA1.2.1490458095.1544873996; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1544871224; _Jo0OQK=3CE696C4FA0E78A1AB821594E74047A1F26CB2483CB17CC3ED3248FBDECC0737B61C98B892736C6217C6508A33D92850AED7BA9DEFB635AA740137F5497A74896B7C57212F12283777C840763663251ADEB840763663251ADEBC37B15F87E4FAC2A16B75375CFA1B530GJ1Z1YA==; domain=bj; zufang_BROWSES=42114196%2C42119308%2C42110091%2C42108981%2C42124001%2C42121020%2C42112658%2C42107935%2C42124316%2C42107853; yfx_f_l_v_t_10000001=f_t_1544873996299__r_t_1544873996299__v_t_1544885624400__r_c_0; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1544885725',
                'Host': 'bj.5i5j.com',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
        html = self.request(url,head)
        soup = BeautifulSoup(html, 'html.parser')
        houskeyword = soup.select_one('.house-tit').text
        info_4 = [i.text for i in soup.select('.jlquannei > p.jlinfo')]
        rent = info_4[0]
        housetype = info_4[1]
        area = info_4[2]
        if len(info_4) == 3:
            payment = ''
        else:
            payment = info_4[3]
        a = self.regex(html, district='<li><span>小区：</span><a href=".*?" target="_blank">(.*?)</a></li>',
                       tage='<li><span>楼层：</span>(.*?)</li>', orientation='<li><span>朝向：</span>(.*?)</li>',
                       decoration='<li><span>装修：</span>(.*?)</li>', towertype='<li><span>楼型：</span>(.*?)</li>',
                       heating='<li><span>供暖：</span>(.*?)</li>',
                       rentway='<li><span>出租方式：</span>(.*?)</li>', looktime='<li><span>看房时间：</span>(.*?)</li>',
                       tradingarea='<li><span>商圈：</span>(.*?)</li>',
                       metor='<li class="traffic"><span>地铁：</span>(.*?)</li>')
        district = a[0]
        tage = a[1]
        orientation = a[2]
        decoration = a[3]
        towertype = a[4]
        heating = a[5]
        rentway = a[6]
        looktime = a[7]
        tradingarea = a[8]
        metor = a[9]
        housingfacilities = ','.join([i.text.strip() for i in soup.select('.fysty > li')])
        record = soup.select('.daikanquan')[2].text.strip().split('\n')[0]
        developers_regex = '<li class="w100"><span>开发商</span>(.*?)</li>'
        developers = re.findall(developers_regex, html)
        if len(developers) == 0:
            developers = ''
        else:
            pass
        return (houskeyword,rent,housetype,area,payment,district,tage,orientation,decoration,towertype,heating,rentway,looktime,tradingarea,metor,housingfacilities,record,developers)


    def a(self):
        info_zong = []
        for i in range(self.num):
            url = 'https://bj.5i5j.com/zufang/n{}'.format(i + 1)
            urls = self.urls(url)
            print(urls)
            for i in urls:
                time.sleep(2)
                try:
                    url_dan = 'https://bj.5i5j.com' + i
                    info = self.info(url_dan)
                except:
                    pass
                else:
                    info_zong.append(info)
        columns = ['房源关键字', '租金', '户型','面积(平米)', '支付方式', '小区','楼层', '朝向', '装修', '楼型', '供暖', '出租方式', '看房时间', '商圈', '地铁',
                   '房源配套设施', '看房记录', '开发商']
        df = pd.DataFrame(info_zong, columns=columns)
        df.to_csv(r'C:\Users\15730\Desktop\info.csv', encoding='utf_8_sig')
if __name__ == '__main__':
    w5i5j(1).a()
