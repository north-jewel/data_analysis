from bs4 import BeautifulSoup
import bs4
import requests
import pandas as pd
import time

def search(keyword,page):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=21&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(keyword,page)
    html = requests.get(url,headers = headers)
    html.encoding = 'gbk'
    return html.text

# html = search('python','1')
def page_all(html):
    soup = BeautifulSoup(html, 'html.parser')
    gong_p = int(soup.select('.dw_page')[0].select('.td')[0].text.replace('共', '').replace('页，到第', '')) + 1
    return gong_p
def info(html):
    soup = BeautifulSoup(html, 'html.parser')

    zhiwei = soup.select('.t1')
    url = zhiwei[1].a['href']
    gongsi = soup.select('.t2')
    didian = soup.select('.t3')
    xinzi = soup.select('.t4')
    shijian = soup.select('.t5')

    job_required = []
    url = []
    company_name = []
    city = []
    salary = []
    publish_data = []

    for i in range(1,51):
        job_required.append(zhiwei[i].text.strip())
        url.append(zhiwei[i].a['href'])
        company_name.append(gongsi[i].text.strip())
        city.append(didian[i].text.strip())
        salary.append(xinzi[i].text.strip())
        publish_data.append(shijian[i].text.strip())

    df = pd.DataFrame({'job_required': job_required,
                       'url': url,
                       'company_name': company_name,
                       'city': city,
                       'salary': salary,
                       'publish_data': publish_data})

    return  df

html = search('python', 1)
gong_p = page_all(html)
print('一共{}页'.format(gong_p))
header = True
for p in range(1,gong_p):
    time.sleep(5)
    if p > 1:
        html = search('python', p)
        header = False
    df = info(html)
    print('第{}页共爬取到{}条数据'.format(p,len(df)))
    df.to_csv('前程无忧.csv',header=header,mode = 'a',index = None)