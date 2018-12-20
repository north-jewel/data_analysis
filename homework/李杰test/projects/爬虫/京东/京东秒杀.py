import requests
import requests,json,base64,re
url = 'https://wqcoss.jd.com/mcoss/secondkill/show?callback=jsonCBSeckillItem&pretime=&count=60&offset=0&actid=114299&ctx=&g_tk=5381&g_ty=ls'
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Mobile Safari/537.36'}
response = requests.post(url,headers=headers)
info = response.text
lis = []
for i in info:
    lis.append(i)

goods = 'skuname(.*?),'
time = 'poolname(.*?),'
price = 'chprice(.*?),'

count = re.findall(goods,info)
count1 = re.findall(time,info)
count2 = re.findall(price,info)
for i in range(len(count)):
    print(count[i].replace('":"','').replace('"',''))
    print(count1[i].replace('":"','').replace('"',''))
    print(count2[i].replace('":"','').replace('"',''))
