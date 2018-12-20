from bs4 import BeautifulSoup
import bs4
import requests
import pandas as pd
import numpy as np
def info_text(url):

        headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

        html = requests.get(url,headers = headers)
        return html.text


def info_all(html):
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.find_all(class_='cn')[0]
        # 标题 = info.h1.text.strip()
        # 工资 = info.strong.text
        # 公司 = info.select('p')[0].select('.catn')[0].text.strip()

        all_info = info.select('p')[1].text.strip().replace('\xa0\xa0|\xa0\xa0','|')
        company_welfare = soup.find('div',class_='t1').text.strip().replace('\n','|')
        gongsi = soup.select('.tCompany_main')[0]
        skill_type = gongsi.select('.mt10')[0].select('p')[0].text.strip().replace('\t','').replace('\r','').replace('\n\n','|')
        keyword = gongsi.select('.mt10')[0].select('p')[1].text.strip().replace('\n','|')
        post_describe = str(gongsi.select('.job_msg > p')).replace('[','').replace(']','').replace(',','').replace('<p>','').replace('</p>','|').replace('<br/>','/')
        company_description = soup.select_one('.tmsg').text.strip()
        company_location = soup.find('div',class_='bmsg inbox').text.replace('\n','').replace('\t','')


                       # 信息   福利           职能类别   关键字   职位信息    公司介绍         上班地址
        info_list = [all_info,company_welfare,skill_type,keyword,post_describe,company_description,company_location]

        return info_list

df = pd.read_csv('前程无忧.csv')
columns1 = ['info_all','company_welfare','skill_type','keyword','post_describe','company_description','company_location']
all_columns = list(df.columns)+columns1
df = df.reindex(columns=all_columns,
                    fill_value=np.NaN)

url = 'https://jobs.51job.com/bangbu/108036732.html?s=01&t=0'
html = info_text(url)
value_all = info_all(html)
df.loc[df['url'].isin([url]), columns1] = value_all
leng = len(df)
url_list = df.url

for i in range(leng):
        try:
                url = url_list[i]
                html = info_text(url)
                value_all = info_all(html)
                df.loc[df['url'].isin([url]), columns1] = value_all
        except:
                df.to_csv('前程无忧详细信息.csv', index=None)
                print('第{}条出错url:{}'.format(i,url))
                break
        else:
                continue
        finally:
                df.to_csv('前程无忧详细信息.csv',index = None)