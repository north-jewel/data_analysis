import requests
import re
import csv
import os
import pandas as pd
from proxiess import Ip

class company:
    def __init__(self,
                 header ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}):
        self.header = header
        # self.companyhtml = self.companyhtml()

#返回的是
    def companyhtml(self,url):
        #网页源代码
        html = requests.get(url,headers = self.header)
        html_info = html.text
        # print(html_info)

        # 正则表达式  职位描述的链接
        post_name = '<a href="(.*?)" data-jid'
        company_name = '<h3 class="name"><a href=".*?" ka=".*?" target=".*?">(.*?)</a></h3>'
        company_location  = '<p>(.*?)<em class="vline"></em>.*?<em class="vline"></em>(.*?)</p>'
        company_size = '<p>(.*?)<em class="vline"></em>.*?<em class="vline"></em>(.*?)</p>'
        salary = '<span class="red">(.*?)</span>'
        # company_type = '<p>(.*?)<em class="vline"></em>.*?<em class="vline"></em>.*?</p>'
#抓到的内容
        res = '''<h3 class="name"><a href=".*?" ka="search_list_company_1_custompage" target="_blank">.*?</a></h3>
                                            <p>互联网<em class="vline"></em>.*?<em class="vline"></em>20-99人</p>'''

        res = re.findall(res,html,re)
        post_name = re.findall(post_name,html_info)
        company_name = re.findall(company_name,html_info)
        company_location = re.findall(company_location,html_info)
        company_size = re.findall(company_size,html_info)
        salary = re.findall(salary,html_info)
        # company_type = re.findall(company_type,html_info)
        print(company_location)
        print(company_size)
        # print(company_type)
# 将公司的信息放入各自的列表
        company_type = []
        company_location_1 = []
        company_size_a = []
        company_education = []
        for i in company_location[::2]:
            company_location_1.append(i[0])
            company_education.append(i[1])
        for n in company_location[::-2]:
            company_type.append(n[0])
            company_size_a.append(n[1])
        # print(post_name)
        # print(company_name)
        # print(salary)
        # print(company_size_a)
        # print(company_education)
        # print(company_location_1)
        # print(company_type)
        return post_name,company_name,company_location_1,company_type,company_size_a,company_education

    def write_info_df(self,df_list):
        info =list(zip(df_list[0],df_list[1],df_list[2],df_list[3],df_list[4],df_list[5]))
        df = pd.DataFrame(info,columns=['url','company_name','company_location','company_type','company_type','company_education'])
        df.to_csv('aaa.csv', encoding='gb2312', index=False)


    def write_info_df2(self,df,url):
        save_df = read_csv('aaa.csv')
        for i in save_df.url:
            url_r = url + 'i'
            job = requests.get(url_r,headers = self.header)

            info_r =''





if __name__ == '__main__':
    urla = 'http://www.xicidaili.com/nn/'
    a = Ip()
    html = a.getHTMLText(urla)
    info = a.get_can_ip(a.get_Ip(html))
    A = info[0][0]
    B = info[0][1]
    # print(A)
    # print(B)
    proxies = {'https': '{}:{}'.format(A,B), 'http': '{}:{}'.format(A,B)}
    # print(proxies)
    # for i in range(1,11):
    url = 'https://www.zhipin.com/c101010100/?query={}&page={}&ka=page-next'.format('python',2)
    a = company()
    # print(a.companyhtml(url))
    url_a = 'https://www.zhipin.com'
    a.write_info(a.companyhtml(url))
