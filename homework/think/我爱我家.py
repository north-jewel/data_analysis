from method import method
import requests
from bs4 import BeautifulSoup
import pandas as pd
from new_ip import  IP
import threading
m=method()
city={

    '北京':'bj',
    '成都':'cd',
    '长沙':'cs',
    '杭州':'hz',
    '南京':'nj',
    '南宁':'nn',
    '上海':'sh',
    '苏州':'sz',
    '天津':'tj',
    '太原':'ty',
    '武汉':'wh',
    '无锡':'wx',
    '郑州':'zz',
    }

def url_(str_='太原'):
    error = []
    try:
        url = 'https://{}.5i5j.com/ershoufang/'.format(city[str_])
        url1='https://{}.5i5j.com'.format(city[str_])
    except Exception as e:
        error.append(e)
        m.writes('错误日志.txt',error)
    return url,url1

def me_l(url):


    heads = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    obj = requests.get(url, headers=heads)
    print(obj.status_code)
    obj.encoding='UTF-8'
    text=obj.text

    return text
#m.writes('我爱我家详情.txt',me_l(url='https://ty.5i5j.com/ershoufang/42025833.html'))
def txt(list):
    _list = []
    for i in range(len(list)):
        _list.append(list[i].text.replace('\n', ''))
    return _list
#url_str=url_()
def isine(text,url_str):
    # text = m.read_file('我爱我家.txt')
    soup=BeautifulSoup(text,'html.parser')
    new_url=[]
    home_url=soup.select(' div.listCon > h3.listTit > a ')
    print(home_url)
    for i in home_url:
        new_url.append(url_str+i['href'])
    return new_url
# a=isine()
# print(a)
def isin_(text):
    error=[]
    # text = m.read_file('我爱我家详情.txt')
    soup = BeautifulSoup(text, 'html.parser')
    message={}
    e=soup.select('div.nodata > div.tywzi > p ')
    print(len(e))
    if len(e)==0:
        home_name=soup.select('div.rent-top.fl > h1.house-tit')

        if home_name:
            home_name_ = txt(home_name)
            message['名字']=[home_name_[0]]
        else:
            home_name_=None
            # print(home_name_)
        home_cost=soup.select('div.housesty > div.jlyou.fl > div.jlquannei.fontbaise > p')
        if home_cost:
            home_cost_=txt(home_cost)
            message['售价']=[home_cost_[0]+home_cost_[1]]
        else:
            home_cost_=None
        # print(home_cost_)
        home_at=soup.select('div.housesty > div.jlyoubai,fl > jlquannei.fontthongse > p')
        if home_at:
            home_at_=txt(home_at)
            try:
                message['单价']=[home_at_[0]]
                message['户型']=[home_at_[1]]
                message['面积']=[home_at_[2]]
            except Exception as e:
                error.append(e)
                m.writes('错误日志.txt',e)
        else:
            home_at_=None
        # print(home_at_)
        home=soup.select('div.zushous > ul > li')
        if home:
            home_=txt(home)
            try:

                message['小区']=[home_[0].split('：')[1]]
                message['楼层']=[home_[1].split('：')[1]]
                message['朝向']=[home_[2].split('：')[1]]
                message['装修']=[home_[3].split('：')[1]]
                message['规划用途']=[home_[4].split('：')[1]]
                message['年代']=[home_[5].split('：')[1]]
                message['建筑类型']=[home_[6].split('：')[1]]
                message['商圈']=[home_[7].split('：')[1]]
                message['看房时间']=[home_[8].split('：')[1]]
            except Exception as e:
                error.append(e)
                m.writes('错误日志.txt',e)

        else:
            home_=None
        # print(home_)
        home_con=soup.select('div.infocon.fl > ul > li')
        if home_con:
            home_con_=txt(home_con)
            message['挂牌时间']=[home_con_[4][4:]]
        else:
            home_con_=None
        # print(home_con_)
        home_l=soup.select('div.infocontent > ul.fytese > li')
        if home_l:
            home_l_=txt(home_l)
            try:
                message['核心卖点']=[home_l_[0][4:]]
            except Exception as e:
                error.append(e)
                m.writes('错误日志.txt',e)
        else:
            home_l_=None
        # print(home_l_)
        # print(home_[0].split('：')[1])
        print(message)
        return message
def ip():
    ip=IP()
    k=ip.K()
    x=ip.Xici()
    new_ip=k+x
    return new_ip
def daili(ip,ports):
    proxies = {
        "http": "http://{}:{}".format(ip,ports),
        "https": "http://{}:{}".format(ip,ports),
    }
    heads = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    url='https://ty.5i5j.com/ershoufang/'
    try:
        obj=requests.get(url, proxies=proxies,headers=heads)
        code = obj.status_code
        print(code)
        if code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        m.writes('代理错误日志.txt',e)
        pass


def thread(arg=10):

        while True:
            print('共{}条线程'.format(threading.active_count()))
            try:
                info=next(it)
            except StopIteration:
                if threading.active_count() < arg:
                    break
                if threading.active_count() == 3:

                    print('清洗完成')
                else:
                    break
            else:

                boo=daili(info[1]['ip'],info[1]['端口'])
                if boo:
                    m.writes('可用代理.txt',info[1])
                if threading.active_count() < arg:
                    xiancehng()


def xiancehng():
    threading.Thread(target=thread).start()

# ip_list=ip()
# print(ip_list)
#
# if len(ip_list):
#     it = enumerate(ip_list)
#     xiancehng()



def mian():
    print('支持的城市有\n', city.keys())
    str_=input('查询的城市')
    url,url1=url_(str_)
    text=me_l(url)
    print(url)
    url_list=isine(text,url1)
    counts=0
    head=True
    print(url_list)
    for i in url_list:
        print(i)
        dict=isin_(me_l(i))
        #print(dict)
        if counts !=0:
            head=False
        df=pd.DataFrame(dict)
        df.to_csv('return2.csv', header=head, mode='a',encoding='utf_8_sig' ,index=False)
        counts += 1
mian()







