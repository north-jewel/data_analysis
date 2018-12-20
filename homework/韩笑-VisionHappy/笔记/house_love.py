
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from numpy import random

url_2 = []
for i in range(1,101):
    url = 'https://bj.5i5j.com/zufang/n{}/'.format(i)
    url_2.append(url)
def love_home_love(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'yfx_c_g_u_id_10000001=_ck18121415052416816770075676970; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Abj.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; _ga=GA1.2.467607825.1544771126; _gid=GA1.2.1427570887.1544771126; PHPSESSID=i8k284bf936r4t5nhudr1vvp54; domain=bj; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Awww.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1544772132,1544854653,1544854779,1544859838; _Jo0OQK=6CE8D4F37D6898D9674A6B31D1C34BC8B9FBE5FB185AB78A7E7E4E3F32DEA2D3CD00C185C0B11E5F20747B5F4AA2447A09FE66E6B9D87F63BBCDDE59481402EBE9AC57212F12283777C840763663251ADEB840763663251ADEBA412889ABE41BE6E2DBEB50F8D291FCBGJ1Z1Wg==; yfx_f_l_v_t_10000001=f_t_1544771124680__r_t_1544854651592__v_t_1544860736618__r_c_1; zufang_BROWSES=42104964%2C42101995%2C42101090%2C42107853%2C42119308%2C42112879%2C42117850%2C42118108; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1544862066',
        'Host': 'bj.5i5j.com',
        'Referer': 'https://bj.5i5j.com/zufang/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

    for i in url_2:
        res = requests.get(i, headers=headers)

        if res.status_code == 200:
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text, 'html.parser')
            time.sleep(random.randint(5,15))
            #print(soup)
            houseketword = soup.find_all('h3', class_='listTit')
            #print(houseketword)
            rent=soup.find_all('p',class_='redC')
            
            #print(houseketword)
            
            house=soup.find_all('div',class_='listX')
            for x in house:
                huxingmianjichaoxianglouceng=x.p.text.split('·')
                housetype = []
                huxingmianjichaoxiangloucen=x.p
                xx = huxingmianjichaoxiangloucen.next_sibling.next_sibling
                district_metor=xx.text.split(' ')
                locdtime = xx.next_sibling.next_sibling.text.split('·')
                #print(locdtime)
               
            
            for i in rent:
                rent_1 = i.strong.text
                rentway = i.next_sibling.next_sibling.text.replace('出租方式：','')
                
                
                
            for t in houseketword:
                houseketword_1 = t.a.text
                dict_1 = {
                            'houseketword':houseketword_1,
                            'rent':rent_1,
                            'housetype':huxingmianjichaoxianglouceng[0],
                            'area':huxingmianjichaoxianglouceng[1],
                            'district':district_metor[1],
                            'orientation':huxingmianjichaoxianglouceng[2],
                            'tage':huxingmianjichaoxianglouceng[3],
                            'decoration':huxingmianjichaoxianglouceng[4],
                            'rentway':rentway,
                            'tradingarea':district_metor[0],    
                            'record':locdtime[1]
                              
                            }
                with open ('house_love.txt','a+') as f:
                    f.write(str(dict_1))
                    f.write('\n')
                    print('写入成功')
                
                
                
                
                
               
            
                

love_home_love(url_2)
