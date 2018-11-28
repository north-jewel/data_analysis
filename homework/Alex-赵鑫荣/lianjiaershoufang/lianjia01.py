# -*- coding: utf-8 -*-
"""
   File Name：     lianjia01
   Product:        PyCharm
   Project:    python4
   File:       lianjia01.py
   Author :       ZXR
   date：          2018/11/25
   time:           9:43
"""
import requests
import re
from bs4 import BeautifulSoup
import time
import pandas as pd

class lianjiabj:

    def get_allurl(self,start_num = 1,end_num=10,num = 20):
        '''
        生成输入的数字个数的所有页面的url
        :param num:开始页面和结束页面  或者  指定结束页面
        :return: 一个所有页面url的列表
        '''
        url = 'https://bj.lianjia.com/ershoufang/pg{}/'
        allurl_list = []
        if num != 20:
            for i in range(1,num+1):
                new_url = url.format(i)
                allurl_list.append(new_url)
            return allurl_list
        else:
            for i in range(start_num,end_num+1):
                new_url = url.format(i)
                allurl_list.append(new_url)
            return allurl_list

    def get_detailurl(self,pgurl):
        '''
        传入一个具体页码的url，获取相应的标题和url
        :param pgurl: 一个有具体页码的url
        :return: 返回一个键是标题，值是url的字典
        '''
        res_obj = requests.get(pgurl)
        res_obj.encoding = 'utf-8'
        if res_obj.status_code == 200:
            info_dict = {}
            detailurl_regex = '<div class="title"><a class="" href="(.*?)" target="_blank" data-log_index=".*?"  data-el="ershoufang" data-housecode=".*?" data-is_focus=".*?" data-sl="">.*?</a>'
            title_regex = '<div class="title"><a class="" href=".*?" target="_blank" data-log_index=".*?"  data-el="ershoufang" data-housecode=".*?" data-is_focus=".*?" data-sl="">(.*?)</a>'
            detailurl_info = re.findall(detailurl_regex,res_obj.text)
            title_info = re.findall(title_regex,res_obj.text)
            for i in range(len(title_info)):
                info_dict[title_info[i]] = detailurl_info[i]
            #print(info_dict)
            return info_dict
        else:
            return None


    def get_detailinfo(self,detail_url):
        '''
        输入详细页面的url，获取页面的响应内容，如标题、房屋面积、楼型等
        :param detail_url: 详细页面的url
        :return: 返回详细页面需要的内容
        '''
        res_obj = requests.get(detail_url)
        res_obj.encoding = 'utf-8'
        if res_obj.status_code == 200:
            detail_list = []
            soup = BeautifulSoup(res_obj.text,'lxml')
            #添加标题
            detail_list.append(soup.select('.main')[0].text)
            #添加面积
            detail_list.append(float(soup.select('.mainInfo')[2].text.replace('平米','')))
            #楼型
            loux = soup.select('#introduction > div > div > div.base > div.content > ul > li:nth-of-type(6)')[0].text
            detail_list.append(loux.replace('建筑类型',''))
            #建筑年份
            jznf = soup.select('body > div.overview > div.content > div.houseInfo > div.area > div.subInfo')[0].text
            if jznf == '未知年建/暂无数据':
                jznf = '未知年建/暂无数据'
            else:
                pattern = '\d+'
                jznf = re.findall(pattern,jznf)[0]+'年'
            # leftContent > ul > li:nth-child(16) > div > div.flood > div
            detail_list.append(jznf)
            #挂牌
            detail_list.append(soup.select('#introduction > div > div > div.transaction > div.content > ul > li:nth-of-type(1) > span:nth-of-type(2)')[0].text)
            #上次交易
            detail_list.append(soup.select('#introduction > div > div > div.transaction > div.content > ul > li:nth-of-type(3) > span:nth-of-type(2)')[0].text)
            #地区
            detail_list.append(soup.select('body > div.overview > div.content > div.aroundInfo > div.areaName > span.info > a:nth-of-type(1)')[0].text)
            #区域
            detail_list.append(soup.select('body > div.overview > div.content > div.aroundInfo > div.areaName > span.info > a:nth-of-type(2)')[0].text)
            #小区
            detail_list.append(soup.select('body > div.overview > div.content > div.aroundInfo > div.communityName > a.info')[0].text)
            #单价(元)
            price = soup.select('body > div.overview > div.content > div.price > div.text > div.unitPrice > span')[0].text.replace('元/平米','')
            price = float(price)
            detail_list.append(price)
            #总价(万元)
            detail_list.append(float(soup.select('body > div.overview > div.content > div.price > span.total')[0].text))
            #户型
            house_type = soup.select('#introduction > div > div > div.base > div.content > ul > li:nth-of-type(1) > span')[0].text
            house_type = house_type.replace('房屋户型','')
            detail_list.append(soup.select('body > div.overview > div.content > div.houseInfo > div.room > div.mainInfo')[0].text)
            #楼层
            floor_info = soup.select('body > div.overview > div.content > div.houseInfo > div.room > div.subInfo')[0].text
            floor_list = floor_info.split('/')
            detail_list.append(floor_list[0])
            #总楼层
            pattern = '\d+'
            total_floor = int(re.findall(pattern,floor_list[1])[0])
            detail_list.append(total_floor)
            #关注人数
            detail_list.append(int(soup.select('#favCount')[0].text))
            #带看人数
            detail_list.append(int(soup.select('#cartCount')[0].text))
            #朝向
            detail_list.append(soup.select('body > div.overview > div.content > div.houseInfo > div.type > div.mainInfo')[0].text)
            #装修
            decoration = soup.select('#introduction > div > div > div.base > div.content > ul > li:nth-of-type(9)')[0].text
            decoration = decoration.replace('装修情况','')
            detail_list.append(decoration)
            #print(detail_list)
            return detail_list
        else:
            return None

    def to_datacsv(self,data,columns = ['标题','面积','楼型','建筑年份','挂牌时间',
                                        '上次交易','地区','区域','小区','单价','总价','户型','楼层',
                                        '总楼层','关注人数','带看','朝向','装修']):
        df = pd.DataFrame(data = data,columns = columns)
        try:
            pd.read_csv('lianjiabj.csv')
        except:
            df.to_csv('lianjiabj.csv',index = False,encoding = 'utf-8-sig')
        else:
            df.to_csv('lianjiabj.csv',mode='a',index = False,header = False,encoding = 'utf-8-sig')
        print('保存完成！')
        return '保存完成！'

ljbj_obj = lianjiabj()
allpage_url = ljbj_obj.get_allurl(start_num=1,end_num=50)
house_list = []
n=1
for i in allpage_url:
    info_dict = ljbj_obj.get_detailurl(pgurl = i)
    for key,value in info_dict.items():
        #time.sleep(2)
        print('正在爬取  {}  的  {}  信息'.format(i,key))
        detail_list = ljbj_obj.get_detailinfo(detail_url = value)
        house_list.append(detail_list)
        print('正在写入  {}  的  {}  信息'.format(i,key))
        print('写入编号为：{}'.format(n))
        ljbj_obj.to_datacsv(data=house_list)
        n+=1
        house_list = []

        #time.sleep(2)
#ljbj_obj.to_datacsv(data=house_list)



#lianjiabj().get_detail(detail_url = 'https://bj.lianjia.com/ershoufang/101103229329.html')