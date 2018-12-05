import re,requests
from bs4 import BeautifulSoup

url = 'https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0'
html = requests.get(url).text
s = BeautifulSoup(html,'html.parser')

# 职位要求
job_required = s.select_one('div.cn > h1')
job_required = job_required.text.lstrip()
print(job_required)

# 公司名称
Company_name = s.select_one('p.cname > a.catn')
Company_name = Company_name.text.lstrip()
print(Company_name)

# 薪资
salary = s.select_one('div.cn > strong')
salary =  salary.text.lstrip()
print(salary)

# 公司类型 公司大小
Company_info = s.find_all('p',class_='at')
Company_info_list = []
for i in Company_info:
    Company_info_list.append(i.text)
Company_type = Company_info_list[0]
Company_size = Company_info_list[1]
print(Company_type)
print(Company_size)

# 办公地址
Company_location = s.find_all('p',class_='fp')
Company_location = Company_location[1].text
print(Company_location)

# 公司福利
Company_welfare_list = s.find_all('span',class_='sp4')
Company_welfare_str = ''
for i in Company_welfare_list:
    Company_welfare_str += '{},'.format(i.text)
print(Company_welfare_str)


# 公司简介
Company_description = s.find_all('div',class_ = 'tmsg inbox')
Company_description = Company_description[0].text.lstrip()
print(Company_description)

# 城市 工作经验 学历要求
experience_info = s.select_one('div.cn > p.msg.ltype').get('title').split('|')
City = experience_info[0].replace('\xa0','')
experience_required = experience_info[1].replace('\xa0','')
edu_required = experience_info[2].replace('\xa0','')
print(City)
print(experience_required)
print(edu_required)


# 技能要求
Skills_required = s.select('div.tCompany_main > div > div > p')
Skills_required_str = ''
for i in Skills_required:
    Skills_required_str += i.text
print(Skills_required_str)

# 职位要求 工作地址
# company_info = s.find_all('p',class_='fp')
# company_info_list = []
# for i in company_info:
#     company_info_list.append(i.text.replace('\r','').replace('\n','').replace('\t',''))
# job_required = company_info_list[0]
# company_location = company_info_list[1]
