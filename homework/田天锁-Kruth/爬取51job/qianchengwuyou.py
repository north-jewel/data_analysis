"""

@author:tts

@file: qianchengwuyou.py

@time: 2018/12/02

"""
import requests
import re,codecs
from pa import chengshi
import urllib
import time,random
from lxml import html
from urllib import parse
class show:
    headers = {
        'Host': 'search.51job.com',
        'Upgrade - Insecure - Requests': '1',
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.67Safari / 537.36'
    }
    def __init__(self,city,keywords):
        self.city  = city
        self.keywords = keywords

        self.city_int = self.cit()

    # 输入城市 返回相对于的码 如果没有找到那个城市 就返回全国的数据
    def cit(self):
        try:
            city_int = chengshi[self.city]
        except KeyError:
            return '000000'
        else:
            return city_int

    # 返回传入城市和关键字 的最大页数
    def page(self):
        url ='https://search.51job.com/list/'+self.city_int+',000000,0000,32,9,99,'+self.keywords+',2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        url_obj = requests.get(url, self.headers, timeout=10)
        s = requests.session()
        s.keep_alive = False
        url_obj.encoding = 'gbk'
        reg = re.compile(r'span id="rtPrev" class="dicon Dm"></span><span class="dw_c_orange">1</span> \/ (.*?)<a href=".*?"',re.S)
        pages = re.findall(reg,url_obj.text)
        pages = int(pages[0])
        return pages
    #返回当前页面中所有公司的链接列表
    def html(self,pag):
        url = 'https://search.51job.com/list/'+self.city_int+',000000,0000,00,9,99,'+self.keywords+',2,'+str(pag)+'.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        url_obj = requests.get(url,self.headers,timeout = 10)
        s = requests.session()
        s.keep_alive = False
        url_obj.encoding = 'gbk'
        reg = re.compile(r'class="t1 ">.*? <a target="_blank" title=".*?" href="(.*?)".*? <span class="t2">', re.S)
        links = re.findall(reg,url_obj.text)
        return links




    def save_file(self,link):
        r1 = requests.get(link,self.headers,timeout =10)
        r1.encoding = 'gbk'
        s = requests.session()
        s.keep_alive = False
        #城市
        reg_city = re.compile(r'p class="msg ltype" title="(.*?)&nbsp;')
        citys =  re.findall(reg_city,r1.text)

        #技能类别
        reg_skill_type = re.compile(r'h1 title="(.*?)">', re.S)
        skill_type = re.findall(reg_skill_type,r1.text)

        #公司名
        reg_company_name = re.compile(r'a href=".*?" target="_blank" title="(.*?)" class="catn"')
        company_name = re.findall(reg_company_name,r1.text)

        #公司规模
        reg_company_size = re.compile(r'p class="at" title="(.*?)"><span class="i_people"')
        company_size = re.findall(reg_company_size,r1.text)

        #公司类型
        reg_company_type = re.compile(r'<p class="at" title="(.*?)">\s*?<span class="i_trade">')
        company_type = re.findall(reg_company_type,r1.text)

        #公司地点
        reg_company_location = re.compile('span class="label">上班地址：</span>(.*?)\s*?</p')
        company_location = re.findall(reg_company_location,r1.text)

        #薪资
        reg_salay = re.compile(r'h1 title=".*?">.*?<strong>(.*?)</strong>', re.S)
        salay = re.findall(reg_salay,r1.text)

    #职位要求
        #技能要求:
        #将其中的<p></p>去除
        reg_skills_required = re.compile(r'class="bmsg job_msg inbox">\s*?<p>(.*?)\s*?<div class="mt10', re.S)
        skills_required = re.findall(reg_skills_required,r1.text)
        skills_required = skills_required[0].replace('<p>','')
        skills_required = skills_required.replace('</p>','')

        #学历要求 这个用到search
        reg_edu_required = '<span>\|</span>&nbsp;&nbsp;.*?&nbsp;&nbsp;<span>\|</span>&nbsp;&nbsp;(.*?)&nbsp;&nbsp;'
        edu_required = re.search(reg_edu_required, r1.text).group(1)

        #工作经验 这个用到search
        reg_experience_required = '<span>\|</span>&nbsp;&nbsp;(.*?)&nbsp;&nbsp;<span>\|</span>'
        experience_required = re.search(reg_edu_required, r1.text).group(1)

        #公司福利  可能为空  有的话一般是多条
        '''
        reg_company_blessing = re.compile(r'span class="sp4">(.*?)</span', re.M)
        company_blessing = re.findall(reg_company_blessing,r1.text)
        blessing =''
        if company_blessing ==[]:
            blessing = '该公司未写入福利项'
        else :
            for i in range(len(company_blessing)):
                blessing = blessing+company_blessing[i]+','
        '''

        '''
        info_dict = {'城市':citys,
                     '技能类别':skill_type,
                     '公司名称':company_name,
                     '公司规模':company_size,
                     '公司类型':company_type,
                     '公司地点':company_location,
                     '薪资':salay,
                     '职位要求':skills_required,
                     '学历要求':edu_required,
                     '工作经验':experience_required,
                     '公司福利':company_blessing}
                     
        '''
        try:
            file = codecs.open('51job.xlsx','a+','utf-8')
            #+'\t' + str(blessing)
            item = str(citys[0])+'\t'+str(skill_type[0])+'\t'+str(company_name[0])+'\t'+str(company_size[0])+'\t'+str(company_type[0])+'\t'+str(company_location[0])+'\t'+str(salay[0])+'\t'+str(skills_required)+'\t'+str(edu_required)+'\t'+str(experience_required)+'\n'
            file.write(item)
            file.close()
        except Exception as e:
            print(e)
            return None







if __name__ == "__main__":
    yibada=show('北京','python')


    pagess = yibada.page()#获得页数
    print('共有'+str(pagess)+'页')
    for p in range(1,pagess+1):
        print('正在爬取第{}页信息'.format(p))
        try:

            li = yibada.html(p)
            print(len(li))
            for l in li:
                print(1)
                yibada.save_file(l)
                print(2)
        except:
            continue
            print('出了问题')
