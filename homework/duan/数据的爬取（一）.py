import requests
import re
import numpy as np
import pandas as pd
import json

url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&at=8282c6f234e54198ad914368ec99e7f3&rt=605d9e4a4d574aa9b7ce400505902d60&_v=0.88860985&userCode=637838355&x-zp-page-request-id=a1ee7b5a4b194395a589222027b3faaf-1543569068541-36049'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
          'Referer':'https://www.zhaopin.com/'}
res = requests.get(url)
res.encoding = 'utf-8'
html = res.json()
info = html['data']['results']
info_dict = {}
dict_all = []
for i in range(len(info))[:2]:
    salary = info[i]['salary']
    info_dict['salary'] = salary
    city = info[i]['city']['items'][0]['name']
    info_dict['city'] = city
    skill_type = info[i]['jobType']['items'][1]['name']
    info_dict['skill_type'] = skill_type
    company_name = info[i]['company']['name']
    info_dict['company_name'] = company_name
    company_size = info[i]['company']['size']['name']
    info_dict['company_size'] = company_size
    company_type = info[i]['company']['type']['name']
    info_dict['company_type'] = company_type
    edu_required = info[i]['eduLevel']['name']
    info_dict['edu_required'] = edu_required
    esperiende_required = info[i]['workingExp']['name']
    info_dict['esperiende_required'] = esperiende_required
    company_welfare = info[i]['welfare']
    info_dict['company_welfare'] = company_welfare
    company_url = info[i]['positionURL']
    company_info = requests.get(company_url,headers = header)
    print(company_info)
    company_html = company_info.text
    #print(company_html)
    regex_location = '<p class="add-txt"><span class="icon-address"></span>(.*?)</p>'
    company_location = re.findall(regex_location,company_html)
    info_dict['company_location'] = company_location
    regex_stills_required = '<div class="intro-content">(.*?)</div>'
    stills_required = re.findall(regex_stills_required,company_html,re.M|re.S)[0].replace('<font>','').replace('</font>','').replace('<br>','').replace('<p>','').replace('</p>','').replace('<span>','').replace('</span>','')
    dict_all.append(stills_required)

    regex_job_required = '<div class="pos-ul">(.*?)</div>'
    job_required = re.findall(regex_job_required,company_html,re.M|re.S)[0].replace('<P>','').replace('</P>','').replace('&nbsp;','').replace('</span>','').replace('\n','')
    
    print(job_required)

    
#print(dict_all)
'''    
    for k,v in info_dict.items():
        if v == '':
            info_dict[k] = '######'
    
        if info_dict['company_welfare'] == []:
            info_dict['company_welfare'] = '########'
        if info_dict['company_location'] == []:
            info_dict['company_location'] = '######3'
    #print(info_dict)
    #print(i)
    dict_all[i] = info_dict
    #print(dict_all)

#print(dict_all)
    for a,b in dict_all.items(): 
        df = pd.DataFrame(b)
        df.to_csv(r'zhaopin.csv',encoding = 'gbk')
 '''   
    

