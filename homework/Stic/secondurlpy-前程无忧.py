#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @时间    :   2018/12/5 9:43
# @原创人  : zdh
# @文件名  : secondurlpy.py
# @项目名称: PyCharm

# 第二层url
import requests
from bs4 import BeautifulSoup
url = 'https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0'
res = requests.get(url)
class Result:
    '''
    前程无忧结果详细信息
    传入结果url
    '''
    def __init__(self,url = 'https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0',
                 ):
        res = requests.get(url)
        self.soup = BeautifulSoup(res.text, 'html.parser')
    def company_name(self):
        '''
        公司名字
        :return:'南京高泰科技有限公司'
        '''
        company_name = self.soup.select_one('a.catn').get('title')
        return company_name
    def job_required(self):
        '''
        职位要求
        :return:[1...,2...,3...,4...,5...,...]
        '''
        job_required = self.soup.select('div.inbox > p')[:-1]
        job_required = [i.text.strip() for i in job_required]
        job_required = [''.join(i.split()) for i in job_required if len(i) != 0]
        return job_required
    def company_location(self):
        '''
        公司地点
        :return:'上班地址：北京市石景山区苹果园街道八大处路45号点石商务公园8号楼7楼'
        '''
        company_location = self.soup.select_one('div.bmsg > p.fp').text
        return company_location
    def company_required(self):
        '''
        公司需求
        :return:['北京-石景山区', '5-7年经验', '本科', '招1人', '12-05发布']
        '''
        company_required = self.soup.select_one('p.msg').text
        company_required = company_required.split('|')
        company_required = ["".join(i.split()) for i in company_required]
        return company_required
    def company_city(self):
        '''
        公司所在城市
        :return: '北京-石景山区'
        '''
        company_required = self.skills_required()
        company_city = company_required[0]
        return company_city
    def experience_required(self):
        '''
        工作经验
        :return: '5-7年经验'
        '''
        company_required = self.skills_required()
        experience_required = company_required[1]
        return experience_required
    def edu_required(self):
        '''
        学历要求
        :return:'本科'
        '''
        company_required = self.skills_required()
        edu_required = company_required[2]
        return edu_required
    def recruit_num(self):
        '''
        招聘人数
        :return: , '招1人'
        '''
        company_required = self.skills_required()
        recruit_num = company_required[3]
        return recruit_num
    def release_time(self):
        '''
        发布时间
        :return: '12-05发布'
        '''
        company_required = self.skills_required()
        release_time = company_required[4]
        return release_time
    def company_description(self):
        '''
        公司描述
        :return:[<p class="at" title="民营公司"><span class="i_flag"></span>民营公司</p>, <p class="at" title="50-150人"><span class="i_people"></span>50-150人</p>, <p class="at" title="计算机软件,计算机服务(系统、数据服务、维修)"><span class="i_trade"></span><a href="https://company.51job.com/beijing/hy01/">计算机软件</a><a href="https://company.51job.com/beijing/hy38/">计算机服务(系统、数据服务、维修)</a></p>]
        '''
        company_description = self.soup.select('p.at')
        return company_description
    def company_type(self):
        '''
        公司类型
        :return: '民营公司'
        '''
        company_description = self.company_description()
        company_type = company_description[0].text
        return company_type
    def company_size(self):
        '''
        公司规模
        :return:'50-150人'
        '''
        company_description = self.company_description()
        company_size = company_description[1].text
        return company_size
    def skill_type(self):
        '''
        公司主营
        :return:'计算机软件,计算机服务(系统、数据服务、维修)'
        '''
        company_description = self.company_description()
        skill_type = [i.text.strip() for i in company_description[2:]]
        return skill_type
    def company_info(self):
        '''
        公司信息
        :return:'我公司成立于2003年12月，是专业从事电信类软件开发和系统集成项目的科技型企业。...'
        '''
        company_info = self.soup.select_one('div.tmsg').text
        return company_info
    def company_welfare(self):
        '''
        公司福利
        :return:['五险一金', '员工旅游', '餐饮补贴', '通讯补贴', '定期体检', '周末双休', '免费班车', '年终奖金', '专业培训']
        '''
        company_welfare = self.soup.select('div.t1 > span')
        company_welfare = [i.text.strip() for i in company_welfare]
        return company_welfare
    def salary(self):
        '''
        工资
        :return:'2-2.5万/月'
        '''
        salary = self.soup.select_one('div.cn > strong').text
        return salary
    def skills_required(self):
        '''
        技能要求
        :return:['高级软件工程师', '软件工程师']
        '''
        skills_required = self.soup.select('p.fp > a')
        skills_required = [i.text.strip() for i in skills_required]

        return skills_required

# print(res)
if res.status_code==200:
    res.encoding = 'gbk'
    # print(res.text)
    soup = BeautifulSoup(res.text,'html.parser')
    div = soup.find(class_='tHeader tHjob')
    # print(div)
    # print(div.h1)
    # print(type(div.h1.get('title')))
    # print(div.h1.get('title'))
    # print(soup.find('h1').text.strip())
    #
    # print(soup.select_one('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > h1').text)
    # print(soup.select_one('div > h1').text)

    # 找唯一标识 ！！！！
    # 有n多种方法 仁者见仁智者见智
    # title = div.h1.get('title')
    # company_name = soup.select_one('body > div.tCompanyPage > '
    #                                'div.tCompany_center.clearf
    # company_name = soup.select_one('a.catn').get('title')
    # print(company_name)
    #
    # company_location = soup.select_one('div.bmsg > p.fp').text
    # print(company_location)
    # edu_required = soup.select_one('p.msg').text
    # edu_required = edu_required.split('|')
    # edu_required = ["".join(i.split()) for i in edu_required]
    # print(edu_required)
    # company_description = soup.select('p.at')
    # print(company_description)
    # company_type = company_description[0].text
    # print(company_type)
    # company_size = company_description[1].text
    # skill_type = [i.text.strip() for i in company_description[2:4]]
    # print(skill_type)
    # company_info = soup.select_one('div.tmsg').text
    # print(company_info.strip())
    # company_welfare = soup.select('div.t1 > span')
    # company_welfare = [i.text.strip() for i in company_welfare]
    # print(company_welfare)
    # salary =  soup.select_one('div.cn > strong').text
    # print(salary)
    # skills_required = soup.select('p.fp > a')
    # skills_required = [i.text.strip() for i in skills_required]
    # print(skills_required)
    # job_required = soup.select('div.bmsg > p')
    # job_required = [i.text.strip() for i in job_required][:-1]
    # job_required = [''.join(i.split()) for i in job_required if len(i) != 0]
    # print(job_required)
    shijia = Result('https://jobs.51job.com/shijiazhuang/108939972.html?s=01&t=0')
    print(shijia.company_required())
    # body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > h1