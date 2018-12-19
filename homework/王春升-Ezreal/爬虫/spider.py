import requests
import re

'''
章节链接：https://www.x23us.com/html/66/66656/ 返回 ：章节列表


'''

class Spider:
    '''
    输入一个连接，输入N个正则表达式，返回相关信息

    
    '''

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

    def __init__(self,
                 url = 'https://www.x23us.com/html/66/66656/',
                 charset = 'utf-8',
                 

                 ):

        self.url = url
        self.charset = charset
        self.html5 = self.response_html()

    def response_html(self):

        r = requests.get(self.url,headers = self.headers)

        r.encoding = self.charset

        return r.text

    def get_info(self,**regexs):
        #print(regexs)

        info_dict = {}

        for key,value in regexs.items():

            info_dict[key] = re.findall(value,self.html5)

        return info_dict

            

        


    


















































    

    
