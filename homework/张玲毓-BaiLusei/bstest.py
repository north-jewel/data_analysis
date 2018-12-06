from bs4 import BeautifulSoup
import bs4,requests
import pandas as pd
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# <a class="story">fsfsf</a>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# # print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
# print(soup.title.string)
# print(type(soup.title.text)) # <class 'str'>
# print(type(soup.title.string)) # <class 'bs4.element.NavigableString'>
# # print(soup.p)
# print(soup.find('p'))
# print(soup.find_all('p'))
# print(type(soup.find_all('p'))) # <class 'bs4.element.ResultSet'> ,可以近似的当成list来用
# print('*'*20)
# print(soup.find_all('p')[0])
# print(soup.findAll('p'))
# print('a标签')
#
# print(type(soup.find('p')))
# print(type(soup.find_all('p')[0]))
# print(dir(soup.find('p')))
# # print(soup.find('p').attrs)
# soup.find_all('p',class_='title')
# print('*******')
# print(soup.find_all(class_='story'))
# print(soup.find(id="link3"))
# print(type(soup.find(id="link3")))  # <class 'bs4.element.Tag'>  类似于字典
# print(soup.find(id="link3").get('hre'))
# print(soup.find(id="link3")['hre'])
# print(soup.find(id="link3"))
# str1='sss'
# print(isinstance(str1,object))
# print(isinstance(soup.find(id="link3"),dict))
# print(issubclass(bs4.element.Tag,dict))
# soup.find_all('p',class_='title')
# print(soup.select('.title'))
# print(type(soup.select('.title')))
# print(soup.select_one('.title'))
# print(type(soup.select('.story')))
# print(soup.select('.story'))
# print(type(soup.select_one('.story')))
# print(soup.select_one('#link1'))


# url = 'https://jobs.51job.com/shenzhen-ftq/108974685.html?s=01&t=0'
# res = requests.get(url)
# soup = BeautifulSoup(res.text,'html.parser')
#
# #招聘职位
# div = soup.find('h1')
# print(type(div))
# print(div.text.lstrip())
#
# #招聘职位
# # zhiwei = soup.select_one('div.cn > h1').get('title')
# # print(zhiwei)
# #公司名称
#
# #公司名称
# gongsiname =soup.select_one('a.catn').get('title')
# print(gongsiname)
#
# #薪资
# xinzi = soup.select_one('div.cn > strong').text
# print(xinzi)
#
# #地址   经验  学历   ''     发布时间
# info = soup.select_one('div.cn > p.msg.ltype').get('title')
# print(info)
#
# #福利
# fuli = []
# for i in soup.find_all('span',class_ = 'sp4'):
#     fuli.append(i.string)
# print(','.join(fuli))
#
# #职业要求
# for i in soup.select('div.tCompany_main > div > div > p'):
#     print(i.text)
#
# #公司介绍
# gongsijieshao = soup.find_all(class_ = 'tmsg inbox')[0].text.lstrip()
# print(gongsijieshao)
#
# for i in soup.find_all('p',class_ = 'at'):
#     print(i.text.strip())
# print(gongsiinfo)
# for ii in soup.select('div.tCompany_main > div:nth-child(1) > div > p'):
#     # yaoqiu.append(ii.string)
#     print(ii.string)
# print(yaoqiu)
# print(yaoqiu)
# aa = soup.find(class_ = 'tCompany_main')
# # print(aa.find('p'))
# print(aa)
# phone = soup.select_one('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(2) > h2 > span').string
# print(yaoqiu)
# class QCWY:
    # def __init__(self,charset = 'gbk'):
    #     self.charset = charset

#将每一页得链接添加到url_list列表
# def home():
#     url_list = []
#     for i in range(1,117):
#         url1 = 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python,2,{}.html?'.format(i)
#         url_list.append(url1)
#     # print(url_list)
#     return url_list
#
# # print(url_list)
# # print(len(url))
# # page = html_text.find('span',class_ = 'td')
# # # print(page)
#
# #网页源代码
# # position_name_list = []
# def html_info(url_list):
#
#         a = 57
#         for i in url_list[57:]:
#             html = requests.get(i)
#             if html.status_code == 200:
#                 html.encoding = 'gbk'
#                 html_text = BeautifulSoup(html.text, 'lxml')
#                 print('开始第{}页'.format(a))
#                     # print(html_text)
#         #         # position_name = html_text.select('#resultList > div.el > p > span > a')
#                 position_name = html_text.find_all('p',class_ = 't1')
#                 for i in position_name:
#         #             print(i.a.get('href'))
#         #             # position_name_list.append(i.a.get('href'))
#                     with open('url.txt','a+') as f:
#                         f.write(i.a.get('href'))
#                         f.write('\n\n')
#                 a += 1

# html_info(home())

# gongsiname_list = []
# zhiwei_list = []
def qcwy():
    with open('前程无忧.txt', 'r') as f:
        ff = f.readline()
        info = {}
        # for i in f.readlines():
        html_a = requests.get(ff)
        html = BeautifulSoup(html_a.text, 'lxml')

        gongsiname = html.select_one('a.catn').get('title')
        zhiwei = html.select_one('div.cn > h1').get('title')
        xinzi = html.select_one('div.cn > strong').text
        info['company_name'] = gongsiname
        info['company_position'] = zhiwei
        info['salsry'] = xinzi
        # fuli = []
        fuli = html.find_all('span', class_='sp4')
        for i in fuli:
            print(i)
            # print(','.join(fuli))
            # info['welfare'] = i.string
        # print(fuli)
        print(info)
        df = pd.DataFrame(data = info,index = [0])
        df.to_csv('qcwy.csv',encoding= 'utf_8_sig',index = None)
        # print(df)
            # zhiwei = html.select_one('div.cn > h1').get('title')
            # zhiwei_list.append(zhiwei)

qcwy()