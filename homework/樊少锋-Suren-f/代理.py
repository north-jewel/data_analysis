import requests
from bs4 import BeautifulSoup
import time
import random

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}

def xici_ip(page):
    for num_page in range(1,page+1):
        url_part = "http://www.xicidaili.com/nn/" # 爬取西刺代理的IP，此处选的是国内https
        url = url_part + str(num_page)  # 构建爬取的页面URL
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text,'lxml')
            trs = soup.find_all('tr')
            for i in range(1,len(trs)):
                tr = trs[i]
                tds = tr.find_all('td')
                ip_item = tds[1].text + ':' + tds[2].text
                # print('抓取第'+ str(page) + '页第' + str(i) +'个：' + ip_item)
                with open('get_xici_ip.txt', 'a', encoding='utf-8') as f:
                    f.writelines(ip_item + '\n')
                # time.sleep(1)
            return ('存储成功')

def get_ip():
    with open('get_xici_ip.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return random.choice(lines)

def check_ip():
    proxies = {'HTTPS': 'HTTPS://' + get_ip().replace('\n', '')}
    try:
        r = requests.get('http://httpbin.org/ip', headers=headers, proxies=proxies, timeout=10)
        if r.status_code == 200:
            return proxies
    except Exception as e:
        print(e)

def main():
    for i in range(30,101):
        xici_ip(i) # 抓取第一页，一页100个url
        print(i)
    try:
        return check_ip()
    except Exception as e:
        print(e)
        check_ip()

if __name__ == '__main__':
    main()
