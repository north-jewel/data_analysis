import re,requests,time,random
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

class Info:

    def __init__(self,url):
        self.url = url
        self.html = requests.get(self.url).text
        self.s = BeautifulSoup(self.html,'html.parser')
        self.job_required = self.job_required()
        self.Company_name = self.Company_name()
        self.salary = self.salary()
        self.Company_type_size = self.Company_type_size()
        self.Company_location = self.Company_location()
        self.Company_welfare = self.Company_welfare()
        self.Company_description = self.Company_description()
        self.C_exper_edu = self.C_exper_edu()
        self.Skills_required = self.Skills_required()

    # 职位要求
    def job_required(self):
        try:
            job_required = self.s.select_one('div.cn > h1')
        except Exception as e:
            with open('报错信息收集.txt','a') as f:
                f.write(self.url)
                f.write('\n')
                f.write('job_required')
                f.write('\n')
                f.write(e)
                f.write('\n\n')
                job_required = np.nan
        else:
            job_required = job_required.text.lstrip().rstrip()
        # print(job_required)
        return job_required

    # 公司名称
    def Company_name(self):
        try:
            Company_name = self.s.select_one('p.cname > a.catn')
        except Exception as e:
            with open('报错信息收集.txt','a') as f:
                f.write(self.url)
                f.write('\n')
                f.write('Company_name')
                f.write('\n')
                f.write(e)
                f.write('\n\n')
            Company_name = np.nan
        else:
            Company_name = Company_name.text.lstrip().rstrip()
        # print(Company_name)
        return Company_name

    # 薪资
    def salary(self):
        try:
            salary = self.s.select_one('div.cn > strong')
        except Exception as e:
            with open('报错信息收集.txt','a') as f:
                f.write(self.url)
                f.write('\n')
                f.write('salary')
                f.write('\n')
                f.write(e)
                f.write('\n\n')
                salary = np.nan
        else:
            salary =  salary.text.lstrip().rstrip()
        return salary

    # 公司类型 公司大小
    def Company_type_size(self):
        Company_info = self.s.find_all('p',class_='at')
        Company_info_list = []
        for i in Company_info:
            Company_info_list.append(i.text)
        Company_type = Company_info_list[0]
        Company_size = Company_info_list[1]
        # print(Company_type)
        # print(Company_size)
        return [Company_type,Company_size]

    # 办公地址
    def Company_location(self):
        try:
            Company_location = self.s.find_all('p',class_='fp')
        except Exception as e:
            with open('报错信息收集.txt','a') as f:
                f.write(self.url)
                f.write('\n')
                f.write('Company_location')
                f.write('\n')
                f.write(e)
                f.write('\n\n')
                Company_location = np.nan
        else:
            Company_location = Company_location[1].text.replace('\n','')
        # print(Company_location)
        return Company_location

    # 公司福利
    def Company_welfare(self):
        try:
            Company_welfare_list = self.s.find_all('span',class_='sp4')
        except Exception as e:
            with open('报错信息收集.txt','a') as f:
                f.write(self.url)
                f.write('\n')
                f.write('Company_location')
                f.write('\n')
                f.write(e)
                f.write('\n\n')
                Company_welfare_str = np.nan
        else:
            Company_welfare_str = ''
            for i in Company_welfare_list:
                Company_welfare_str += '{},'.format(i.text)
        # print(Company_welfare_str)
        return Company_welfare_str


    # 公司简介
    def Company_description(self):
        try:
            Company_description = self.s.find_all('div',class_ = 'tmsg inbox')
        except Exception as e:
            with open('报错信息收集.txt','a') as f:
                f.write(self.url)
                f.write('\n')
                f.write('Company_description')
                f.write('\n')
                f.write(e)
                f.write('\n\n')
                Company_description = np.nan
        else:
            Company_description = Company_description[0].text.lstrip().rstrip()
        # print(Company_description)
        return Company_description

    # 城市 工作经验 学历要求
    def C_exper_edu(self):
        experience_info = self.s.select_one('div.cn > p.msg.ltype').get('title').split('|')
        City = experience_info[0].replace(u'\xa0',u'')
        experience_required = experience_info[1].replace(u'\xa0',u'')
        edu_required = experience_info[2].replace(u'\xa0',u'')
        if '招' in edu_required:
            edu_required = np.nan
        # print(City)
        # print(experience_required)
        # print(edu_required)
        return [City,experience_required,edu_required]


    # 技能要求
    def Skills_required(self):
        try:
            Skills_required = self.s.select('div.tCompany_main > div > div > p')
        except Exception as e:
            with open('报错信息收集.txt','a') as f:
                f.write(self.url)
                f.write('\n')
                f.write('Company_location')
                f.write('\n')
                f.write(e)
                f.write('\n\n')
                Skills_required_str = np.nan
        else:
            Skills_required_str = ''
            for i in Skills_required:
                Skills_required_str += i.text
            Skills_required_str = Skills_required_str.rstrip().rstrip().replace('\n','').replace(u'\xa0',u'')
        # print(Skills_required_str)
        return Skills_required_str


    def joint(self,num_):
        dic = {}
        dic['City'] = self.C_exper_edu[0]
        dic['Company_name'] = self.Company_name
        dic['Company_size'] = self.Company_type_size[1]
        dic['Company_type'] = self.Company_type_size[0]
        dic['Company_description'] = self.Company_description
        dic['Company_location'] = self.Company_location
        dic['job_required'] = self.job_required
        dic['salary'] = self.salary
        dic['company_welfare'] = self.Company_welfare
        dic['edu_required'] = self.C_exper_edu[2]
        dic['experience_required'] = self.C_exper_edu[1]
        dic['Skills_required'] = self.Skills_required
        dic['webpage'] = self.url
        df = pd.DataFrame(dic,index=[0])
        df.to_csv(r'C:\Users\XIAOMI\Desktop\GiTHub\Day2\ZhiLian\zhilianzhaopin2.csv', index=False,header=False, encoding='utf_8_sig',mode='a')
        return df

if __name__ == '__main__':

    with open('前程无忧2.txt','r') as f:
        a = f.readlines()
        a_len = len(a)
        num_ = 1
        num_0 = 1
        for i in a:
            selp = random.randint(0, 5)
            if 'jobs' in i:
                print('开始第{}条数据...'.format(num_))
                try:
                    Info(i.replace('\n','')).joint(num_)
                    time.sleep(selp)
                    print('第{}条oK'.format(num_), '还有{}条数据'.format(a_len - num_))
                except Exception as  e:
                    with open('报错信息收集.txt', 'a') as f:
                        f.write(self.url)
                        f.write('\n')
                        f.write('Company_location')
                        f.write('\n')
                        f.write(e)
                        f.write('\n\n')
                    print(i.replace('\n',''))
                    print(e)
                    print('第{}条报错'.format(num_), '还有{}条数据'.format(a_len - num_))
                num_ += 1
                print('\n')
            else:
                with open('乱党.txt','a') as f:
                    print('乱党出现！添加至乱党txt')
                    print('乱党信息为：{}'.format(i))
                    f.write(i)
                    f.write('\n')
                    print('第{}条乱党添加oK'.format(num_0))
                    num_0 += 1
