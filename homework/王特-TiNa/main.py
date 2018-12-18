import re,requests,time,random,urllib
from bs4 import BeautifulSoup

useragent = [
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

with open('Ip.txt','r',encoding='utf-8') as ip:
    ip_list = ip.readlines()

class wiwj:

    def __init__(self):
        self.url =  'https://bj.5i5j.com/zufang'
        self.selp = random.randint(10,20)
        self.ip_dic = {'http':random.choice(ip_list)}
        self.header = {'User-Agent':useragent}

    # 返回100页的url链接
    def generate_urls(self):
        urls = []
        for i in range(1,101):
            urls.append('https://bj.5i5j.com/zufang/n{}/'.format(i))
        return urls

    # 传入url，解析网页，返回 s
    def get_page_html(self,url):
        print('开始{}秒睡眠...'.format(self.selp))
        time.sleep(self.selp)
        html = requests.get(url,self.header)
        s = BeautifulSoup(html.text,'html.parser')
        return s

    # 传入网页的url，返回房子的url链接，存储到url.txt中
    def parse_homepage(self,page_url):
        house_urls = []
        print(page_url)
        s = self.get_page_html(page_url)
        print('A')
        try:
            url_list = s.find_all('h3',class_ ="listTit")
            print(url_list[0])
        except Exception as e:
            print('B')
            try:
                page_url = s.find('script').text.split("'")[1]
            except Exception as e:
                page_url = s.find('div',class_='p-more').find('p').find('span').text
                s = self.get_page_html(page_url)
        print('C')
        print(s)
        url_tag = s.find_all('h3', class_="listTit")
        print('D')
        print(url_tag)
        print('E')
        a = 1
        for url_a in url_tag:
            house_url = url_a.find('a').get('href')
            house_url = self.url + house_url
            print(house_url)
            print('开始存储第{}条信息'.format(a))
            house_urls.append(house_url)
            with open('url.txt','a',encoding='utf-8') as f:
                f.write(house_url)
                f.write('\n')
            print('存储完成！')
            print('\n')
            a+=1
        return house_urls

    # 输入解析的网页源代码，返回房屋信息的字典
    def parse_house(self,s,house_url):
        print(house_url)
        url_info_dic = {}
        houskeyword = s.find('h1').text
        house_info = s.find_all('p', class_="jlinfo")
        rent = house_info[0].text
        housetype = house_info[1].text
        area = house_info[2].text
        paymen = house_info[3].text
        record = {'time': house_info[4].text, 'zuijin7': house_info[5].text, 'zuijin30': house_info[6].text}

        li_info = s.find('div', class_="zushous").find_all('li')
        house_dic = {'小区': 'district', '楼层': 'tage', '朝向': 'orientation', '装修': 'decoration', '楼型': 'towertype',
                     '供暖': 'heating', '出租方式': 'rentway', '看房时间': 'looktime', '商圈': 'tradingarea', '地铁': 'metor'}
        tag_house_dic = {'district': '', 'tage': '', 'orientation': '', 'decoration': '', 'towertype': '',
                         'heating': '', 'rentway': '', 'looktime': '', 'tradingarea': '', 'metor': ''}
        for tag in li_info:
            tag_info, tag_ = tag.text.split('：')[0], tag.text.split('：')[1]
            if tag_info in house_dic.keys():
                tag_house_dic[house_dic[tag_info]] = tag_

        house_info2 = s.find('div', class_="fysssty").find_all('li')
        housingfacilities = ','.join([tag.text for tag in house_info2])

        developers = s.find('li', class_="w100").text.replace('开发商', '')

        url_info_dic['houskeyword'] = houskeyword
        url_info_dic['rent'] = rent
        url_info_dic['housetype'] = housetype
        url_info_dic['area'] = area
        url_info_dic['paymen'] = paymen
        url_info_dic['record'] = record
        url_info_dic.update(tag_house_dic)
        url_info_dic['housingfacilities'] = housingfacilities
        url_info_dic['developers'] = developers
        url_info_dic['pageurl'] = house_url

        print(url_info_dic)

        with open('huoseinfo.txt', 'a', encoding='utf-8') as f:
            f.write(repr(url_info_dic))
            f.write('\n')
        print('第{}条信息存储完成！！'.format(a + 1))
        print('\n')
        a += 1

    # 调动方法，抓取信息
    def startspider(self,house_urls):
        a = 0
        for house_url in house_urls:
            s = self.get_page_html(house_url)
            print('第{}条数据开始'.format(a + 1))
            try:
                houskeyword = s.find('h1').text
            except Exception as e:
                house_url = s.find('script').text.split("'")[1]
                s = self.get_page_html(house_url)
            self.parse_house(s,house_url)
        print('end!')



if __name__ == '__main__':
    w = wiwj()
    urls = w.generate_urls()
    b = 1
    for u in urls:
        print('开始第{}页'.format(b))
        house_urls = w.parse_homepage(u)
        w.startspider(house_urls)
        print('第{}页爬取完成！'.format(b))
        b += 1
    # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
    # url = 'https://bj.5i5j.com/zufang/n8/'
    # html = requests.get(url,header)
    # s = BeautifulSoup(html.text,'html.parser')
    # print(s)
    # url_list = s.find_all('h3', class_="listTit")
    # print(url_list)
