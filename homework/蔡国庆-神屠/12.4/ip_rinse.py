import requests
import re
import pandas as pd
class Agency_IP():
    def __init__(self):
        self.url = 'http://www.xicidaili.com/'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

    def html(self):
        h5 = requests.get(self.url,headers = self.header).text
        #print(h5)
        return h5
    def ip(self):
        h5 = self.html()
        ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", h5, re.S)
        #print(ip_list)
        return ip_list
    # def save(self):
    #     ip_list = self.rinse()
    #     ip = []
    #     port = []
    #     ip_dict = {}
    #     for i in ip_list:
    #         ip.append(i[0])
    #         port.append(i[1])
    #     ip_dict['ip'] = ip
    #     ip_dict['port'] = port
    #     location = r'C:\Users\16677\Desktop\drag_hook_data\xici_ip.csv'
    #     df = pd.DataFrame(ip_dict)
    #     df.to_csv(location,index = None)
    def rinse(self):
        httpResult = self.ip()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='}
        usable_ip = []
        port = []
        ip = {}
        for i in httpResult:
            proxies = {
                'http': '{}:{}'.format(i[0],i[1]),
                'https': '{}:{}'.format(i[0],i[1])
            }
            try:
                print(proxies)
                response = requests.get(url = 'http://2018.ip138.com/ic.asp',
                                        proxies=proxies, headers=headers)
                usable_ip.append(i[0])
                port.append(i[1])

            except:
                print('{} ip报错'.format(i))
        ip['usable_ip'] = usable_ip
        ip['port'] = port
        return ip
    def save(self):
        ip_dict = self.rinse()
        location = r'C:\Users\16677\Desktop\drag_hook_data\xici_ip.csv'
        df = pd.DataFrame(ip_dict)
        df.to_csv(location,index = None)
if __name__ == '__main__':

    Agency_IP().save()

