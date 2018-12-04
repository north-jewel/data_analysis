import requests
import random
import time
import pandas as pd

#请求页面，获取页面数据
def GetHtml(start,city=None,post=None):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId={}&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3&_v=0.79624471&x-zp-page-request-id=09ba09b0d18f41a08d05af2bbfffdbae-1543922403256-92428'.format(start,city,post)
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
        #print(jobs)
    return jobs
#保存数据到excel
def Save():
    city = input('请输入你要查询的城市:')
    post = input('请输入你要查询的职位:')
    jobs = []
    i = 1
    while True:
        print('正在爬取第{}页,请稍后......'.format(i))
        start = 60*(i-1)
        html = GetHtml(start,city,post)
        onepagejobs = Get_One_Page_Post(html)
        jobs.append(onepagejobs)
        s = random.randint(1,5)
        time.sleep(s)#设置睡眠时间,防止反扒
        i+=1
        if (len(jobs)==3):
            print('全部爬取完毕！')
            break
    content = pd.concat(jobs)
    content.to_excel('智联招聘测试.xlsx',index=None)

if __name__ == '__main__':
    Save()