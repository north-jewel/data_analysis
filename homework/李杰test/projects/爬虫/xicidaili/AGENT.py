import requests,re
from bs4 import BeautifulSoup

class Agent:
    def __init__(self,header,url):
        self.header = header
        self.url = url
    def Out_url(self):
        url_info = requests.get(self.url,headers=self.header).text
        agent =re.findall('<td>(.*?).(.*?).(.*?).(.*?)</td>',url_info)
        print(agent)
        return 123




headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
url = 'http://www.xicidaili.com/nn/'
Agent(headers,url).Out_url()