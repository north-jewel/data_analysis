import pandas as pd
from bs4Sprid import Bsprid
from spider import Spider
import threading

class Pacific:
    def __init__(self,
                 arg1=2,
                 arg2=1,
                 encoding='gb2312',
                 ):
        self.encoding = encoding
        self.url_content = 'https://price.pcauto.com.cn/top/oil/s1-t{}-p{}.html'.format(arg1,arg2)
    # def carinfo(self,url_car):
    #     res = requests.get(url_car)
    def contentinfo(self):
        url_list = []
        txt = Bsprid(self.url_content, self.encoding)
        contentinfo = txt.get_dicts(carname = 'div.info > p.sname',content6 = 'div.info > p.col',
                                    page = 'div.page > div.pcauto_page > a')
        content_info_url = txt.get_dict_url(url = 'div.info > p.sname > a')
        for i in content_info_url['url']:
            url_list.append('https://price.pcauto.com.cn{}'.format(i))
        if len(contentinfo['page']) > 0 :
            contentinfo['spage'] = contentinfo['page'][-2]
        else:
            contentinfo['spage'] = 1
        contentinfo['url']=url_list
        return contentinfo
    def particular_info(self,url_particular):
        res = Spider(url=url_particular,charset='gb2312')
        particular_info = res.info(gearbox = '<span class="">变&ensp;速&ensp;箱:</span>.*?<em>.*?<a id="bsx_5" name="focus_info" href=".*?" target="_blank" title=".*?">(.*?)</a>.*?</em>',
                       cartype = '<span class="">车身类型:</span>.*?<em>.*?<a href=".*?" target="_blank" title=".*?">(.*?)</a>.*?<a',
                       ranking = '<em>非总得分</em>.*?</div>.*?</div>.*?<p class="tip">(.*?)<a href=".*?" target="_blank" title="什么是车实力？" class="icon-qa">',
                       carstrength = '<span class="gray">车实力</span>.*?<p class="score">(.*?)</p>.*?<em>非总得分</em>',
                       configuration='<span class="gray">配置水平</span>.*?<p class="blue score">(.*?)</p>',
                       major = '<span class="gray">专业评测</span>.*?<p class="blue score">(.*?)</p>',
                       ownerevaluate = '<span class="gray">车主评价</span>.*?<p class="blue score">(.*?)</p>',
                       price = '<span class="gray">价格/费用</span>.*?<p class="blue score">(.*?)</p>',
        )
        return particular_info
# info_dict = Pacific(10,1).contentinfo()
# print(info_dict)

class Threadq(threading.Thread):
    def __init__(self,arg1,arg2):
        threading.Thread.__init__(self)
        self.arg1 = arg1
        self.arg2 = arg2
    def run(self):
        inde_list = []
        for arg in range(self.arg1,self.arg2):
            info_dict1 = Pacific(arg).contentinfo()
            for page in range(int(info_dict1['spage'])):
                info_dict = Pacific(arg,page).contentinfo()
            # print(Pacific(arg).contentinfo())
                for u in range(len(info_dict['url'])):
                    info = {}
                    info['carname'] = info_dict['carname'][u]
                    content6 = info_dict['content6'][u * 6:u * 6 + 6]
                    info['officialprice	'] = content6[0]
                    info['carfuelc'] = content6[1]
                    info['brand'] = content6[2]
                    info['MIITfuelc'] = content6[3]
                    info['rank'] = content6[4]
                    info['displacement'] = content6[5]
                    url = info_dict['url'][u]
                    print(url)
                    particular_info = Pacific().particular_info(url)
                    for k, v in particular_info.items():
                        if len(v) > 0:
                            info[k] = v
                        else:
                            info[k] = ''
                    mutex = threading.Lock()
                    mutex.acquire()
                    inde_list.append(1)
                    inde = sum(inde_list)
                    print(inde)
                    fair = pd.DataFrame(info, index=[inde])
                    fair.to_csv('Tpyinfo.csv', mode='a', header=False, encoding='utf-8-sig')  # ,mode='a'   追加
                    mutex.release()

if __name__ == '__main__':
    '''
    inde_list = []
    for arg in range(2, 21):
        print('页数：',arg)
        info_dict = Pacific(arg).contentinfo()
        # print(Pacific(arg).contentinfo())
        for u in range(len(info_dict['url'])):
            info = {}
            info['carname'] = info_dict['carname'][u]
            content6 = info_dict['content6'][u * 6:u * 6 + 6]
            info['officialprice	'] = content6[0]
            info['carfuelc'] = content6[1]
            info['brand'] = content6[2]
            info['MIITfuelc'] = content6[3]
            info['rank'] = content6[4]
            info['displacement'] = content6[5]
            url = info_dict['url'][u]
            print(url)
            particular_info = Pacific().particular_info(url)
            for k, v in particular_info.items():
                if len(v) > 0:
                    info[k] = v
                else:
                    info[k] = ''
            inde_list.append(1)
            inde = sum(inde_list)
            print(inde)
            fair = pd.DataFrame(info, index=[inde])
            fair.to_csv('Tpyinfo.csv', mode='a', header=False, encoding='utf-8-sig')  # ,mode='a'   追加
    '''
    thread_list = []
    for i in range(4):
        thread_list.append(Threadq(2+i*5,2+i*5+5))
    for x in thread_list:
        x.start()
    for j in thread_list:
        j.join()
    print('完成！！')



