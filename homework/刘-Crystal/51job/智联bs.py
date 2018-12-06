import requests
from bs4 import BeautifulSoup
URL = 'https://jobs.zhaopin.com/CC152362529J00038850912.htm'
res = requests.get(URL)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'lxml')
title = soup.select_one('h1').text
company_name = [i.text for i in (soup.select('div.company > a'))]
saraly = soup.select('div.info-money > strong')
for i in saraly:
    saraly = i.text
info = soup.select('div.info-three > span')
city = info[0].text
experience = info[1].text
edu = info[2].text
wel = soup.select('div > span')
print(wel)