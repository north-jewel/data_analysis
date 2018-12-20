import requests,re
import urllib.parse
import urllib
import json
class QQM4A:
    def __init__(self,urll,header):
        self.out_url = urll
        self.headers = header
    def List_url(self):
        url_info = requests.get(self.out_url).text
        re_music_url = '"songmid":"(.*?)","songname"'
        music_url = re.findall(re_music_url,url_info)
        #print(len(music_url))
        return music_url
    def Listen_url(self):
        listen_url = []
        gequ_list = []
        for i in self.List_url():
            url = 'https://y.qq.com/n/yqq/song/{}'.format(i)+'.html'
            listen_url.append(url)
            #只限刘德华歌曲
            data ='{"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"6501322940","songmid":["'+i+'"],"uin":"0","loginflag":1}}}'
            data_url = u"https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey24727490084941572&g_tk=5381&jsonpCallback=getplaysongvkey24727490084941572&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data=https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey24727490084941572&g_tk=5381&jsonpCallback=getplaysongvkey24727490084941572&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={}".format(data)
            data_text = requests.get(data_url,headers).text
            a = data_text.replace('getplaysongvkey24727490084941572(','').replace(')','')
            b = eval(a)
            gequ = b['req_0']['data']['midurlinfo'][0]['purl']
            gequ_list.append(gequ)
        return gequ_list

    def Music_ulr(self):
        a= self.Listen_url()
        print(len(a))
        for i in range(2):
            url = 'http://117.135.168.19/amobile.music.tc.qq.com/{}'.format(a[i])
            aa = requests.get(url,headers).content
            with open('{}.mp3'.format(i),'wb') as f:
                f.write(aa)
        return '下载完成'




headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.31 Safari/537.36'}


if __name__ == '__main__':
    #在这里输入歌手id
    url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?g_tk=5381&jsonpCallback=MusicJsonCallbacksinger_track&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&singermid=003ArN8Z0WpjTz&order=listen&begin=0&num=30&songstatus=1'
    print(QQM4A(urll=url, header=headers).Music_ulr())

