import requests
import random
import time
import pandas as pd

#请求页面，获取页面数据
def GetHtml(start):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    url = 'https://fe-api.zhaopin.com/c/i/sou?start='+str(start)+'&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&sortType=publish&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&lastUrlQuery=%7B%22jl%22:%22538%22,%22kw%22:%22%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88%22,%22kt%22:%223%22%7D&_v=0.79472005&x-zp-page-request-id=15621c9c7abd41679024b2ac5cf0f992-1541566903009-311773'
    response = requests.get(url,headers=headers)
    html = response.json()
    return html

#获取一页的职位信息
def Get_One_Page_Post(html):

    datas = html['data']['results']
    jobs = pd.DataFrame(columns = ['city','compay','company_type','company_size','job_required','salary','experience_required','edu_required','company_welfare','release_date','positionURL'])
    for i in range(len(datas)):
        city = datas[i]['city']['display']
        company = datas[i]['company']['name']
        company_type = datas[i]['company']['type']['name']
        company_size = datas[i]['company']['size']['name']
        job_required = datas[i]['jobName']
        salary = datas[i]['salary']
        experience_required = datas[i]['workingExp']['name']
        edu_required = datas[i]['eduLevel']['name']
        company_welfare = datas[i]['welfare']
        release_date = datas[i]['createDate']
        positionURL = datas[i]['positionURL']
        job = pd.DataFrame([city,company,company_type,company_size,job_required,salary,experience_required,edu_required,company_welfare,release_date,positionURL]).T
        job.columns = ['city','compay','company_type','company_size','job_required','salary','experience_required','edu_required','company_welfare','release_date','positionURL']
        jobs = pd.concat([jobs,job])
        print(jobs)
    return jobs
#保存数据到excel
def Save():
    jobs = []
    i = 1
    while True:
        print('正在爬取第'+str(i)+'页,请稍后......')
        start = 60*(i-1)
        html = GetHtml(start)
        onepagejobs = Get_One_Page_Post(html)
        jobs.append(onepagejobs)
        s = random.randint(1,5)
        time.sleep(s)#设置睡眠时间,防止反扒
        i+=1
        if (len(jobs)==1):
            print('全部爬取完毕！')
            break
    content = pd.concat(jobs)
    content.to_excel('智联招聘测试.xlsx',index=None)

Save()