import requests,re
import pandas as pd
import time
import random
['北京','成都','长沙','杭州','南京','南宁','上海','苏州','天津','太原','武汉','无锡','郑州']
['bj','cd','cs','hz','nj','nn','sh','sz','tj','ty','wh','wx','zz']

def iloveihome(page,keyword,url = None):
    if keyword == '二手房':
        key = 'ershoufang'
    if keyword == '租房':
        key = 'zufang'
    if url is None:
        print(1)
        url = 'https://bj.5i5j.com/{}/n{}/?wscckey=878bda31482aaf58_1544864500'.format(key,page)
    headers = {

        'Host': 'bj.5i5j.com',
        'Referer': 'https://bj.5i5j.com/zufang/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Cookie': '_ga=GA1.2.1980858266.1544855095; yfx_c_g_u_id_10000001=_ck18121514245510315882495951772; _gid=GA1.2.385810395.1544958310; _Jo0OQK=5197B7E3E72FF2982D11FAC93B3AC06777307A2571EA810152CDBF592AB69EC5CA8C86239D592771AFA9553F4B2FD6F81E9746C1D6F4412F990DDBA9EE73A3A955EC57212F12283777C840763663251ADEB840763663251ADEB7BE709A3B43A5E242350674422DE2517GJ1Z1TQ==; zufang_BROWSES=42119308%2C42127694; PHPSESSID=s2et3lbdmm0pf5lg820pj6tdp3; domain=bj; _gat=1; yfx_f_l_v_t_10000001=f_t_1544855095025__r_t_1545007165408__v_t_1545007165408__r_c_2; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Awww.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Awww.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1544855095,1544958311,1545007166; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1545007175'
        }
    print(2)
    html = requests.get(url,headers = headers)
    print(len(html.text))
    return html.text


def re_g(html,keyword):
    if keyword == '租房':
        re_all = '''<div class="listCon">
        <h3 class="listTit">
            <a href="(.*?)" target="_blank" .*?>(.*?)</a>
        </h3>
		<div class="listX">
		    <!--<p><i class="i_01"></i>4室2厅· 192.67平米· 南北 ·中层/11层 ·精装</p>-->
            <p><i class="i_01"></i>(.*?)  ·  (.*?)  平米  ·  (.*?)  ·  (.*?)  ·  (.*?)</p>
            <p><i class="i_02"></i><a href=".*?" target="_blank">(.*?)</a>(.*?)</p>
            <p><i class="i_03"></i>(.*?)  人关注 · 近30天带看  (.*?)  次  ·  (.*?)发布</p>
		    <div class="jia">
                <p class="redC"><strong>(.*?)</strong>
									元/月
										</p>
                <p>出租方式：(.*?)</p>
		    </div>
		</div>
        <div class="listTag"><span>(.*?)</span></div>
	</div>'''
    elif keyword == '二手房':
        re_all = '''<div class="listCon">
                <h3 class="listTit">
                    <a href="(.*?)" target="_blank"  onmousedown=".*?">(.*?)</a>
                </h3>
                <div class="listX">
                    <!-- <p><i class="i_01"></i>.*?</p> -->
                    <p><i class="i_01"></i>(.*?)·(.*?)  平米  ·  (.*?)  ·  (.*?)  ·  (.*?)</p>
                    <p><i class="i_02"></i><a href=".*?" target="_blank">(.*?)</a>(.*?)</p>
                    <p><i class="i_03"></i>(.*?)  人关注 · 近30天带看  (.*?)  次  ·  (.*?)发布</p>
                    <div class="jia">
                        <p class="redC"><strong>(.*?)</strong>万</p>
                        <p>单价(.*?)元/m²</p>
                    </div>
                </div>
                <div class="listTag"><span>(.*?)</span></div>
            </div>'''

    columns_name = ['url','houskeyword','housetype','area',
                    'orientation','tage','decoration','district',
                    'metor','attention','record','date_posted',
                    'rent','rentway','label']
    a = re.findall(re_all,html,re.S)
    print(len(html))
    print(len(a))


    df = pd.DataFrame(a,columns=columns_name)
    df.label = df.label.apply(lambda x:x.replace('</span><span>','|'))
    df.metor = df.metor.apply(lambda x:x.replace('<!-- · 地铁10号线 -->','')
                              .replace(' · ',''))
    return df

def re_a(html):
    re_a = '''<HTML>
<HEAD>
<script>window.location.href='(.*?)';</script>
</HEAD>
<BODY>'''
    url = re.findall(re_a,html,re.S)[0]
    return url

header = True
# cc = ['中日友好医院','万象新天两居室','新景家园东区距离地铁最近5/7号线','都市经典大一居随时可看房']

['二手房','租房']
keyword = '租房'
for i in range(1,200):
    print('第{}页开始爬取'.format(i))
    html = iloveihome(page = i,keyword = keyword)
    time.sleep(random.randrange(5, 10))
    print(888)
    if len(html) < 200:
        print('第一条件没过')
        try:
            url = re_a(html)
        except IndexError:
            continue
        html = iloveihome(page = i,keyword= keyword,url = url)
        time.sleep(random.randrange(5, 10))
        if len(html) < 200:
            print('第二条件没过')
            continue
    # print(cc[i-1] in html)
    df = re_g(html = html,keyword=keyword)
    if i == 2:
        print(header)
        header = None
    df.to_csv('5i5jer.csv',mode='a',index=None,header=header)

