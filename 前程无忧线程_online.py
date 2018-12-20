import threading
import time
import os
import requests
import re
import pandas as pd
from mas_info import massage_info
edu_required_2 = []
city_2 = []
skill_type_2 = []
salary_2 = []
company_name_2 = []
company_size_2 = []
company_type_2 = []
company_description_2 = []
company_location_2 = []
job_required_2 = []
experience_required_2 = []
company_welfare_2 = []
other_3 = []
skill_type_1 = '<h1 title="(.*?)">'#职业
salary_1 = '<strong>(.*?)</strong>'
company_name_1 = '<a href=".*?" target="_blank" title="(.*?)"'  # 公司名称
company_size_1 = '<span class="i_people"></span>(.*?)</p>'#公司规模
company_type_1 = '<span class="i_flag"></span>(.*?)</p>'#公司类型
company_description_1 = '<div class="tmsg inbox">(.*?)</div>\
'#公司简介
company_location_1 = '<span class="label">上班地址：</span>(.*?)</p>'#公司位置
job_required_1 = '<div class="bmsg job_msg inbox">(.*?)<div class="mt10">\
'  # 职业需求.技能要求
experience_required_1 = '&nbsp;&nbsp;(.*?)经验'#经验要求
company_welfare_1 = '<span class="sp4">(.*?)</span>'#公司福利.匹配多个
other_1 = r'<p class="msg ltype" title="(.*?)">'
other_2 = '&nbsp;&nbsp;招(.*?)人'
list_123 = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
def thread_spider(city,job,arg):
    city_info = massage_info()
    city_1 = city_info[city]
    url_info = []
    for i in range(1,arg):
        url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html?\
        lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99\
        &companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate\
        =9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(city_1,job,i)
        re_a = '<a target="_blank" title=".*?" href="(.*?)" onmousedown="">'
        Fuak = requests.get(url, headers=headers)
        Fuak.encoding = 'gbk'
        page_y = re.findall(re_a,Fuak.text)
        url_info.append(page_y)
        list_123.append(url_info)
    return list_123
def spider_info(city,url):

    a = ''
    try:
        page_all = requests.get(url, headers=headers)
    except requests.exceptions.SSLError:
        pass
    except requests.exceptions.ConnectionError:
        pass
    else:
        page_all.encoding = 'gbk'
        salary = re.findall(salary_1, page_all.text)[1]
        skill_type = re.findall(skill_type_1, page_all.text)[0]
        company_name = re.findall(company_name_1, page_all.text)[0]
        company_size = re.findall(company_size_1, page_all.text)[0]
        company_type = re.findall(company_type_1, page_all.text)[0]
        company_description = re.findall(company_description_1, page_all.text, re.S)[0].replace('\r', '').replace('\n','').replace('<br>', '').replace('<div>', '').replace('</br>', '').replace('</p>', '').replace('&nbsp;', '').replace('&amp;','').replace('<p>', '').replace('</div>', '').replace('</span>', '').replace('<b>', '').replace('</b>', '')
        company_location = re.findall(company_location_1, page_all.text)
        job_required = re.findall(job_required_1, page_all.text,re.S)[0].replace('\r', '').replace('\n', '').replace('<br>', '').replace('<div>', '').replace('</br>', '').replace('</p>', '').replace('&nbsp;', '').replace('&amp;','').replace('<p>', '').replace('</div>', '').replace('</span>', '').replace('<b>', '').replace('</b>', '').replace('<span>', '')
        company_welfare = re.findall(company_welfare_1, page_all.text)
        Three_f = re.findall(other_1, page_all.text, re.S)
        for u in company_location:
            company_location = u.replace('\t', '')
        if len(company_welfare) == 0:
            company_welfare = '######'
        if len(salary) == 0:
            salary = '######'
        if len(company_location) == 0:
            company_location = '######'
        if len(company_size) == 0:
            company_size = '######'
        else:
            for x in company_welfare:
                a = a + x
            company_welfare = a
        for k in Three_f:
            experience_required = re.findall(experience_required_1, k, re.S)[0].replace('|', '').replace('&nbsp;','') + '经验'
            other = '招' + re.findall(other_2, k, re.S)[0] + '人'
            if '本科' in k:
                edu_required = '本科'
            elif '大专' in k:
                edu_required = '大专'
            elif '硕士' in k:
                edu_required = '硕士'
            elif '研究生' in k:
                edu_required = '研究生'
            elif '博士' in k:
                edu_required = '博士'
            else:
                edu_required = '######'
        salary_2.append(salary)
        skill_type_2.append(skill_type)  # 1
        company_name_2.append(company_name)
        company_size_2.append(company_size)
        company_type_2.append(company_type)
        company_description_2.append(company_description)
        company_location_2.append(company_location)
        job_required_2.append(job_required)
        experience_required_2.append(experience_required)
        other_3.append(other)
        city_2.append(city)
        edu_required_2.append(edu_required)
        company_welfare_2.append(company_welfare)
        print(city_2)
def write_dict(city,job,page):
    city_info = massage_info()
    city_3 = city_info[city]
    url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,1.html?\
            lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99\
            &companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate\
            =9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(city_3, job)
    page_re = '<span class="td">共(.*?)页，到第</span>'
    res = requests.get(url,headers = headers)
    res.encoding = 'gbk'
    page_info = re.findall(page_re,res.text)[0]
    page_info = int(page_info)
    if page_info<int(page):
        print('请输入正确的页数，最大不能超过{}'.format(page_info))
    else:
        list_url = thread_spider(city,job,int(page)+1)
        dict_info = {}
        thread_list = []
        for y in list_url[0]:
            for i in y:
                t = threading.Thread(target=spider_info, args=(city,i,))
                thread_list.append(t)
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        for t in thread_list:
            t.join()
        dict_info['city'] = city_2
        dict_info['salary'] = salary_2
        dict_info['skill_type'] = skill_type_2
        dict_info['company_name'] = company_name_2
        dict_info['company_size'] = company_size_2
        dict_info['company_type'] = company_type_2
        dict_info['company_description'] = company_description_2
        dict_info['company_location'] = company_location_2
        dict_info['job_required'] = job_required_2
        dict_info['edu_required'] = edu_required_2
        dict_info['experience_required'] = experience_required_2
        dict_info['company_welfare'] = company_welfare_2
        dict_info['other'] = other_3
        df = pd.DataFrame(dict_info)
        path = os.getcwd()+'\\51job_3.csv'
        df.to_csv(path,encoding = 'gbk')
        print('成功添加至代码目录~')
city = input('请输入要爬取的城市：')
job = input('请输入要爬取的工作：')
page = input('请输入爬取的页数（网页）：')
write_dict(city,job,page)
