import requests,re,bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
import random

headers = {'Cookie': 'PHPSESSID=e04dcl1rkvcjdvjmvtq53hp9ad; _ga=GA1.2.1302851638.1544936116; _gid=GA1.2.746896476.1544936116; yfx_c_g_u_id_10000001=_ck18121612551515807320655551232; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1544936117; domain=bj; _Jo0OQK=75E4B432703F0DFD4E952568E48E7B67B1F63ABBB34359B7DF2C134EAA6AFD8C949A69DE239B77CFA2F5ECD8F821838AB994A7CF6727E5FB776E68808FC26C54DF3C57212F12283777C840763663251ADEB840763663251ADEB42E0F544D03120245FAFDAF9B9801008GJ1Z1Ig==; zufang_BROWSES=42119308; yfx_f_l_v_t_10000001=f_t_1544936115573__r_t_1544936115573__v_t_1544938642820__r_c_0; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1544938643',
            'Host': 'bj.5i5j.com',
            'Referer': 'https://bj.5i5j.com/zufang/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
            }

def soup_all_url(self,soup):
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

def wawj(num):
    a= 0
    url_info_list = []
    b = True
    for i in range(1,num+1):
        a += 1
        url = 'https://bj.5i5j.com/zufang/n{}/?wscckey=b7c59fd3ebbd0b43_1544939300'.format(i)
        res = requests.get(url,headers = headers)
        res_text = BeautifulSoup(res.text,'lxml')
        print(res.text)
        url_list = res_text.find_all('h3',class_ = 'listTit')
        for n in url_list:
            url_info = n.a.attrs['href']
            url_info_list.append(url_info)
        df = pd.DataFrame(url_info_list,columns=['url'])
        if a == 2:
            b = False
        df.to_csv('urlinfo.csv',encoding='utf_8_sig',index=False,mode='a',header=b)
        # print(len(url_info_list))
        url_info_list = []

        print('第{}页完'.format(a))
        time.sleep(10)
    return url_info_list
# wawj(1)



def data_info():
    headers = {'Cookie': 'PHPSESSID=e04dcl1rkvcjdvjmvtq53hp9ad; _ga=GA1.2.1302851638.1544936116; _gid=GA1.2.746896476.1544936116; yfx_c_g_u_id_10000001=_ck18121612551515807320655551232; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1544936117; _Jo0OQK=75E4B432703F0DFD4E952568E48E7B67B1F63ABBB34359B7DF2C134EAA6AFD8C949A69DE239B77CFA2F5ECD8F821838AB994A7CF6727E5FB776E68808FC26C54DF3C57212F12283777C840763663251ADEB840763663251ADEB42E0F544D03120245FAFDAF9B9801008GJ1Z1Ig==; domain=bj; yfx_f_l_v_t_10000001=f_t_1544936115573__r_t_1544936115573__v_t_1544961478553__r_c_0; zufang_BROWSES=42119308%2C42105938%2C42111676%2C42123365%2C42115004%2C42119335%2C42118108%2C42120898; _gat=1; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1544962747',
                'Host': 'bj.5i5j.com',
                'Referer': 'https://bj.5i5j.com/zufang/42119308.html',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    a = 0
    b = True
    url_info = pd.read_csv('url.csv')
    data_dict = {}
    for i in url_info.url:
        print(i)
        a += 1
        print('开始第{}条'.format(a))
        url ='https://bj.5i5j.com'+i
        detail_res = requests.get(url,headers = headers).text
        detail_text = BeautifulSoup(detail_res,'lxml')


        #房源关键字
        houskeyword_re = detail_text.find('h1',class_ = 'house-tit').text
        # print(houskeyword_re)

        #租金
        rent_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div.jlyou.fl > div > p.jlinfo').text
        # print(rent_re)

        #面积
        area_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div:nth-of-type(3) > div > p.jlinfo').text
        # print(area_re)

        #户型
        housetype_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div:nth-of-type(2) > div > p.jlinfo.font18').text
        # print(housetype_re)

        #支付方式
        payment_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div:nth-of-type(4) > div > p.jlinfo.font18').text
        # print(payment_re)

        #小区
        # district_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-of-type(1) > a').text
        # print(district_re)

        #楼层
        # tage_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-of-type(2)').text.replace('楼层：','')
        # print(tage_re)

        #朝向
        # orientation_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-of-type(3)').text.replace('朝向：','')
        # print(orientation_re)

        #装修
        # decoration_re= detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-of-type(4)').text.replace('装修：','')
        # print(decoration_re)

        #楼型
        # towertype_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-of-type(5)').text.replace('楼型：','')
        # print(towertype_re)

        #供暖
        # heating_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-of-type(6)').text.replace('供暖：','')
        # print(heating_re)

        #出租方式
        # rentway_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-of-type(7)').text
        # print(rent_re)

        # 看房时间
        # looktime_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-of-type(8)').text.replace('看房时间：','')
        # print(looktime_re)

        #商圈
        # tradingarea_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-of-type(9)').text.replace('商圈：','')
        # print(tradingarea_re)

        #地铁
        # metor_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.zushous > ul > li.traffic').text.replace('地铁：','')
        # print(metor_re)
        # try:
        #     house_info1 = detail_text.find('div', class_="zushous")
        #     li_info = house_info1.find_all('li')
        #     district_re = li_info[0].text.replace('小区：','')
        #     tage_re = li_info[1].text.replace('楼层：','')
        #     orientation_re = li_info[2].text.replace('朝向：','')
        #     decoration_re = li_info[3].text.replace('装修：','')
        #     towertype_re = li_info[4].text.replace('楼型：','')
        #     heating_re = li_info[5].text.replace('供暖：','')
        #     rentway_re = li_info[6].text.replace('出租方式：','')
        #     print(rentway_re)
        #     looktime_re = li_info[7].text.replace('看房时间：','')
        #     tradingarea_re = li_info[8].text.replace('商圈：','')
        #     metor_re = li_info[9].text.replace('地铁：','')
        # except IndexError:
        #     metor_re = np.nan
        #     heating_re = np.nan
        li_info = detail_text.find('div', class_="zushous").find_all('li')
        house_dic = {'小区': 'district', '楼层': 'tage', '朝向': 'orientation', '装修': 'decoration', '楼型': 'towertype',
                     '供暖': 'heating', '出租方式': 'rentway', '看房时间': 'looktime', '商圈': 'tradingarea', '地铁': 'metor'}
        tag_house_dic = {'district': '', 'tage': '', 'orientation': '', 'decoration': '', 'towertype': '',
                         'heating': '', 'rentway': '', 'looktime': '', 'tradingarea': '', 'metor': ''}
        for tag in li_info:
            tag_info, tag_ = tag.text.split('：')[0], tag.text.split('：')[1]
            if tag_info in house_dic.keys():
                tag_house_dic[house_dic[tag_info]] = tag_
        data_dict['houskeyword'] = houskeyword_re
        data_dict['rent'] = rent_re
        data_dict['housetype'] = housetype_re
        data_dict['area'] = area_re
        data_dict['payment'] = payment_re
        # data_dict['district'] = district_re
        # data_dict['tage'] = tage_re
        # data_dict['orientation'] = orientation_re
        # data_dict['decoration'] = decoration_re
        # data_dict['towertype'] = towertype_re
        # data_dict['heating'] = heating_re
        # data_dict['rentway'] = rentway_re
        # data_dict['looktime'] = looktime_re
        # data_dict['tradingarea'] = tradingarea_re
        # data_dict['metor'] = metor_re
        print(tag_house_dic)
        # print(data_dict)
        # df = pd.DataFrame(data_dict,columns=data_dict.keys(),index= [0])
        # if a == 2:
        #     b = False
        # df.to_csv('wawj.csv',index=False,encoding='utf_8_sig',mode='a',header= b)
        time.sleep(random.randrange(10))
data_info()
# wawj(10)


