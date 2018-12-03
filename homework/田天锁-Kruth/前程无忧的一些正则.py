import re
import requests
headers = {
        'Host': 'search.51job.com',
        'Upgrade - Insecure - Requests': '1',
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.67Safari / 537.36'
}

#url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
'''
url_obj = requests.get(url,headers,timeout = 10)
url_obj.encoding = 'gbk'
#reg = re.compile(r'class="t1 ">.*? <a target="_blank" title=".*?" href="(.*?)".*? <span class="t2">', re.S)
reg = re.compile(r'class="t1 ">.*? <a target="_blank" title=".*?" href="(.*?)".*? <span class="t2">',re.S)
links = re.findall(reg,url_obj.text)

print(links)
'''
urls = 'https://jobs.51job.com/guangzhou/83260048.html?s=01&t=0'
urls_obj = requests.get(urls,headers,timeout = 10)
urls_obj.encoding = 'gbk'
#城市
'''
urls = 'https://jobs.51job.com/guangzhou/83260048.html?s=01&t=0'
urls_obj = requests.get(urls,headers,timeout = 10)
urls_obj.encoding = 'gbk'
reg_city = re.compile(r'p class="msg ltype" title="(.*?)&nbsp;')
city = re.findall(reg_city,urls_obj.text)
print(city)
'''
#技能类别
'''
urls = 'https://jobs.51job.com/guangzhou/83260048.html?s=01&t=0'
urls_obj = requests.get(urls,headers,timeout = 10)
urls_obj.encoding = 'gbk'
reg_skill_type = re.compile(r'h1 title="(.*?)">',re.S)
skill_type = re.findall(reg_skill_type,urls_obj.text)
print(skill_type)
'''
#公司名
'''
urls = 'https://jobs.51job.com/guangzhou/83260048.html?s=01&t=0'
urls_obj = requests.get(urls,headers,timeout = 10)
urls_obj.encoding = 'gbk'
reg_company_name = re.compile(r'a href=".*?" target="_blank" title="(.*?)" class="catn"')
company_name = re.findall(reg_company_name ,urls_obj.text)
print(company_name)
'''
#公司规模
'''
reg_company_size = re.compile(r'p class="at" title="(.*?)"><span class="i_people"')
company_size = re.findall(reg_company_size,urls_obj.text)
print(company_size)

'''
#公司类型
'''
#reg_company_type = re.compile(r'span class="i_trade"></span><a href=".*?">(.*?)</a><a href=".*?">(.*?)</a',re.S)
#reg_company_type = re.compile('p class="at" title="(.*?)"><span class="i_trade"',re.S)
#reg_company_type = re.compile(r'p class="at" title="(.*?)"><span class="i_trade"',re.S)
#reg_company_type = re.compile(r'<div class="com_tag"><p class="at" title=".*?"><span class="i_flag"></span>.*?</p><p class="at" title=".*?"><span class="i_people"></span>.*?</p><p class="at" title="(.*?)"><span class="i_trade',re.S)
#reg_company_type = re.compile(r'span class="i_trade"></span>[/s/S]<a href=".*?">(.*?)</a,',re.S)
#reg_company_type = re.compile(r'span class="i_people"></span>.*?</p><p class="at" title="(.*?)"><span class="i_trade"',re.S)
reg_company_type = re.compile(r'<p class="at" title="(.*?)">\s*?<span class="i_trade">')
company_type = re.findall(reg_company_type,urls_obj.text)
print(company_type)

'''

#公司地点

'''
reg_company_location = re.compile('span class="label">上班地址：</span>(.*?)\s*?</p')
company_location = re.findall(reg_company_location,urls_obj.text)
print(company_location)
#reg_company_location = re.compile('')
'''
#薪资
#reg_skill_type = re.compile(r'h1 title=".*?">.*?<strong>(.*?)</strong>', re.S)


#职位要求:
	#技能要求
'''
reg_skills_required = re.compile(r'class="bmsg job_msg inbox">\s*?<p>(.*?)\s*?<div class="mt10',re.S)

skills_required = re.findall(reg_skills_required,urls_obj.text)
print(skills_required)
'''

#学历要求
reg_edu_required = re.compile('class="msg ltype" title=".*?&nbsp;&nbsp;|&nbsp;&nbsp;.*?&nbsp;&nbsp;|&nbsp;&nbsp;(.*?)&nbsp;&nbsp;|')
edu_required = re.findall(reg_edu_required,urls_obj.text)
print(edu_required)




















