from bs4 import  BeautifulSoup
import requests
from method import method
# m=method()
# url='https://jobs.51job.com/beijing-dcq/108180547.html?s=01&t=0'
# ojb=requests.get(url)
# ojb.encoding='gbk'
# text=ojb.text
# m.writes('h52.txt',text,'gbk')
'''
soup=BeautifulSoup(open('./h52.txt',encoding='gbk'),'html.parser')
title_name=soup.title.string
print(title_name)
title=soup.select('.cn > h1')[0].get('title')
print(title)
wage=soup.select('.cn > strong')[0].string
print(wage)
company=soup.select('.cname > a')[0].get('title')
print(company)
details=soup.select('.cn > p  ')[1].get('title')
print(details)
position=soup.select('div.bmsg.job_msg.inbox > p')
position_list=[str(i).replace('</p>','').replace('<p>','').replace('<br/>','') for i in position]
print(position_list)
boon=soup.select('div.t1 > span')
boon_list=[i.string for i in boon]
print(boon_list)
company_content=soup.select('div.tmsg.inbox')[0].text.strip()
print(company_content)
site=soup.select('div.bmsg.inbox > p.fp')[0].text.strip()
print(site)
'''
soup=BeautifulSoup(open('./h5.txt',encoding='utf-8'),'html.parser')
content=soup.select('p.t1 > span  > a ')
print(content)