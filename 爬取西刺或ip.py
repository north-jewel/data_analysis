import requests
import re
import pandas as pd
from fake_useragent import UserAgent

class proxies_filter:
    
    xici_url = 'http://www.xicidaili.com/nn/'
    ip_url = 'http://ip.seofangfa.com/proxy/1.html'
    def __init__(self,name = 'xici'):
        self.ua = UserAgent()
        self.name = name
        if self.name == 'xici':
            response = requests.get(self.xici_url,headers = self.random_header())
            self.html = response.text
            print(response)
        elif self.name == 'ip':
            response = requests.get(self.ip_url, headers=self.random_header())
            self.html = response.text

    def get_proxies(self):
        if self.name == 'xici':
            xre = '<td>(.*?)</td>\s*<td>(.*?)</td>'
            print(self.html)
            pro_list = re.findall(xre,self.html)
            print(pro_list)
            num = 0
            for i in pro_list[:]:
                if num % 2 == 0:
                    pass
                else:
                    pro_list.remove(i)
                num += 1
            
            pro_list = [i[0]+':'+i[1] for i in pro_list]
            self.save(pro_list)
            print('西刺第一页ip爬取完成')
            return pro_list
        if self.name == 'ip':
            xre = '<tr><td>(.*?)</td><td>(.*?)</td>'
            pro_list = re.findall(xre, self.html)
            pro_list = [i[0]+':'+i[1] for i in pro_list]
            self.save(pro_list)
            print('IP第一页ip爬取完成')
            return pro_list

    def save(self,pro_list):
        df = pd.DataFrame(pro_list, columns=None)
        df.to_csv('proxies.csv',header = None,index = False,mode = 'a')
        return None

    
    def random_header(self):
        headers = {'User-Agent': self.ua.random,
                   'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   'Accept-Encoding': 'gzip'}
        return headers


name = 'xici'
a = proxies_filter(name)
a.get_proxies()
