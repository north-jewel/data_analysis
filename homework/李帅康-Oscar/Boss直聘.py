import requests
import re


url = 'https://www.zhipin.com/c101010100'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
params = {'query': 'python',
          'page':1,
          'ka':'page-next'}
res = requests.get(url,params = params,headers=headers)
html = res.text
#print(html)
#city_regex = ''
skill_type_regex = '<div class="job-title">(.*?)</div>'
company_name_regex = '<h3 class="name"><a href=".*?" ka="search_list_company_.*?_custompage" target="_blank">(.*?)</a></h3>'
company_description_regex = '<div class="text">(.*?)<\/div>'
company_location_regex = '<p>(.*?)<em class="vline">.*?</em>(.*?)</p>'
skills_required_regex = '<h3>职位描述</h3>.*?<div class="text">(.*?)<\/div>'
company_welfare_regex = '<span class="red">(.*?)</span>'
next_page_regex = '<a href="(.*?)" data-jid=".*?" data-itemid=".*?" data-lid=".*?" data-jobid=".*?" data-index=".*?" ka="search_list_.*?" target="_blank">'


skill_type = re.findall(skill_type_regex,html)  #技术类型
'''
['python', 'Python', 'Python讲师', 'python工程师', '高级Python', 'Python',
'''
company_location = re.findall(company_location_regex,html)
'''
[('北京 朝阳区 望京', '3-5年<em class="vline"></em>本科'), ('互联网', 'C轮<em class="vline"></em>1000-9999人'), 
'''
company_name = re.findall(company_name_regex,html)  #公司名
'''
['百度', '爱奇艺', '中公教育', '安知信息', '九易广告', '北京网信华创', '腾信软创', '今日头条', '中睿天下',
'''
company_description = ''  #公司简介
skills_required = ''  #技能要求
company_welfare = re.findall(company_welfare_regex,html)  #公司福利
'''
['15k-30k', '20k-40k', '15k-30k', '40k-50k', '35k-65k',
'''
next_page = re.findall(next_page_regex,html)
'''
['/job_detail/748e99363f53f18f1XJ52Nq_ElA~.html', '/job_detail/42db2756750a587b1XN539-_E1M~.html',
'''
company_info = []
for i in range(len(next_page)):
    url = 'https://www.zhipin.com'+next_page[i]
    res = requests.get(url,headers = headers)
    html_1 = res.text
    company_description = re.findall(company_description_regex,html_1,re.S)
    company_info.append(company_description)
print(company_info)


#city 城市  skill_type 技术类型 company_name 公司名  company_size 公司大小 company_type  公司类型
#company_description 公司简介  company_location 公司位置 job_required 职位要求 skills_required 技能要求
#edu_required 学历需求  experience_required  经验要求  company_welfare  公司福利
