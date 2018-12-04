import requests
from method import method
import re


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

#a=search('python','北京,广州')
def request(url):
    # heads={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    # obj=requests.get(url,headers=heads)
    # obj.encoding='gbk'
    # text=obj.text
    text=meth.read_file(r'./h5.txt')
    site_re='<span class="t3">(.*?)</span>'
    wage_re='<span class="t4">(.*?)</span>'
    time_re='<span class="t5">(.*?)</span>'
    job_re='<a target="_blank" title="(.*?)" href="(.*?)" onmousedown="">'
    company_re='<span class="t2"><a target="_blank" title="(.*?)" href=".*?">.*?</a></span>'
    pages_re=' <span id="rtPrev" class="dicon Dm"></span><span class="dw_c_orange">1</span>(.*?)<a'



    site=re.findall(site_re,text,re.S)
    wage = re.findall(wage_re, text, re.S)
    time = re.findall(time_re, text, re.S)
    job=re.findall(job_re,text)
    company=re.findall(company_re,text,re.S)
    pages=re.findall(pages_re,text,re.S)[0].replace('/','')
   # print(job)
    site.pop(0)
    # print(site)
    # print(wage)
    wage.pop(0)
    # print(time)
    time.pop(0)
    # print(company)
    # print(pages)
    # print(len(job))
    # print(len(site))
    new_dict={}
    new_list=list(zip(job,site,wage,time,company))
    for i in  range(len(new_list)):
        new_dict[i]=new_list[i]
    # print(new_dict)
    return new_dict,pages
request(url)












