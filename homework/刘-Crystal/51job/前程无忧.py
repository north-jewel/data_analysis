import requests
import re
from cityinfo import city_info
from info_re import all_re
import numpy as np
import pandas as pd


class Job:

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
    CITY = city_info()
    All_re = all_re()

    def __init__(self,
                 city, job,
                 encoding='gbk',

                 ):
        self.encoding = encoding
        self.city = city
        self.job = job
        self.every_url = self.job_url()
        self.small_url = self.small_url()
        self.data = self.job_info()

    def job_url(self):
        params = {
            'lang': 'c',
            'stype': '',
            'postchannel': '0000',
            'workyear': '99',
            'cotype': '99',
            'degreefrom': '99',
            'jobterm': '99',
            'companysize': '99',
            'providesalary': '99',
            'lonlat': '0,0',
            'radius': '-1',
            'confirmdate': '9',
            'fromType': '',
            'dibiaoid': '0',
            'address': '',
            'line': '',
            'specialarea': '00',
            'from': '',
            'welfare': ''}
        num = self.CITY[self.city]
        url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,1.html'.format(num, self.job)
        res = requests.get(url, params=params, headers=self.header)
        res.encoding = self.encoding
        page_re = '<span class="td">共(.*?)页，到第</span>'
        page = re.findall(page_re, res.text)[0]
        job_url_list = []
        for i in range(1, 5):
            if i > 2:
                url = url.replace('2,{}.'.format (i - 1), '2,{}'.format (str (i) + '.'))
            else:
                url = url.replace('1.', '{}'.format (str (i) + '.'))

            job_url_list.append(url)
        print(job_url_list)
        return job_url_list

    def small_url(self):

        url_list = []
        for i in self.every_url:
            res1 = requests.get(i, headers=self.header)
            res1.encoding = self.encoding
            url_re = '<a target="_blank" title=".*?" href="(.*?)" onmousedown="">\
'
            new_url = re.findall(url_re, res1.text)
            url_list.append(new_url)
        print(url_list)
        return url_list

    def job_info(self):
        city_list = []
        skill_list = []
        company_name_list = []
        company_size_list = []
        company_welfare_list = []
        company_type_list = []
        company_location_list = []
        salary_list = []
        edu_req_list = []
        experience_required_list = []
        company_description_list = []
        job_required_list = []
        info_data = {}
        for every_url_list in self.small_url:
            for i in every_url_list:
                url_res = requests.get(i, headers=self.header)
                url_res.encoding = self.encoding
                # 学历匹配
                info_sum = re.findall(self.All_re['city_All'], url_res.text,)[0]
                # print(info_sum)
                # 城市
                try:
                    city_1 = re.findall(self.All_re['city1'], info_sum, re.S)[0]
                except IndexError:
                    city_1 = np.nan

                # print(city_1)
                # 技能
                try:
                    skill_type = re.findall(self.All_re['skill_type'], url_res.text)[0]
                except IndexError:
                    skill_type = np.nan

                # print(skill_type)
                # 公司名字
                try:
                    company_name = re.findall(self.All_re['company_name'], url_res.text)[0]
                except IndexError:
                    company_name = np.nan
                # print(company_name)
                # 公司描述

                company = re.findall(self.All_re['company_description'], url_res.text)
                try:
                    company_size = company[1]
                except IndexError:
                    company_size = np.nan
                # print(company_size)
                try:
                    company_type = company[0]
                except IndexError:
                    company_type = np.nan
                # print(company_type)
                try:
                    company_description = company[2]

                except IndexError:
                    company_description = np.nan
                # print(company_description)
                # 工作需求
                job_required = re.findall(self.All_re['job_required'], url_res.text, re.S)[0].replace('\r', '').replace('\n', '').\
                    replace('\t', '').replace('<p>', '').replace('<span>', '').replace('</span>', '').replace('</p>', '').replace('<br>', '').replace('<div>', '').replace('</div>', '').replace('<strong>', '').replace('</strong>', '').replace('<b>', '').replace('</b>', '').replace('<p>','').replace('</p>', '')
                # print(job_required)
                # 公司位置
                try:
                    company_location = re.findall(self.All_re['company_location'], url_res.text)[0]
                except IndexError:
                    company_location = np.nan
                # print(company_location)
                # 经验需求
                experience_required = re.findall(self.All_re['experience_required'], info_sum, re.S)[0].replace('|', '').replace('&nbsp;', '')+'经验'
                # print(experience_required)
                # 公司福利
                company_welfare = re.findall(self.All_re['company_welfare'], url_res.text)
                if len(company_welfare) == 0:
                    company_fuli = np.nan
                else:
                    company_fuli = ''
                    for i in company_welfare:
                        company_fuli = company_fuli+i
                # print(company_fuli)
                # 薪资

                salary = re.findall(self.All_re['salary'], url_res.text)[1]
                if salary == '':
                    salary = np.nan

                # print(salary)
                if '本科' in info_sum:
                    edu_req = '本科'
                    # print(edu_req)
                elif '大专' in info_sum:
                    edu_req = '大专'
                    # print(edu_req)
                elif '硕士' in info_sum:
                    edu_req = '硕士'
                    # print(edu_req)
                elif '博士' in info_sum:
                    edu_req = '博士'
                    # print(edu_req)
                elif '研究生'in info_sum:
                    edu_req = '研究生'
                    # print(edu_req)
                else:
                    edu_req = np.nan
                    # print(edu_req)

                city_list.append(city_1)
                skill_list.append(skill_type)
                company_name_list.append(company_name)
                company_description_list.append(company_description)
                company_location_list.append(company_location)
                company_welfare_list.append(company_welfare)
                company_size_list.append(company_size)
                company_type_list.append(company_type)
                salary_list.append(salary)
                edu_req_list.append(edu_req)
                experience_required_list.append(experience_required)
                job_required_list.append(job_required)

        info_data['city'] = city_list
        info_data['skill_type'] = skill_list
        info_data['company_name'] = company_name_list
        info_data['company_description'] = company_description_list
        info_data['company_location'] = company_location_list
        info_data['company_welfare'] = company_welfare_list
        info_data['company_size'] = company_size_list
        info_data['company_type'] = company_type_list
        info_data['salary'] = salary_list
        info_data['edu_require'] = edu_req_list
        info_data['experience'] = experience_required_list
        info_data['job_require'] = job_required_list
        return info_data

    def save_csv(self):
        location = r'C:\Users\lenovo\Desktop\data.csv'
        df = pd.DataFrame(data=self.data)
        df.to_csv(location, encoding='gbk')


J = Job(city='太原', job='Java')
J.save_csv()