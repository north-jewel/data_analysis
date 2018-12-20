import requests
import re
from random import choice
import pandas as pd
import glob
from fake_useragent import UserAgent





class Proxies_test():

    def __init__(self,proxies_ip):
        self.proxies_ip = proxies_ip
        self.ua = UserAgent()
    
    def random_header(self):
        headers = {'User-Agent': self.ua.random,
                    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    'Accept-Encoding': 'gzip'}
        return headers

    def test(self):
        url = 'http://2018.ip138.com/ic.asp'
        proxies = {
                    "http": "{}".format(self.proxies_ip),
                    "https": "{}".format(self.proxies_ip),
                }

        try:
            response = requests.get(url, proxies=proxies, headers=self.random_header())
        except (requests.exceptions.ProxyError, TimeoutError):
            pass
        else:
            return proxies


if __name__ == '__main__':
    print(Proxies_test('58.218.201.188:58093').test())













