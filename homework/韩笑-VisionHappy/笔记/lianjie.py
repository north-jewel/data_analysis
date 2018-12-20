from bs4 import BeautifulSoup
import bs4
import requests

    
#将每一页得链接添加到url_list列表
    
url_1 = []
for i in range(1,117):
        url='https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(i)
        url_1.append(url)
def html_info(url_1):
        a = 1
        for i in url_1:
            html = requests.get(i)
            if html.status_code == 200:
                html.encoding = 'gbk'
                html_text = BeautifulSoup(html.text, 'lxml')
                print('正在爬取{}页'.format(a))                   
                position_name = html_text.find_all('p',class_ = 't1')
                for i in position_name:
                    with open('url.txt','a+') as f:
                        f.write(i.a.get('href'))
                        f.write('\n\n')
                    a += 1
html_info(url_1)

