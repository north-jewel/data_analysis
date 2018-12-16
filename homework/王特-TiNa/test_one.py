import re,requests,time,random,urllib
from bs4 import BeautifulSoup

cookie = '''morCon=open; _ga=GA1.2.379192257.1542712657; yfx_c_g_u_id_10000001=_ck18112019173715231181353072907; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3A%3A%3A%3A%3A%3A%3Aloft%25E5%2585%25AC%25E5%25AF%2593%25E5%2587%25BA%25E7%25A7%259F%3A%3Abj.5i5j.com%3A%3A93044729240%3A%3A%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E9%2595%25BF%25E5%25B0%25BE%25E8%25AF%258D%3A%3A%25E5%2585%25AC%25E5%25AF%2593%25E7%259B%25B8%25E5%2585%25B3%3A%3A36%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2Fzufang%2F; PHPSESSID=m72t4nrnke25thnn7oota0psam; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1543993285,1543993344,1544055483,1544511670; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Abj.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=; zufang_cookiekey=%5B%22%257B%2522url%2522%253A%2522%252Fzufang%252F_%2525E5%25258C%252597%2525E4%2525BA%2525AC%253Fzn%253D%2525E5%25258C%252597%2525E4%2525BA%2525AC%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E5%258C%2597%25E4%25BA%25AC%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fzufang%252F_loft%253Fzn%253Dloft%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522loft%2522%252C%2522total%2522%253A%25220%2522%257D%22%5D; _gid=GA1.2.1758329371.1544934604; _Jo0OQK=5511644D5A7C9F5387A93B61DDF15A2291AB14F2C013104941683015357F745DFCD6C0A0D62CABA1B7B5254C8393402BA5857CC3933187CF09B51D03F3D6BC7AA41C57212F12283777C840763663251ADEB840763663251ADEBEDFEE6E5C9D6B2DC9C0616B90758FB61GJ1Z1WQ==; domain=bj; zufang_BROWSES=90141601%2C41957036%2C41957027%2C41959873%2C42050674%2C42049583%2C41984277%2C41931116%2C41800399%2C41616927%2C42100766%2C42068241%2C42020981%2C42082924%2C41809226%2C41933675%2C42119308; yfx_f_l_v_t_10000001=f_t_1542712657502__r_t_1544934615090__v_t_1544956562672__r_c_5; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1544957491'''


headers = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
]

with open('Ip.txt', 'r', encoding='utf-8') as f:
    f_list = f.readlines()

slep = random.randint(0, 5)
ip = random.choice(f_list)
header = random.choice(headers)
Ip_dic = {'http': ip}
time.sleep(slep)

url = 'https://bj.5i5j.com/zufang/n1'
html = requests.get(url, headers = {'User-Agent':header}, proxies=Ip_dic)
s = BeautifulSoup(html.text, 'html.parser')

name = s.find_all('h3',class_='listTit')[0].find('a')
url_ = name.get('href')
houskeyword = name.text
with open('url_info.txt','a',encoding='utf-8') as f:
    f.write('https://bj.5i5j.com'+url_)
    f.write('\n')

# rent = s.find_all('p',class_="redC")[0].find('strong').text

slep1 = random.randint(0,5)
ip1 = random.choice(f_list)
header1 = random.choice(headers)
Ip_dic1 = {'http':ip1}
time.sleep(slep1)
html = requests.get(housurl, proxies=Ip_dic1,headers = {'User-Agent':header1,'Cookie':cookie})
s = BeautifulSoup(html.text, 'html.parser')

house_info = s.find_all('p',class_="jlinfo")
rent = house_info[0].text
housetype = house_info[1].text
area = house_info[2].text
paymen = house_info[3].text
record = {'time':house_info[4].text,'zuijin7':house_info[5].text,'zuijin30':house_info[6].text}

house_info1 = s.find('div',class_="zushous")
li_info = house_info1.find_all('li')
district = li_info[0].text
tage = li_info[1].text
orientation = li_info[2].text
decoration = li_info[3].text
towertype = li_info[4].text
heating = li_info[5].text
rentway = li_info[6].text
looktime = li_info[7].text
tradingarea = li_info[8].text
metor = li_info[9].text
# print(district)
# print(tage)
# print(orientation)
# print(decoration)
# print(towertype)
# print(heating)
# print(rentway)
# print(looktime)
# print(tradingarea)
# print(metor)

house_info2 = s.find('div',class_="fysssty").find_all('li')
housingfacilities = ','.join([tag.text for tag in house_info2])
# print(housingfacilities)

developers = s.find('li', class_="w100").text.replace('开发商','')
# print(developers)

# houskeyword = s.find('h1').text
# print(houskeyword)

