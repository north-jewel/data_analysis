import requests,re

def boos():
    url='https://www.zhipin.com/job_detail/?query=python&scity=101010100&industry=&position='
    proxies={'http':'118.182.33.6','https':'118.182.33.6'}
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    html=requests.get(url,headers = header,proxies=proxies).text
    skill_type_re='<div class="job-title">(.*?)</div>'
    skill_type=re.findall(skill_type_re,html)
    company_location_re='<p>(.*?)<em class="vline"></em>(.*?)<em class="vline"></em>(.*?)</p >'
    company_location=re.findall(company_location_re,html)
    salary_re='<span class="red">(.*?)</span>'
    salary=re.findall(salary_re,html)
    job_required_re='<a href="(.*?)" data-jid=".*?" data-itemid="\d*?" data-lid=".*?" data-jobid=".*?" data-index="\d*?" ka=".*?" target="_blank">'
    job_required=re.findall(job_required_re,html)
    a = len(job_required)
    for i in range(a):
        b  = 'https://www.zhipin.com'+job_required[i]
        html_1=requests.get(b).text
        description_re='<div class="text">(.*?)</div>'
        description=re.findall(description_re,html_1,re.S)
        print(description)
        
        
        
        
    #print(job_required)
    #print(salary)
    #print(company_location)
    #print(skill_type)
    #print(html)
        
boos()
