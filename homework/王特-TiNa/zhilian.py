import re,requests
import pandas as pd

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
        self.url = url
        self.r = Regex()
        self.html_cont = self.r.Html_text(self.url)
        self.dic = dic
        #self.Company_description = self.Company_description()
        self.Company_location = self.Company_location()
        self.Skills_required = self.Skills_required()

#     def Company_description(self):
#         re_ = '''<div class="intro-content">
# (.*?)
# </div>'''
#         re_cont = self.r.re_cont(re_, self.html_cont)
#         p = re.compile('<[^>]+>')
#         print(re_cont)
#         re_cont = p.sub('', re_cont[0])
#         re_cont = re_cont.replace('&nbsp;', ' ')
#         return {'Company_description':re_cont}

    def Company_location(self):
        re_ = '''<p class="add-txt"><span class="icon-address"></span>(.*?)</p>'''
        re_cont = self.r.re_cont(re_, self.html_cont)
        return {'Company_location':re_cont[0]}

    def Skills_required(self):
        re_ = '''<div class="pos-ul">
(.*?)
</div>'''
        re_cont = self.r.re_cont(re_, self.html_cont)
        p = re.compile('<[^>]+>')
        re_cont = p.sub('', re_cont[0])
        re_cont = re_cont.replace('&nbsp;',' ').replace('\xa0',' ').replace('•',' ')
        return {'Skills_required':re_cont}

    def joint(self):
        self.Company_location.update(self.Skills_required)
        self.dic.update(self.Company_location)
        return self.dic

def dict_info(url,df):
    dic = {}
    a = requests.get(url).json()
    a = a['data']['results']
    b = 0
    for aa in a:
        dic['City'] = aa['city']['display']
        dic['Company_name'] = aa['company']['name']
        dic['Company_size'] = aa['company']['size']['name']
        dic['Company_type'] = aa['company']['type']['name']
        dic['salary'] = aa['salary']
        dic['job_required'] = aa['jobName']
        dic['edu_required'] = aa['eduLevel']['name']
        dic['experience_required'] = aa['workingExp']['name']
        dic['company_welfare'] = aa['welfare']
        dic['webpage'] = aa['positionURL']
        ddic = XiangXi(dic['webpage'], dic).joint()
        df = df.append(ddic, ignore_index=True)
        print('第',b,' 条完成！')
        b += 1
    return df

if __name__ == '__main__':
    df = pd.read_csv(r'C:\Users\XIAOMI\Desktop\GiTHub\Day2\ZhiLian\zhilianzhaopin2.csv',encoding='gbk')
    for i in range(2):
        url = '''
        https://fe-api.zhaopin.com/c/i/sou?start={}pageSize=60&cityId=530&industry=10100&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3'''.format(i*60)
        df = dict_info(url,df)
        print(i,' 页完成')
    df.to_csv(r'C:\Users\XIAOMI\Desktop\GiTHub\Day2\ZhiLian\zhilianzhaopin2.csv', index=False, encoding='gbk')
    print('end')
