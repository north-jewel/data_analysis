# from bs4 import BeautifulSoup
import requests,re
import random


class Ip:
    def __init__(self,
                 header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}):
        print('kaishi')
        self.header = header
        # self.getHTMLText = self.getHTMLText()
        # self.get_Ip = self.get_Ip()

#西次网页源代码
    def getHTMLText(self,url):
        print('html')
        r = requests.get(url,headers = self.header).text
        return r

#抓到IP 添加到空列表
    def get_Ip(self,html):
        print('ip')
        rex = '<td>(.*?)</td>\s*<td>(.*?)</td>'
        rex = re.findall(rex,html)
        rex_list = []
        for n in rex[::2]:
            rex_list.append(n)
        return rex_list

#检测抓到的ip是否能用  返回一个能用的ip列表
    def get_can_ip(self,ip_list):
        # print(ip_list)
        ip_pool = []
        url = 'http://2018.ip138.com/ic.asp'
        # get_list_ip = self.get_Ip
        for i in ip_list:
            proxies = {'https':'{}:{}'.format(i[0],i[1]),
                       'http':'{}:{}'.format(i[0],i[1])}
            try:
                res = requests.get(url,proxies = proxies,headers = self.header)
            except (requests.exceptions.ProxyError,TimeoutError):
                print('xxx')
            else:
                print('ok',i)
                ip_pool.append(i)
                # return i
                # res.encoding = 'gb2312'
                # regex = '<body style="margin:0px"><center>(.*?)</center></body>'
                # huoqu = re.findall(regex, res.text)
                # print(huoqu)
                # if len(huoqu) != 0:
                #     ip_list.append(i)
                #     break
                # else:
                #     print('下一个')
                #     pass
            if ip_pool:
                return ip_pool
        # return i

# print(Ip().get_can_ip())
#
# def prox():
#     a = Ip().get_can_ip()
#     proxies = {'https':a,'http':a}
#     return proxies
# print(prox())

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    a = Ip()
    html = a.getHTMLText(url)
    a.get_can_ip(a.get_Ip(html))