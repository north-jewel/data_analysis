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

from woaiwojia import usergent
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import random
import time
import threading

class LoveHomeSpider:

    # 取决于 你初始化类的时候,是否想传入参数
    def __init__(self):
        self.url = 'https://bj.5i5j.com/zufang/n1/'
        self.header = {'user-agent': usergent.get_one_agent()}
        self.thread_pool = []

    # def __init__(self,url,header):
    #     self.url = url
    #     self.header = header

    # 将得到的数据做后续的处理
    def save_detail(self,txt_detail,
                    columns = ['url', 'houskeyword', 'rent', 'housetype', 'area', 'payment', 'district', 'tage',
                   'orientation', 'decoration', 'towertype', 'heating', 'rentway', 'looktime',
                   'tradingarea', 'metro', 'housingfacilities', 'last_time', 'seven_days', 'thirty_days',
                   'developers'],):
        df = pd.DataFrame(txt_detail,columns = columns)
        print('准备写入！')
        try:
            pd.read_csv('wawj5.csv')
        except FileNotFoundError:
            print('1，开始写入！')
            df.to_csv('wawj5.csv',index = False,encoding = 'utf-8')
        else:
            print('2，开始写入！')
            df.to_csv('wawj5.csv',index = False,header = None,encoding = 'utf-8',mode = 'a')
        print('写入完成！')

    def generate_urls(self):
        urls = []
        # https://bj.5i5j.com/zufang/n1/
        for i in range(6, 101):
            urls.append('https://bj.5i5j.com/zufang/n{}/'.format(i))
        return urls

    def get_page(self, url,encoding = 'utf-8'):

        time.sleep(random.choice([2, 2.5, 2.8, 1.2, 2.3, 1.9, 1.75, 1.83, 1.98, 2.68, 3.0, 3.3, 3.6]))
        s = requests.Session()
        headers = {
            'User-Agent': usergent.get_one_agent(),
        }
        # headers = self.header
        print(headers)
        res_obj = s.get(url, headers=headers)
        if res_obj.status_code == 200:
            res_obj.encoding = encoding
            print(res_obj.text)
            regex = '<script>window.location.href=(.*?);</script>'
            try:
                new_url = re.findall(regex, res_obj.text)[0]
                new_url = eval(new_url)
                # headers = self.header
                # print(headers)
                new_obj = s.get(new_url, headers=headers)
                if new_obj.status_code == 200:
                    new_obj.encoding = encoding
                    return new_obj.text
                else:
                    print('2,新链接请求失败！')
                    return None
            except IndexError:
                return res_obj.text
        else:
            print('1,原链接请求失败！')
            return None

    def get_all_url(self,
                    text,
                    url,
                    count_num = 6):
        start_num = 1
        while True:
            try:
                soup = BeautifulSoup(text, 'html.parser')
            except TypeError:
                start_num+=1
                if start_num == count_num:
                    url_list = []
                    return url_list
                time.sleep(random.choice([2, 2.5, 2.8, 2.2, 2.5, 1.9, 1.75, 1.83, 1.98, 2.68, 3.0, 3.3, 3.6]))
                print('第{}次请求页面链接：'.format(start_num))
                print(url)
                text = self.get_page(url=url, )
            else:
                url_list = self.parse_homepage(soup=soup)
                return url_list


    def parse_homepage(self,soup):

        # soup = BeautifulSoup(text,'html.parser')
        all_tag = soup.find_all('h3', class_='listTit')
        detail_urls = []
        url = 'https://bj.5i5j.com{}'
        for i in all_tag:
            i_list = []
            i_a_href = url.format(i.find('a').get('href'))
            i_a_text = i.find('a').text
            i_list.append(i_a_href)
            i_list.append(i_a_text)
            detail_urls.append(i_list)

        print(detail_urls)
        return detail_urls

    def parse_homepage_error(self, text):
        regex = '<script>window.location.href=(.*?);</script>'
        new_url = re.findall(regex, text)[0]
        new_url = eval(new_url)
        return new_url

    def get_detail_info(self,
                        page_source,
                        url,
                        count_num=6):
        start_num = 1
        while True:
            try:
                # count_num-=1
                soup = BeautifulSoup(page_source, 'html.parser')
            except TypeError:
                start_num+=1
                if start_num == count_num:
                    house_info = [None] * 19
                    return house_info
                time.sleep(random.choice([2, 2.5, 2.8, 2.2, 2.5, 1.9, 1.75, 1.83, 1.98, 2.68, 3.0, 3.3, 3.6]))
                print('第{}次请求详细链接：'.format(start_num))
                print(url)
                page_source = self.get_page(url=url, )
            else:
                house_info = self.parse_detailpage(soup=soup)
                return house_info


    def parse_detailpage(self, soup):
        # soup = BeautifulSoup(text,'html.parser')
        house_info = []
        try:
            rent = soup.find('div', class_='jlquannei fontbaise').find('p', class_='jlinfo').text
        except:
            rent = None
        finally:
            house_info.append(rent)

        try:
            fonthongse = soup.find_all('div', class_='jlquannei fonthongse')
            housetype = fonthongse[0].find('p').text
        except:
            housetype = None
        finally:
            house_info.append(housetype)

        try:
            fonthongse = soup.find_all('div', class_='jlquannei fonthongse')
            area = fonthongse[1].find('p').text
        except:
            area = None
        finally:
            house_info.append(area)

        try:
            fonthongse = soup.find_all('div', class_='jlquannei fonthongse')
            payment = fonthongse[2].find('p').text
        except:
            payment = None
        finally:
            house_info.append(payment)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            district = zushous[0].find('a').text
        except:
            district = None
        finally:
            house_info.append(district)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            tage = zushous[1].text.replace('楼层：', '')
        except:
            tage = None
        finally:
            house_info.append(tage)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            orientation = zushous[2].text.replace('朝向：', '')
        except:
            orientation = None
        finally:
            house_info.append(orientation)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            decoration = zushous[3].text.replace('装修：', '')
        except:
            decoration = None
        finally:
            house_info.append(decoration)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            towertype = zushous[4].text.replace('楼型：', '')
        except:
            towertype = None
        finally:
            house_info.append(towertype)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            heating = zushous[5].text.replace('供暖：', '')
        except:
            heating = None
        finally:
            house_info.append(heating)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            rentway = zushous[6].text.replace('出租方式：', '')
        except:
            rentway = None
        finally:
            house_info.append(rentway)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            looktime = zushous[7].text.replace('看房时间：', '')
        except:
            looktime = None
        finally:
            house_info.append(looktime)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            tradingarea = zushous[8].text.replace('商圈：', '')
        except:
            tradingarea = None
        finally:
            house_info.append(tradingarea)

        try:
            zushous = soup.find('div', class_='zushous').find_all('li')
            metro = zushous[9].text.replace('地铁：', '')
        except:
            metro = None
        finally:
            house_info.append(metro)

        try:
            fysty = soup.find('ul', class_='fysty').find_all('li')
            fy_str = ''
            for i in fysty:
                fy_str += i.text + ','
        except:
            fy_str = None
        finally:
            house_info.append(fy_str)

        try:
            dk_list = soup.find_all('div', class_='dknquan fonthongse')
            last_time = dk_list[0].find('p', class_='jlinfo jtoppad').text
        except:
            last_time = None
        finally:
            house_info.append(last_time)

        try:
            dk_list = soup.find_all('div', class_='dknquan fonthongse')
            seven_days = dk_list[1].find('p', class_='jlinfo jtoppad').text
        except:
            seven_days = None
        finally:
            house_info.append(seven_days)

        try:
            dk_list = soup.find_all('div', class_='dknquan fonthongse')
            thirty_days = dk_list[2].find('p', class_='jlinfo jtoppad').text
        except:
            thirty_days = None
        finally:
            house_info.append(thirty_days)

        try:
            developers = soup.find('li', class_='w100').text.replace('开发商', '')
        except:
            developers = None
        finally:
            house_info.append(developers)

        # print(house_info)
        return house_info

    # 将你的方法 都调度起来
    def startspider(self):
        urls = self.generate_urls()
        for url in urls:
            txt = self.get_page(url)

            detail_urls = self.get_all_url(txt,url)
            if len(detail_urls) == 0:
                continue
            for detail_url in detail_urls:
            # for x in range(0,len(detail_urls),10):
            #     for i in range(x,x+10):
            #         t = threading.Thread(target = self.crawl,args=(detail_urls[i],))
            #         self.thread_pool.append(t)
            #     for t in self.thread_pool:
            #         t.start()
            #     for t in self.thread_pool:
            #         t.join()
            #     self.thread_pool = []
                new_txt = self.get_page(detail_url[0])
                txt_detail = self.get_detail_info(new_txt,detail_url[0])  # 列表
                detail_url.extend(txt_detail)
                print(detail_url)
            self.save_detail(detail_urls) # 将得到的数据做后续的处理,比如 转成df,存入文件等等

    def crawl(self,detail_url):
        new_txt = self.get_page(detail_url[0])
        txt_detail = self.get_detail_info(new_txt, detail_url[0])  # 列表
        detail_url.extend(txt_detail)
        print(detail_url)

if __name__ == '__main__':
    lhs = LoveHomeSpider()
    # print(lhs.generate_urls())
    # print(lhs.get_page(lhs.url))
    lhs.startspider()