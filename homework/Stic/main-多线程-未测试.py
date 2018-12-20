import re,requests,time,random,threading
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd

'''
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
]'''
class wiwj:
    # headers = { "User-Agent": UserAgent(verify_ssl=False).random} 随机伪装浏览器内核
    headers_list = []
    ua = UserAgent()
    ua_list = [ua.ie,ua.opera,ua.chrome,ua.firefox,ua.safari]
    for i in range(500):
        h = random.choice(ua_list)
        if h in headers_list:
            continue
        else:
            headers_list.append(h)
    cookie = '''morCon=open; _ga=GA1.2.379192257.1542712657; yfx_c_g_u_id_10000001=_ck18112019173715231181353072907; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3A%3A%3A%3A%3A%3A%3Aloft%25E5%2585%25AC%25E5%25AF%2593%25E5%2587%25BA%25E7%25A7%259F%3A%3Abj.5i5j.com%3A%3A93044729240%3A%3A%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E9%2595%25BF%25E5%25B0%25BE%25E8%25AF%258D%3A%3A%25E5%2585%25AC%25E5%25AF%2593%25E7%259B%25B8%25E5%2585%25B3%3A%3A36%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2Fzufang%2F; PHPSESSID=m72t4nrnke25thnn7oota0psam; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1543993285,1543993344,1544055483,1544511670; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Abj.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=; zufang_cookiekey=%5B%22%257B%2522url%2522%253A%2522%252Fzufang%252F_%2525E5%25258C%252597%2525E4%2525BA%2525AC%253Fzn%253D%2525E5%25258C%252597%2525E4%2525BA%2525AC%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E5%258C%2597%25E4%25BA%25AC%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fzufang%252F_loft%253Fzn%253Dloft%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522loft%2522%252C%2522total%2522%253A%25220%2522%257D%22%5D; _gid=GA1.2.1758329371.1544934604; _Jo0OQK=5511644D5A7C9F5387A93B61DDF15A2291AB14F2C013104941683015357F745DFCD6C0A0D62CABA1B7B5254C8393402BA5857CC3933187CF09B51D03F3D6BC7AA41C57212F12283777C840763663251ADEB840763663251ADEBEDFEE6E5C9D6B2DC9C0616B90758FB61GJ1Z1WQ==; zufang_BROWSES=90141601%2C41957036%2C41957027%2C41959873%2C42050674%2C42049583%2C41984277%2C41931116%2C41800399%2C41616927%2C42100766%2C42068241%2C42020981%2C42082924%2C41809226%2C41933675%2C42119308%2C42121020%2C42112658%2C42126149%2C42123933%2C41945589%2C42004739; domain=bj; _gat=1; yfx_f_l_v_t_10000001=f_t_1542712657502__r_t_1545008915992__v_t_1545012811034__r_c_6; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1545012812'''

    def __init__(self):
        self.s = requests.Session()
        # self.url_info = self.url_info()

    #'得到前100页的链接list'
    def url_info(self):
        page_url_list = []
        for i in range(1,101):
            page_url = 'https://bj.5i5j.com/zufang/n{}/'.format(i)
            page_url_list.append(page_url)
        return page_url_list

    #'输入一个主页html，得到这页所有的内容页url地址list'
    def url_content(self,html = None):
        url_content = []
        print('开始{}秒的睡眠。。'.format(10))
        time.sleep(10)
        s = BeautifulSoup(html.text, 'html.parser')
        try:
            url_list = []
            names = s.find_all('h3', class_='listTit')
            for i in range(len(names)):
                url_list.append(names[i].find('a').get('href'))
            for i in url_list:
                url_content.append('https://bj.5i5j.com' + i)
            # print(url_content)
            return url_content
        except:
            return s

    #'输入内容页html，返回内容dict'
    def huose_info(self,html,inde):
        url_info_dict = {}
        print('开始{}秒的睡眠。。'.format(10))
        s = BeautifulSoup(html.text, 'html.parser')
        # print(s)
        try:
            houskeyword = s.find('h1').text
            house_info = s.find_all('p', class_="jlinfo")
            rent = house_info[0].text
            housetype = house_info[1].text
            area = house_info[2].text
            paymen = house_info[3].text
            record = [house_info[4].text,house_info[5].text,house_info[6].text]

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
            url_info_dict['houskeyword'] = houskeyword
            url_info_dict['rent'] = rent
            url_info_dict['housetype'] = housetype
            url_info_dict['area'] = area
            url_info_dict['paymen'] = paymen
            url_info_dict['record'] = str(record)
            url_info_dict.update(tag_house_dic)
            url_info_dict['housingfacilities'] = housingfacilities
            url_info_dict['developers'] = developers
            # print(url_info_dict)
            thread_lock.acquire()
            df = pd.DataFrame(url_info_dict,index=[inde])
            df.to_csv('tpy2.csv',mode = 'a',header=False, encoding='utf-8-sig')
            thread_lock.release()
            return '{}写入'.format(houskeyword)
        except Exception as e:
            print(e)

    #输入链接，得到链接html
    def info_test(self,url):
        s = requests.Session()
        headers = random.choice(self.headers_list)
        txt = s.get(url,headers = {'User-Agent': headers})
        txt.encoding='utf-8'
        regex = '<script>window.location.href=(.*?);</script>'
        try:
            new_url = re.findall(regex, txt.text)[0]
            new_url = eval(new_url)
            txt = s.get(new_url,headers = {'User-Agent': headers})
            txt.encoding = 'utf-8'
            return txt
        except:
            return txt

    #循环info_test，最多5次
    def info_test_5(self,url):
        test_html = self.info_test(url)
        for i in range(5):
            if len(test_html.text) > 500:
                return test_html
            else:
                continue
        return '都五次了还没有得到！！'

class Threadq(threading.Thread):
    def __init__(self,arg1,arg2):
        threading.Thread.__init__(self)
        self.arg1 = arg1
        self.arg2 = arg2
    def run(self):
        w = wiwj()
        url_info = w.url_info()  # 100主页url
        for url_home in url_info[self.arg1:self.arg2]:
            html = w.info_test_5(url_home)
            content_url = w.url_content(html)
            print(content_url)
            for url in content_url:
                html2 = w.info_test_5(url)
                try:
                    inde_list.append(1)
                    inde = sum(inde_list)
                    print(w.huose_info(html2, inde))
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    inde_list = []
    thread_list = []
    thread_lock = threading.Lock()
    dic = {'district': 'district', 'tage': 'tage', 'orientation': 'orientation', 'decoration': 'decoration', 'towertype': 'towertype', 'heating': 'heating', 'rentway': 'rentway',
           'looktime': 'looktime', 'tradingarea': 'tradingarea', 'metor': 'metor'}
    df = pd.DataFrame(dic, index=[0])
    df.to_csv('tpy2.csv', mode='a', header=False, encoding='utf-8-sig')
    for i in range(4):
        thread_list.append(Threadq(i*10,1*10+10))
    for x in thread_list:
        x.start()
    for j in thread_list:
        j.join()
    print('完成！！')
    # wiwj().huose_info()
