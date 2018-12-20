"""

@author:tts

@file: bs4_51job.py

@time: 2018/12/05

"""
import requests
from bs4 import BeautifulSoup
from pa import chengshi
import pandas as pd
'''
url = 'https://jobs.51job.com/guangzhou/83260048.html?s=01&t=0'
url_obj = requests.get(url)
url_obj.encoding='gbk'
url_text = url_obj.text
soup = BeautifulSoup(url_text,'html.parser')
#print(soup)
a = soup.find('div',class_='cn')
#print(a.h1)
#技能类别
#print(soup.find('h1').text.strip())
#print(soup.select_one('h1').get('title'))
'''

#城市
'''
zong  = soup.find('p',class_='msg ltype').text.strip()
print(zong)
zong = zong.split('|')
print(zong)
city = zong[0]
print(city)
#学历
xueli = zong[2].replace('\xa0','').replace('\xa03','')
print(xueli)
#工作经验
jingyan = zong[1].replace('\xa0','').replace('\xa03','')
print(jingyan)
#print(soup.select_one('p.msg.ltype ').get('title'))
'''

#公司名
#print(soup.find('div',class_='com_msg').text.strip())
#print(soup.select_one('div.com_msg > a > p').get('title'))

#公司规模
#print(soup.find_all('p','at')[1].text.strip())
#print(soup.select('div.com_tag > p:nth-of-type(2) ')[0].get('title'))

#公司类型
#print(soup.find_all('p','at')[2].text.strip())
#print(soup.select('div.com_tag > p:nth-of-type(3)')[0].get('title'))

#公司地点
#print(soup.find_all('p',class_='fp')[1].text.strip())
#print(soup.select('div.tCompany_main > div:nth-of-type(2) > div > p ')[0].text)

#薪资
#print(soup.find('div',class_='cn').find_all('strong')[0].text)
#print(soup.select('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > strong ')[0].text)


#技能要求
#print(soup.find('div',class_='bmsg job_msg inbox').text.strip())
#print(soup.select('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-of-type(1) > div')[0].text.strip())

#学历要求
#print(soup.find('p',class_='msg ltype'))
print()

#工作经验
print()
print()


#公司福利

#fuli = soup.find_all('span',class_='sp4')
#print(fuli)


#
#首页爬取

#爬取一个页面上的所有招聘链接
'''
urls = 'https://search.51job.com/list/010000,000000,0000,32,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
urls_obj = requests.get(urls)
urls_obj.encoding='gbk'
urls_text = urls_obj.text
soups = BeautifulSoup(urls_text,'html.parser')
#这个总比下面好用
company_zong=soups.select('#resultList > div.el > span > a')
#这个尽量别用
#company_zong=soups.select('#resultList > div.el > p > span > a')
#print(company_zong)

commpy_name=[]
commpy_url=[]
for  i in company_zong:
    print(i.get('href'))
    commpy_url.append(i.get('href'))
    commpy_name.append(i.text)
#print(company_url)
#print(len(company_zong))
print(commpy_url)
print(len(commpy_url))
print(commpy_name)

'''

class paqu_51job:
    def __init__(self,city,keywords):
        self.city = city
        self.keyword = keywords
        self.city_int = self.cit()
        self.page_max = self.pages()
    def cit(self):
        try:
            city_int = chengshi[self.city]
        except KeyError:
            return '000000'
        else:
            return city_int


    def pages(self):
        url = 'https://search.51job.com/list/'+self.city_int+',000000,0000,00,9,99,'+self.keyword+',2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        url_obj = requests.get(url)
        url_obj.encoding = 'gbk'
        url_text = url_obj.text
        soup = BeautifulSoup(url_text, 'html.parser')
        page_min_max = soup.select('#resultList > div.dw_tlc > div:nth-of-type(5)')[0].text
        page_max = page_min_max.split('/')[1].replace(' ','')#获取到了最大页数
        return page_max
    #pages('python')

    #进入具体网站 爬取相关的信息 返回一个字典
    def write_commpy_fortxt(self,urls):
        commpy_url = urls
        commpy_url_obj = requests.get(commpy_url)
        commpy_url_obj.encoding='gbk'
        commpy_url_text = commpy_url_obj.text
        soups = BeautifulSoup(commpy_url_text, 'html.parser')


        city_xueli_jingyan = soups.find('p',class_='msg ltype').text.strip()
        city_xueli_jingyan = city_xueli_jingyan.split('|')
        # 城市
        city = city_xueli_jingyan[0]
        #学历
        xueli = city_xueli_jingyan[2].replace('\xa0','').replace('\xa03','')
        #技能类别
        jinengleibie = soups.find('h1').text.strip()

        #工作经验
        jingyan = city_xueli_jingyan[1].replace('\xa0','').replace('\xa03','')
        #公司名
        commpy_name = soups.find('div',class_='com_msg').text.strip()
        #公司规模
        commpy_size = soups.find_all('p','at')[1].text.strip()
        #公司类型
        commpy_type = soups.find_all('p','at')[2].text.strip()
        #公司地点
        commpy_didian = soups.find_all('p',class_='fp')[1].text.strip()
        #薪资
        many = soups.find('div',class_='cn').find_all('strong')[0].text
        #技能要求
        yaoqiu = soups.find('div',class_='bmsg job_msg inbox').text.strip()
        commpy_dict = {
            'city':city,
            'skill_type': jinengleibie,
            'company_name':commpy_name,
            'company_size':commpy_size,
            'company_type':commpy_type,
            'company_location':commpy_didian ,
            'skills_required':yaoqiu,
            'edu_required':xueli,
            'experience_required':jingyan

        }
        return commpy_dict


    def pages_commpy_url(self):#返回5000条数据吧
        #commpy_url_zong=[]
        header = True
        for p in range(1,int(self.page_max)+1):

            print('共有'+self.page_max+'页')
            url = 'https://search.51job.com/list/'+self.city_int+',000000,0000,00,9,99,'+self.keyword+',2,'+str(p)+'.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
            url_obj = requests.get(url)
            url_obj.encoding = 'gbk'
            url_text = url_obj.text
            soup = BeautifulSoup(url_text, 'html.parser')
            company_zong = soup.select('#resultList > div.el > span > a')
            #commpy_url = []
            print('当前页面有'+str(len(company_zong))+'条招聘信息')
            nums = 0
            for i in company_zong:
                nums+=1
                print('正在写入第' + str(p) + '页,第'+str(nums)+'个')
                #print(i.get('href'))
                #commpy_url.append(i.get('href'))
                com_url = i.get('href')
                print(i.get('href'))
                com_dict = self.write_commpy_fortxt(com_url)
                com_dict['company_url']= com_url
                com_df=pd.DataFrame(com_dict)
                if nums>1:
                    header=False
                    com_df.to_csv(r'qianchengwuyou.csv',header=header,mode='a',encoding='utf_8_sig')
                #写入 所有连接
                '''
                with open('bs4_51job_commpy_url.txt','a') as f:
                    f.write(i.get('href'))
                    f.write('\n')
                '''
            #commpy_url_zong.append(commpy_url)









if __name__ == "__main__":
    a=paqu_51job('北京','python')
    page = a.pages()
    print(page)
    write_commpy = a.pages_commpy_url()





