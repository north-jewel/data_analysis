import requests
from method import method
import re


url='https://search.51job.com/list/010000%252C060000,000000,0000,00,9,99,%2520,2,1.html'
meth=method()
def search(str_,city=None):
    chines=meth.isChinese(str_)
    english=meth.isEnglish(str_)
    if chines:
        chines=meth.decods(meth.decods(chines))
    if city:
        city_list=meth.add_city(city)
        city_code=meth.convert(meth.read_file(r'./config/地点.txt',arg='gbk',evals=True))
        new_city=''
        #print(city_code)
        list_=['%252C']*(len(city_list)-1)
        list_.append('')
        counts=0
        for i in city_list:
            if city_code[i]:
                new_city+=city_code[i]+list_[counts]
                counts+=1
            else:
                print('城市不存在')
                break
    else:
        new_city='010000'
    return 'https://search.51job.com/list/{1},000000,0000,00,9,99,{0},2,1.html'.format(chines+english,new_city,)

#a=search('python','北京,广州')
def request(url):
    # heads={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    # obj=requests.get(url,headers=heads)
    # obj.encoding='gbk'
    # text=obj.text
    #meth.writes('h5.txt',text,'utf-8')
    #print(text)
    text=meth.read_file(r'./h5.txt')

    pages_re='</span> (.*?)<a'
    content_re='''
                                <a target="_blank" title=".*?" href="(.*?)" onmousedown="">

                                    (.*?)                                </a>

                            </span>

                                                                                </p>

                        <span class="t2"><a target="_blank" title=".*?" href=".*?">(.*?)</a></span>

                        <span class="t3">(.*?)</span>

                        <span class="t4">(.*?)</span>

                        <span class="t5">(.*?)</span>

                    </div>
            '''
    print('2')
    pages=re.findall(pages_re,text)[0].replace('/','')
    print('2')
    content=re.findall(content_re,text,re.S)
    print('2')
    print(content)
    print(pages)
request(url)












