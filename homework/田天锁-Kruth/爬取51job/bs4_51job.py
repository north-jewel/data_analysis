"""

@author:tts

@file: bs4_51job.py

@time: 2018/12/05

"""
import requests
from bs4 import BeautifulSoup

url = 'https://jobs.51job.com/guangzhou/83260048.html?s=01&t=0'
url_obj = requests.get(url)
url_obj.encoding='gbk'
url_text = url_obj.text
soup = BeautifulSoup(url_text,'html.parser')
#print(soup)
a = soup.find('div',class_='cn')
#print(a.h1)
#技能类别
#print(soup.find('h1').text.strip())
#print(soup.select_one('h1').get('title'))


#城市
#print(soup.find('p',class_='msg ltype').text.strip())
#print(soup.select_one('p.msg.ltype ').get('title'))

#公司名
#print(soup.find('div',class_='com_msg').text.strip())
#print(soup.select_one('div.com_msg > a > p').get('title'))

#公司规模
#print(soup.find_all('p','at')[1].text.strip())
#print(soup.select('div.com_tag > p:nth-of-type(2) ')[0].get('title'))

#公司类型
#print(soup.find_all('p','at')[2].text.strip())
#print(soup.select('div.com_tag > p:nth-of-type(3)')[0].get('title'))

#公司地点
#print(soup.find_all('p',class_='fp')[1].text.strip())
#print(soup.select('div.tCompany_main > div:nth-of-type(2) > div > p ')[0].text)

#薪资
#print(soup.find('div',class_='cn').find_all('strong')[0].text)
#print(soup.select('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > strong ')[0].text)


#技能要求
#print(soup.find('div',class_='bmsg job_msg inbox').text.strip())
#print(soup.select('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-of-type(1) > div')[0].text.strip())

#学历要求
#print(soup.find('p',class_='msg ltype'))
print()

#工作经验
print()
print()


#公司福利

#fuli = soup.find_all('span',class_='sp4')
#print(fuli)




