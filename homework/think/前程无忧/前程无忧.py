import requests
from method import method
import re
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
city='北京,广州'
url='https://search.51job.com/list/010000%252C060000,000000,0000,00,9,99,%2520,2,1.html'
meth=method()
def search(str_,city=None):
    chines=meth.isChinese(str_)
    english=meth.isEnglish(str_)
    if chines:
        chines=meth.decods(meth.decods(chines))
    if city:
        city_list=meth.add_city(city)
        city_code=meth.convert(meth.read_file(r'./config/地点.txt',arg='gbk',evals=True))
        new_city=''
        #print(city_code)
        list_=['%252C']*(len(city_list)-1)
        list_.append('')
        counts=0
        for i in city_list:
            if city_code[i]:
                new_city+=city_code[i]+list_[counts]
                counts+=1
            else:
                print('城市不存在')
                break
    else:
        new_city='010000'
    return 'https://search.51job.com/list/{1},000000,0000,00,9,99,{0},2,1.html'.format(chines+english,new_city,)


def request(url):
    heads={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    obj=requests.get(url,headers=heads)
    obj.encoding='gbk'
    text=obj.text
    #text=meth.read_file(r'./h5.txt')
    job_re='<a target="_blank" title=".*?" href="(.*?)" onmousedown="">'
    pages_re=' <span id="rtPrev" class="dicon Dm"></span><span class="dw_c_orange">1</span>(.*?)<a'
    job=re.findall(job_re,text)
    try:
        pages=re.findall(pages_re,text,re.S)[0].replace('/','')
    except:
        pages=None
    print(job)
    print(pages)
    return pages,job
#request(url)

def details(url):
    heads = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    obj = requests.get(url, headers=heads)
    obj.encoding = 'gbk'
    text = obj.text
    soup = BeautifulSoup(text, 'html.parser')
    title_name = soup.title.string
    #print(title_name)
    title = soup.select('.cn > h1')[0].get('title')
    #print(title)
    wage = soup.select('.cn > strong')[0].string
    #print(wage)
    company = soup.select('.cname > a')[0].get('title')
    #print(company)
    details = soup.select('.cn > p  ')[1].get('title')
    #print(details)
    position = soup.select('div.bmsg.job_msg.inbox > p')
    position_list = [str(i).replace('</p>', '').replace('<p>', '').replace('<br/>', '') for i in position]
   #print(position_list)
    boon = soup.select('div.t1 > span')
    boon_list = [i.string for i in boon]
    #print(boon_list)
    company_content = soup.select('div.tmsg.inbox')
    company_content_list=[i.text.strip() for i in company_content]
    #print(company_content_list)
    site = soup.select('div.bmsg.inbox > p.fp')
    site_list=[i.text.strip() for i in site]
    #print(site_list)
    new_dict={
        'order': [0],
        'url':'',
        'city':[city],
        'company_name': [company],
        'wage':wage,
        'company_size':  [meth.l_str(company_content_list).replace('\xa0','')],
        'work_type': [title],
        'company_type': [title_name],
        'company_location' : [site_list[0]],
        'job_required' : [meth.l_str(position_list).replace('<b></b>','').replace('<i></i>','').replace('<u></u>','').replace('<sub></sub>','').replace('<sup></sup>','').replace('<strike></strike>','')],
        'company_welfare': [meth.l_str(boon_list)],
    }
    #print(new_dict)
    return new_dict


#details(url='https://jobs.51job.com/guangzhou/108381415.html?s=01&t=0')

# a=search('python','北京,广州')
# z,list1=request(a)
# for i in range(2,int(z)+1):
#     url='https://search.51job.com/list/010000%252C030200,000000,0000,00,9,99,python,2,{}.html'.format(i)
#     try:
#         a,b=request(url)
#     except:
#         pass
#     #time.sleep(random.randrange(1,10))
#     list1.append(b)
# meth.writes('detail.txt',str(list1))

a=meth.read_file('detail.txt',evals=True)
a=meth.split_(a)
counts=1
head=True
error=[]
for i in a:
    print(i)
    try:

        b=details(i)


        b['order']=counts
        b['url']=i
        counts += 1
    except Exception as e :
        error.append(e)
    if counts > 1:
        head=False

    b.to_csv('return.csv',header=head,method='a')

meth.writes('错误日志.txt',error)








