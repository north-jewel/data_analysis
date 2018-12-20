import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://price.pcauto.com.cn/top/oil/s1-t3.html'
url_obj = requests.get(url)
url_obj.encoding = 'gbk'
url_text = url_obj.text
soup = BeautifulSoup(url_text,'html.parser')
pages = soup.find('ul',class_="").find_all('a')
panduan = soup.find('div', class_="pcauto_page")




car_url = []
for i in pages:
    # print(i)
    # print(i.get('href'))
    # print(i.text.strip())
    # car_url[i.text.strip()] = 'https://price.pcauto.com.cn'+i.get('href')
    car_url.append('https://price.pcauto.com.cn'+i.get('href'))
# for x,y in car_url.items():
#     car_obj = requests.get(y)
#     car_obj.encoding = 'gbk'
#     car_text = car_obj.text
#     soups = BeautifulSoup(car_text, 'html.parser')
#     a = soups.find('div', class_="pcauto_page")
#     #class="c"
#     if a ==None:#证明只有一页
#         info_len=len(soups.find_all('div', class_='info'))
#         print(y)
#         print(info_len)
#         #循环len 获取相应的数据 写入到字典里再写入到csv中
#     else:
#         pass
# print(car_url)

# carname = soup.select('#JboxRank > div.tbA > ul > li:nth-of-type(1) > div.info > p.sname > a')
carname = []
juti_car_url=[]
sname = soup.find_all('p',class_='sname')
# print(sname)
for i in sname:
    carname.append(i.find('a').text.strip())
    juti_car_url.append(i.find('a').get('href'))
# print(carname)
# print(juti_car_url)
# red = soup.find('p',class_='col')
# print(red)

    # if x == '小型车':
    #     print(y)


#juti_url = 'https://price.pcauto.com.cn/sg3264/'
juti_url = 'https://price.pcauto.com.cn/sg903/'
juti_url_obj = requests.get(juti_url)
juti_url_obj.encoding='gbk'
juti_url_text = juti_url_obj.text
soup = BeautifulSoup(juti_url_text,'html.parser')
gearbox = soup.select('#detail > div.box-b > div.infor > div.price > ul > li:nth-of-type(2) > p:nth-of-type(1) > em')[0].text
print(gearbox)
cartypes = soup.select('#detail > div.box-b > div.infor > div.price > ul > li:nth-of-type(2) > p:nth-of-type(2) > em > a:nth-of-type(1)')
cartype = cartypes[0].text.strip()
# print(cartype)
rank = soup.select('#strengthProcess > p')[0].text.strip().replace('查看详情>>','')
carstrength = soup.find('p',class_='score').text.strip()
configuration = soup.select('#strengthProcess > div.processBarWrap > div:nth-of-type(1) > div > p')[0].text.strip()
major = soup.select('#strengthProcess > div.processBarWrap > div:nth-of-type(2) > div > p')[0].text.strip()
ownerevaluate = soup.select('#strengthProcess > div.processBarWrap > div:nth-of-type(3) > div > p')[0].text.strip()
price = soup.select('#strengthProcess > div.processBarWrap > div:nth-of-type(4) > div > p')[0].text.strip()

