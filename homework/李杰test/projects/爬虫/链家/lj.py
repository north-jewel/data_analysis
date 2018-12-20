import requests,re
import numpy as np
import pandas as pd
class Lianjia:
    def __init__(self,url,headers):
        self.url = url
        self.headers = headers
    def Frame(self):
        list_url = []
        for i in range(1):
            page_url = 'https://bj.lianjia.com/ershoufang/pg{}/'.format(i)
            re_page_text  = requests.get(page_url,headers=headers).text
            home_url = '<div class="item" data-houseid="(.*?)">'
            home_info = re.findall(home_url,re_page_text)
            list_url.append(home_info)
        return list_url
    def Home_url(self,):
        cite_Frame = list(self.Frame())[0]
        Home_list = []
        for i in cite_Frame:
            cav_url = 'https://bj.lianjia.com/ershoufang/'+str(i)+'.html'
            Home_list.append(cav_url)
        return Home_list
    def Home_info(self):
        cite_Home = list(self.Home_url())

        for i in range(2):
            url_info = requests.get(cite_Home[i],headers=headers).text
            re_title = '<h1 class="main" title=".*?">(.*?)</h1>'
            re_build_year = '<div class="subInfo">(.*?)</div>'
            re_label = '<span>(.*?)</span>'
            re_area = '<a href="/ershoufang/(.*?)/" target="_blank">(.*?)</a>&nbsp;'
            re_a_hous = '<span class="label">小区名称</span><a href="/xiaoqu/(.*?)/" target="_blank" class="info ">(.*?)</a>'
            re_unit_pricr = '<span class="unitPriceValue">(.*?)<i>元/平米</i></span>'
            re_total_price = '<span class="total">(.*?)</span>'
            re_look_count = '<div class="count">(.*?)</div>'
            re_con_label = ' <li><span class="label">(.*?)</span>(.*?)</li>'
            re_attention = '<span id="favCount" class="count">(.*?)</span>'
            re_have_met = '<span id="cartCount" class="count">(.*?)</span>'
            re_hous_2 = '<li><span class="label">房屋户型</span>(.*?)</li>'
            re_hous_3 = '<li><span class="label">所在楼层</span>(.*?)</li>'
            re_hous_4 = '<li><span class="label">建筑面积</span>(.*?)</li>'
            re_hous_5 = '<li><span class="label">房屋朝向</span>(.*?)</li>'
            re_hous_6 = '<li><span class="label">装修情况</span>(.*?)</li>'
            re_hous_7 = '<li><span class="label">建筑类型</span>(.*?)</li>'
            all_floor_regex = '<li><span class="label">所在楼层</span>.*?共(.*?)层.</li>'
            diqu_regex = '<span class="label">所在区域</span><span class="info"><a href=".*?" target="_blank">(.*?)</a>&nbsp;<a href=".*?" target="_blank">.*?</a>'

            title = re.findall(re_title,url_info)[0]#标题
            build_year = re.findall(re_build_year,url_info)[-1]#建筑年份
            label = re.findall(re_label,url_info)[6:9]
            area = re.findall(re_area,url_info)[1][1]#区域
            a_hous = re.findall(re_a_hous,url_info)[0][1]#小区
            unit_price = re.findall(re_unit_pricr,url_info)[0]#单价
            total_price = re.findall(re_total_price,url_info)[0]#总价
            look_count = re.findall(re_look_count,url_info)[0]
            attention = re.findall(re_attention,url_info)[0]#关注
            have_met = re.findall(re_have_met,url_info)[0]#带看
            hous_2 = re.findall(re_hous_2,url_info)[0]#户型
            hous_3 = re.findall(re_hous_3, url_info)[0]#楼层
            hous_4 = re.findall(re_hous_4, url_info)[0]#面积
            hous_5 = re.findall(re_hous_5, url_info)[0]#朝向
            hous_6 = re.findall(re_hous_6, url_info)[0]#装修
            hous_7 = re.findall(re_hous_7,url_info)[0]#楼型
            hous_8 = re.findall(all_floor_regex,url_info)[0]#总楼层
            hous_9 = re.findall(diqu_regex,url_info)[0]#地区
            label2 = label[0]#挂盘时间
            label3 = label[2]#上次交易
            a = np.array([title,hous_4,hous_7,build_year,label2,label3,hous_9,area,a_hous,unit_price,total_price,hous_2,hous_3,hous_8,attention,have_met,hous_5,hous_6])
            df = pd.DataFrame(a).T
            df.to_csv('aa.csv',encoding='gbk', index=False,mode='a',header=None)

        # df_2 = pd.read_csv(r'C:\Users\Administrator\Desktop\爬虫\aa.csv',engine='python')
        # df_2.columns=['标题','面积','楼型','建筑年份','挂牌时间','上次交易','地区','区域','小区','单价','总价','户型','楼层','总楼层','关注人数','带看','朝向','装修']

        return 0

if __name__ == '__main__':
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    print(Lianjia(1,headers).Home_info())









