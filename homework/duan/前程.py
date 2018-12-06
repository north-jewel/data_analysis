from bs4 import BeautifulSoup
import requests
import time
import numpy
start_url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html? lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-    1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
urls = []
for i in range(1,116):
    url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{}.html'.format(i)
    #print(url)
    urls.append(url)
#print(urls)

#解析首页的url
def get_content(url):
    aaa = 1
    for i in url:
        print(aaa)
        res = requests.get(i) #验证第一页
        if res.status_code == 200:
            res.encoding = 'gbk'
            soup = BeautifulSoup(res.text, 'html.parser')
            # resultList > div:nth-child(4) > span.t2 > a
            a = soup.select('#resultList > div.el > span > a')
            for i in a:
                company_name = i.text
                #print(company_name)
            b = soup.select('#resultList > div.el > p > span > a')
            with open('url.txt','a+') as f:

                #f.write('滴{}也'.format(aaa))
                #f.write('\n')
                for x in b:
                    num = b.index(x)
                    url_fenzhi = x['href']
                    res = requests.get(url_fenzhi)
                    soup = BeautifulSoup(res.text, 'html.parser')
                    div = soup.find(class_='tHeader tHjob')
                    company_name = soup.select_one('a.com_name')
                    company_type = soup.select('p.at')[0].text
                    company_size = soup.select('p.at')[1].text

                    company_location = soup.find(class_='bmsg inbox').text

                    job_required = soup.select('div.bmsg > p')[0].text.strip().replace('工作描述:','').replace('岗位职责：','')
                    company_discription = soup.select('div.tmsg')[0].text.strip()
                    skill_type = soup.select_one('p.fp').text
                    company_werfile = soup.find('div', class_='t1').text.strip()
                    salary = soup.find('div', class_='cn').strong.text
                    job_type = div.h1.get('title')
                    #print(wel)
                    print(job_required)
                    #print(skill_type)

                    #f.write('\n')
                    #f.write(url_fenzhi)
                    #f.write('\n')


            aaa += 1
            contentuls = soup.select('#resultList > div > p > span > a')
            #print(contentuls[0].text.strip())
            salary = soup.select('#resultList > div > span.t4')
            #print(salary)
            time.sleep(2)
get_content(urls[:2])