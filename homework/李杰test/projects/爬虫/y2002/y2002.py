import requests,re

#
#慢摇舞曲
#
class Y2002:
    def __init__(self,header,url):
        self.header = header
        self.url= url
    def Y2002_url(self):
        info_url = requests.get(self.url,headers=self.header).text
        re_url = "<a href='(.*?).html' class='song' target='song'>(.*?)</a>"
        info = re.findall(re_url,info_url)
        print(info)
        print(len(info))
        for i in info:
            print('链接：'+'http://www.y2002.com/'+i[0]+'.html','歌名：'+i[1])
        #print(info_url)



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
url ='http://www.y2002.com/hottype/1.html'

Y2002(headers,url=url).Y2002_url()