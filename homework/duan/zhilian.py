import re
import requests
import numpy as np
import pandas as pd
import time

url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&at=8282c6f234e54198ad914368ec99e7f3&rt=605d9e4a4d574aa9b7ce400505902d60&_v=0.88860985&userCode=637838355&x-zp-page-request-id=a1ee7b5a4b194395a589222027b3faaf-1543569068541-36049'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
          'Referer':'https://www.zhaopin.com/'}
res = requests.get(url)
#res.encoding = 'utf-8'
html = res.json()
info = html['data']['results']
def info_list():
    salary_list = []
    city_list = []
    skill_type_list = []
    company_name_list = []
    company_size_list = []
    company_type_list = []
    edu_required_list = []
    esperiende_required_list = []
    for i in range(len(info))[:10]:
        salary = info[i]['salary']
        if salary == '':
            salary_list.append('kongzhi')
        salary_list.append(salary)
        city = info[i]['city']['items'][0]['name']
        if city == '':
            city_list.append('kongzhi')
        city_list.append(city)
        skill_type = info[i]['jobType']['items'][1]['name']
        if skill_type == '':
            skill_type_list.append('kongzhi')
        skill_type_list.append(skill_type)
        company_name = info[i]['company']['name']
        if company_name == '':
            company_name_list.append('kongzhi')
        company_name_list.append(company_name)
        company_size = info[i]['company']['size']['name']
        if company_size == '':
            company_size_list.append('kongzhi')
        company_size_list.append(company_size)
        company_type = info[i]['company']['type']['name']
        if company_type == '':
            company_type_list.append('kongzhi')
        company_type_list.append(company_type)
        edu_required = info[i]['eduLevel']['name']
        if edu_required == '':
            edu_required_list.append('kongzhi')
        edu_required_list.append(edu_required)
        esperiende_required = info[i]['workingExp']['name']
        if esperiende_required == '':
            esperiende_required_list.append('kongzhi')
        esperiende_required_list.append(esperiende_required)
    return salary_list,city_list,skill_type_list,company_name_list,company_size_list,company_type_list,edu_required_list,esperiende_required_list
def info_list2():
    company_welfare_list = []
    company_location_list = []
    stills_required_list = []
    company_description_list = []
    for i in range(len(info))[:10]:

        company_welfare = info[i]['welfare']

        company_welfare_list.append(str(company_welfare))
        company_url = info[i]['positionURL']
        company_info = requests.get(company_url)
        #company_info.encoding = 'gbk'
        company_html = company_info.text

        regex_location = '<p class="add-txt"><span class="icon-address"></span>(.*?)</p>'
        company_location = re.findall(regex_location, company_html)

        company_location_list.append(str(company_location))
        regex_company_description = '<div class="intro-content">(.*?)</div>'
        company_description = re.findall(regex_company_description, company_html, re.M | re.S)

        com_info = company_description[0].replace('<font>', '').replace('</font>', '').replace('<br>', '').replace('<p>', '').replace('</p>', '').replace('<span>', '').replace('</span>', '').replace('\n','').replace('<font size="3" style="font-family: 宋体; font-size: 12px;">','').replace('</b>','').replace('<b>','').replace('\u3000','').replace('&nbsp','')
        company_description_list.append(str(com_info))
        regex_stills_required = '<div class="pos-ul">(.*?)</div>'
        stills_required = re.findall(regex_stills_required, company_html, re.M | re.S)

        stills_info = stills_required[0].replace('<p>','').replace('</p>', '').replace('&nbsp;', '').replace('</span>', '').replace('<br/>', '').replace(' \xa0','').replace('\n','')
        stills_required_list.append(str(stills_info))
        time.sleep(1)

    return company_welfare_list,company_location_list,stills_required_list,company_description_list



def info_dict():
    info_port = info_list()
    info_re = info_list2()
    salary = pd.DataFrame({'薪资':info_port[0]})
    city = pd.DataFrame({'城市':info_port[1]})
    skill_type = pd.DataFrame({'技能类型':info_port[2]})
    company_name = pd.DataFrame({'公司名称':info_port[3]})
    company_size = pd.DataFrame({'公司规模':info_port[4]})
    company_type = pd.DataFrame({'公司类型':info_port[5]})
    edu_required = pd.DataFrame({'学历要求':info_port[6]})
    esperiende_required = pd.DataFrame({'经验要求':info_port[7]})
    company_welfare = pd.DataFrame({'公司福利':info_re[0]})
    company_location = pd.DataFrame({'工作地点':info_re[1]})
    stills_repuired = pd.DataFrame({'技能要求':info_re[2]})
    print(stills_repuired[:3])
    company_description = pd.DataFrame({'公司描述':info_re[3]})
    df = pd.concat([salary,city,skill_type,company_name,company_size,company_type,edu_required,esperiende_required,company_welfare,company_location,stills_repuired,company_description],axis = 1)
    df.to_csv(r'zhaopin.csv',encoding = 'gb18030')
info_dict()
