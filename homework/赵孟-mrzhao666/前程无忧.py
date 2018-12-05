from bs4 import BeautifulSoup
import bs4
import requests

url = 'https://jobs.51job.com/suzhou-gyyq/108977483.html?s=01&t=0'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

html = requests.get(url,headers = headers).text

soup = BeautifulSoup(html, 'html.parser')

info = soup.find_all(class_='cn')[0]
info.h1.text.strip()
info.strong.text
info.select('p')[0].select('.catn')[0].text.strip()
# info.select('p')[1].text.strip().split('\xa0\xa0|\xa0\xa0')
info.select('p')[1].text.strip().replace('\xa0\xa0|\xa0\xa0','/')

gongsi = soup.select('.tCompany_main')[0]
a = gongsi.select('.mt10')[0].select('p')[0].text.strip().replace('\t','').replace('\r','').replace('\n\n','|')
b = gongsi.select('.mt10')[0].select('p')[1].text.strip().replace('\n','|')
c = str(gongsi.select('.job_msg > p')).replace('[','').replace(']','').replace(',','').replace('<p>','').replace('</p>','|').split('<br/>')
