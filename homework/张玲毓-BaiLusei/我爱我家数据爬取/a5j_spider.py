# 思考
# 咱们要写一个什么类?这个类用来做什么
# 这个类有哪些属性? 有什么行为特征
# https://bj.5i5j.com/zufang/n1/
# 对应到类中 属性-->属性
# 行为-->方法

# Cookie: PHPSESSID=ff2tm10n8t15qt8oj7e89tfnur; domain=bj; yfx_c_g_u_id_10000001=_ck18121814262719214835619595335; yfx_f_l_v_t_10000001=f_t_1545114387754__r_t_1545114387754__v_t_1545114387754__r_c_0; _ga=GA1.2.1525843679.1545114388; _gid=GA1.2.985194328.1545114388; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Awww.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Awww.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6; _Jo0OQK=471256A4FCCD9A856DBD30426F867103F3DB8B42CFF957390507CDA302AF3D6155AFCCD14E4F809E4E3D2EFD0C6E029776A49097D56F18EDADF46A94AE037FDFE1AC57212F12283777C840763663251ADEB840763663251ADEBF2908E7E926C31E8A593CD374DB85252GJ1Z1Jw==; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1545008768,1545114389,1545114399,1545114409; zufang_BROWSES=42145746; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1545114515
# 此次 咱们写 类,  面向对象

# 爬我爱我家的爬虫

###地区city?
# 属性   url  header
# 行为  能干啥

# 生成所有页面的链接
# 给个链接,返回源代码
# 解析数据  解析不同界面的方法

from bs4 import BeautifulSoup
import requests
import random,time



class LoveHomeSpider:

    # 取决于 你初始化类的时候,是否想传入参数
    def __init__(self):
        self.url = 'https://bj.5i5j.com/zufang/n'
        # self.header = {'user-agent': self.get_one_agent()}
        self.header = {'Cookie': 'PHPSESSID=e04dcl1rkvcjdvjmvtq53hp9ad; _ga=GA1.2.1302851638.1544936116; _gid=GA1.2.746896476.1544936116; yfx_c_g_u_id_10000001=_ck18121612551515807320655551232; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1544936117; domain=bj; _Jo0OQK=75E4B432703F0DFD4E952568E48E7B67B1F63ABBB34359B7DF2C134EAA6AFD8C949A69DE239B77CFA2F5ECD8F821838AB994A7CF6727E5FB776E68808FC26C54DF3C57212F12283777C840763663251ADEB840763663251ADEB42E0F544D03120245FAFDAF9B9801008GJ1Z1Ig==; zufang_BROWSES=42119308; yfx_f_l_v_t_10000001=f_t_1544936115573__r_t_1544936115573__v_t_1544938642820__r_c_0; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1544938643',
            'Host': 'bj.5i5j.com',
            'Referer': 'https://bj.5i5j.com/zufang/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
            }
    # def __init__(self,url,header):
    #     self.url = url
    #     self.header = header



    def get_one_agent(self):
        return random.choice(headers)

    # 将得到的数据做后续的处理
    def save_detail(self,txt_detail):
        # print(txt_detail)
        pass

    #详情页的链接  返回一个列表
    def generate_urls(self):
        urls = []
        a = 0
        for i in range(1, 2):
            a += 1
            url = self.url+str(i)
            # print(url)
            res = requests.get(url, headers=self.header)
            res_text = BeautifulSoup(res.text, 'lxml')  #主页的源代码
            # print(res_text)
            url_list = res_text.find_all('h3', class_='listTit')
            for n in url_list:
                url_info = n.a.attrs['href']
                # print(url_info)
                urls.append(url_info)
            print('第{}页完'.format(a))
            time.sleep(random.randrange(5,10))

        return urls

    #详情页的源代码
    def get_page(self,url):
        '''

        :param url: 详情页的url
        :return: 详情页的源代码
        '''
        url1 = 'https://bj.5i5j.com'+url
        print(url1)
        res = requests.get(url1, headers=self.header)
        res_text = BeautifulSoup(res.text,'lxml')
        return res_text

    def parse_homepage(self,detail_text):
        '''

        :param text: 详情页的源代码
        :return: 返回一个列表
        '''
        detail_urls=[]
        data_dict = {}
        houskeyword_re = detail_text.find('h1', class_='house-tit').text
        rent_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div.jlyou.fl > div > p.jlinfo').text
        area_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div:nth-of-type(3) > div > p.jlinfo').text
        housetype_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div:nth-of-type(2) > div > p.jlinfo.font18').text
        payment_re = detail_text.select_one('body > div.main.container > div.details-view.clear > div.content.fr > div.housesty > div:nth-of-type(4) > div > p.jlinfo.font18').text
        li_info = detail_text.find('div', class_="zushous").find_all('li')
        house_dic = {'小区': 'district', '楼层': 'tage', '朝向': 'orientation', '装修': 'decoration', '楼型': 'towertype',
                     '供暖': 'heating', '出租方式': 'rentway', '看房时间': 'looktime', '商圈': 'tradingarea', '地铁': 'metor'}
        tag_house_dic = {'district': '', 'tage': '', 'orientation': '', 'decoration': '', 'towertype': '',
                         'heating': '', 'rentway': '', 'looktime': '', 'tradingarea': '', 'metor': ''}
        for tag in li_info:
            tag_info, tag_ = tag.text.split('：')[0], tag.text.split('：')[1]
            if tag_info in house_dic.keys():
                tag_house_dic[house_dic[tag_info]] = tag_
        data_dict['houskeyword'] = houskeyword_re
        data_dict['rent'] = rent_re
        data_dict['housetype'] = housetype_re
        data_dict['area'] = area_re
        data_dict['payment'] = payment_re
        # print(tag_house_dic)
        # print(data_dict)
        data_dict.update(tag_house_dic)
        print(data_dict)
        return

    def parse_homepage_error(self, text):
        soup = BeautifulSoup(text,'lxml')
        # print(soup)
        link = soup.find('script').text  # todo
        # print(link)
        # url = s.find('script').text.split("'")[1]
        return link

    def parse_detailpage(self, text):
        pass

    # 将你的方法 都调度起来
    def startspider(self):
        urls = self.generate_urls() #返回列表 内容是详情页的链接
        # print(urls)
        for url in urls:
            txt = self.get_page(url)    #迭代这个详情页的链接列表  并调用get_page访问源代码
            try:
                detail_urls = self.parse_homepage(txt)  # 按照正常步骤解析
            except:
                link = self.parse_homepage_error(txt)
                txt = self.get_page(link)
                detail_urls = self.parse_homepage(txt) # 这次铁定不会出错了

            for detail_url in detail_urls:
                txt_detail = self.parse_homepage(detail_url)  # 列表
                self.save_detail(txt_detail) # 将得到的数据做后续的处理,比如 转成df,存入文件等等




if __name__ == '__main__':
    lhs = LoveHomeSpider()
    # print(lhs.generate_urls())
    # print(lhs.get_page(lhs.url))
    lhs.startspider()