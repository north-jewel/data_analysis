import requests
import re

class Ip:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    def __init__(self,page = 1):
        self.save_ip = []
        self.page = page
        self.get_list = self.get_list()
    def get_list(self):
        daili = requests.get("https://www.kuaidaili.com/free/inha/{}/".format(self.page),headers=self.headers)
        daili.encoding = 'utf-8'
        daili_text = daili.text
        regex = '<td data-title="IP">(.*?)</td>'
        daili_c = re.findall(regex,daili_text)
        daili_list = []
        print(daili_c)
        for i in daili_c:
            daili_list.append(i)
        return daili_list
    def get_can_ip(self):
        get_list = self.get_list
        for i in get_list[:20]:
            ip = i  # 代理ip    国内高级代理ip:https://www.kuaidaili.com/free/inha/1/     page:2589页
            proxies = {"http": i, "https": i, }
            try:
                res = requests.get("http://2018.ip138.com/ic.asp", proxies=proxies, headers=self.headers)
                requests.get("http://www.zhipin.com", proxies=proxies, headers=self.headers)
            except:
                continue
            else:
                # print(proxies)
                res.encoding = 'gb2312'
                regex = '<body style="margin:0px"><center>(.*?)</center></body>'
                huoqu = re.findall(regex, res.text)
                if len(huoqu) != 0:
                    self.save_ip.append(i)
                    if len(self.save_ip) > 5:
                        break
                    else:
                        continue
                else:
                    print('下一个')
                    continue
        return self.save_ip

def proxies(n):
    can_p = []
    get_ip = Ip(n).get_can_ip()
    for i in get_ip:
        proxies = {"http": i, "https": i, }
        can_p.append(proxies)
    return can_p

if __name__ == '__main__':
    for n in range(1,2899):
        print(proxies(n))



'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
ip = '116.1.11.19'  #代理ip    国内高级代理ip:http://www.xicidaili.com/nn
proxies = {"http": ip,"https": ip,}
res = requests.get("http://2018.ip138.com/ic.asp",proxies = proxies,headers = headers)
res.encoding = 'gb2312'
regex = '<body style="margin:0px"><center>(.*?)</center></body>'
#print(re.findall(regex,res.text))
'''