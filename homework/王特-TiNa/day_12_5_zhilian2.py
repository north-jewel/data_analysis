import re,requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

class Regex:

    def __init__(self):
        self.charset = 'utf-8'

    def Html_text(self,url):
        html = requests.get(url)
        html.encoding = self.charset
        html_text = html.text
        return html_text

    def re_cont(self,regex,html_text):
        re_cont = re.findall(regex,html_text)
        return  re_cont

class XiangXi(Regex):

    def __init__(self,url,dic):
        self.dic = dic
        self.url = self.dic['webpage']
        self.r = Regex()
        self.html = requests.get(self.url).text
        self.s = BeautifulSoup(self.html, 'html.parser')
        self.html_cont = self.r.Html_text(self.url)
        self.Company_name = self.dic['Company_name']
        self.Company_location = self.Company_location()
        self.Skills_required = self.Skills_required()
        self.Company_description = self.Company_description()

    def Company_description(self):
        try:
            Company_description = self.s.find_all('div', class_='pos-ul')[0]
        except:
            print(self.url)
            print(self.Company_name, ' "公司介绍" 信息爬取失败')
            return {'Skills_required': np.nan}
        else:
            Company_description = Company_description.text.lstrip()
            return {'Company_description' : Company_description}

    def Company_location(self):
        re_ = '''<p class="add-txt"><span class="icon-address"></span>(.*?)</p>'''
        re_cont = self.r.re_cont(re_, self.html_cont)
        if re_cont:
            try:
                re_cont = re_cont[0]
            except:
                print(self.Company_name, ' "办公地点" 信息爬取失败')
                return {'Company_location':np.nan}
            else:
                return {'Company_location':re_cont}
        else:
            Company_location = self.s.find_all('p',class_='c9')
            Company_location = Company_location[0].text.lstrip()
            return {'Company_location':Company_location}

    def Skills_required(self):
        re_ = '''<div class="pos-ul">
(.*?)
</div>'''
        re_cont = self.r.re_cont(re_, self.html_cont)
        try:
            re_cont = re_cont[0]
        except:
            print(self.url)
            Skills_required = self.s.find_all('div', class_='pos-ul')
            Skills_required = Skills_required[0].text.lstrip().replace(r'\xa0','')
            print(Skills_required)
            return {'Skills_required':Skills_required}
        else:
            p = re.compile('<[^>]+>')
            re_cont = p.sub('', re_cont)
            re_cont = re_cont.replace('&nbsp;',' ').replace(r'\xa0',' ').replace('•',' ')
            return {'Skills_required':re_cont}

    def joint(self):
        self.dic.update(self.Company_description)
        self.dic.update(self.Skills_required)
        self.dic.update(self.Company_location)
        return self.dic

def dict_info(url,df):
    a = requests.get(url).json()
    a = a['data']['results']
    b = 0
    for aa in a:
        dic = {}
        dic['City'] = aa['city']['display']
        dic['Company_name'] = aa['company']['name']
        dic['Company_size'] = aa['company']['size']['name']
        dic['Company_type'] = aa['company']['type']['name']
        dic['salary'] = aa['salary']
        dic['job_required'] = aa['jobName']
        dic['edu_required'] = aa['eduLevel']['name']
        dic['experience_required'] = aa['workingExp']['name']
        dic['company_welfare'] = ','.join(aa['welfare'])
        dic['webpage'] = aa['positionURL']
        ddic = XiangXi(dic['webpage'], dic).joint()
        df = df.append(ddic, ignore_index=True)
        b += 1
        print('第', b, ' 条完成！')
    return df

if __name__ == '__main__':
    df = pd.read_csv(r'C:\Users\XIAOMI\Desktop\GiTHub\Day2\ZhiLian\zhilianzhaopin2.csv')
    for i in range(5):
        url = '''
        https://fe-api.zhaopin.com/c/i/sou?start={}pageSize=60&cityId=530&industry=10100&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3'''.format(i*60)
        df = dict_info(url,df)
        print(i,' 页完成')
    df.to_csv(r'C:\Users\XIAOMI\Desktop\GiTHub\Day2\ZhiLian\zhilianzhaopin2.csv', index=False, encoding='gbk')
    print('end')
