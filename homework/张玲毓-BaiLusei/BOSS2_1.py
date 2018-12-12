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
    # print(url_list[15])
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

def get_html():
    url = 'https://www.zhipin.com/job_detail/42db2756750a587b1XN539-_E1M~.html?ka=search_list_24'
    # a = 0
    # b = True
    # for url in url_list:
    #     a += 1
    html = requests.get(url,headers = header).text
    print(html)
    # gangwei_re = '<div class="text">岗位要求<br/>(.*?)</div>'
    # tuandui_re = '<div class="job-tags">(.*?)</div>'
    # gongsi_re = ' <div class="job-sec company-info"><h3>.*?</h3><div class="text">(.*?)</div><a ka="job-comintroduce" href="/gongsi/e715aa1be4283fc21nd62tq5.html" target="_blank" class="look-all"><span>...</span>查看全部</a></div>'
    # s = BeautifulSoup(html,'html.parser')
    info = {}
    # gangwei = s.select_one('#main > div.job-box > div > div.job-detail > div.detail-content > div:nth-of-type(1) > div')
    # tuandui = s.select_one('#main > div.job-box > div > div.job-detail > div.detail-content > div:nth-of-type(2)')
    # fuli = s.select_one('#main > div.job-box > div > div.job-detail > div.detail-content > div:nth-of-type(2) > div')
    # gongsi = s.select_one('#main > div.job-box > div > div.job-detail > div.detail-content > div.job-sec.company-info > div')
    # gangwei = s.select_one('#main > div.job-box > div > div.job-detail > div.detail-content > div:nth-of-type(1)')
    # tuanduifuli = s.select_one('#main > div.job-box > div > div.job-detail > div.detail-content > div:nth-of-type(2)')
    # gongsi = s.select_one('#main > div.job-box > div > div.job-detail > div.detail-content > div.job-sec.company-info')
    gangwei = '<h3>职位描述</h3>\s*<div class="text">(.*?)</div>'
    tuandui = '<h3>团队介绍</h3>\s*<div class="text">(.*?)</div>'
    fuli = '</div>\s*<div class="job-tags">\s*(.*?)\s*</div>'
    gongsi = '<h3>公司介绍</h3>\s*<div class="text">(.*?)</div>'
    gangwei_re = re.findall(gangwei,html,re.S)
    tuandui_re = re.findall(tuandui,html,re.S)
    fuli_re = re.findall(fuli,html,re.S)
    gongsi_re = re.findall(gongsi,html,re.S)
    if tuandui == 'None':
        info['jobdesc'] =
    # fuli_re = re.findall(fuli, html, re.S)[0].replace('<span>', '').replace('</span>', '').strip()
    # gangwei_re = re.findall(gangwei, html, re.S)[0].replace('<br/>', '')
    print(gangwei_re)
    print(tuandui_re)
    print(fuli_re)
    print(gongsi_re)
    #
    # if tuandui == 'None':
    #     info['teaminfo'] = ''
    #     info['jobdesc'] =gangwei.text.strip()
    #     info['weflare'] = fuli.text.strip()
    # if gongsi == 'None':
    #     info['campanyinfo'] = ''
    # if gongsi == 'None' and tuandui == 'None':
    #     info['teaminfo'] = ''
    #     info['campanyinfo'] = ''
    # if fuli == 'None':
    #     info['weflare'] = ''
    #
    # print(info)
    # df = pd.DataFrame(info, index=[0])
    # df.to_csv('info.csv', mode='a', header=True, encoding='utf_8_sig', index=False)


    # print('第{}条'.format(a))
        # df = pd.DataFrame(info,index = [0])
        # # print(df)
        # print('第{}条'.format(a))
        # if a == 2:
        #     b = False
        # df.to_csv('info.csv',mode='a',header = b,encoding='utf_8_sig',index= False)
    # print(tuandui)
    # print(gangwei)
    # print(gongsi)

    return info

# x = fill_info()
get_html()
# 16 32 49