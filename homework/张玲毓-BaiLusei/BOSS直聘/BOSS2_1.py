import re,requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

#读取到information文件  将链接添加到一个新列表
def fill_info():
    df_info = pd.read_csv('information.csv')
    url_list = []
    for i in df_info['链接']:
        url_list.append(i)
    return url_list

#访问url页面  将url列表循环  依次访问页面并且正则
# def a(html):
#     info{}
#     gangwei = s.select_one('#main > div.job-box > div > div.job-detail > div.detail-content > div:nth-of-type(1) > div').text.strip()
#     tuandui = s.select_one('#main > div.job-box > div > div.job-detail > div.detail-content > div:nth-of-type(2) > div').text
#     info['respon'] = gangwei
#     info['teaminfo'] = tuandui
#     return info
# def b():

def get_html(url_list):
    a = 0
    b = True
    for url in url_list[:10]:
        a += 1
        html = requests.get(url,headers = header).text
        gangwei = '<h3>职位描述</h3>\s*<div class="text">(.*?)</div>'
        tuandui = '<h3>团队介绍</h3>\s*<div class="text">(.*?)</div>'
        fuli = '<div class="job-tags">\s*(.*?)\s*</div>'
        gongsi = '<h3>公司介绍</h3>\s*<div class="text">(.*?)</div>'

        gangwei_re = re.findall(gangwei,html,re.S)[0].replace('<br/>','').strip()
        tuandui_re = re.findall(tuandui,html,re.S)
        fuli_re = re.findall(fuli,html,re.S)
        gongsi_re = re.findall(gongsi,html,re.S)

        if gongsi_re:
            gongsi_re = gongsi_re[0].replace('<br/>','').replace('&ldquo','').replace('&rdquo','').strip()
        else:
            gongsi_re = np.nan

        if tuandui_re:
            tuandui_re = tuandui_re[0].replace('<br/>','')
        else:
            tuandui_re = np.nan

        if fuli_re:
            fuli_re = fuli_re[0].replace('<span>','').replace('</span>',',')
        else:
            fuli_re = np.nan

        info_dict = {'job_desc':[gangwei_re],
                'team_info':[tuandui_re],
                'company_welfare':[fuli_re],
                'company_info':[gongsi_re]}
        print(info_dict)
        df = pd.DataFrame(info_dict)
        if a == 2:
            b = False
        df.to_csv('xiangxi.csv',encoding='utf_8_sig',mode='a',header = b,index = None)
        print(df)
    return info_dict

x = fill_info()
get_html(x)