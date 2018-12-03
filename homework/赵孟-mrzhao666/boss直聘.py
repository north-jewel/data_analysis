import requests
import re
import pandas as pd

def search(keyword,page = 1):
    url = r'https://www.zhipin.com/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

    url = 'https://www.zhipin.com/c101010100/'
    params = {
        'query': keyword,
        'page': page,
        'ka': 'page-next'
    }
    html = requests.get(url,headers = headers,params=params)
    return html.text

def re_info(html):
    info_re = '''<li>
                                <div class="job-primary">
                                    <div class="info-primary">
                                        <h3 class="name">
                                            <a href="(.*?)" data-jid=".*?" data-itemid="\d*?" data-lid=".*?" data-jobid=".*?" data-index="\d*?" ka=".*?" target="_blank">
                                                <div class="job-title">(.*?)</div>
                                                <span class="red">(.*?)</span>
                                                <div class="info-detail"></div>
                                            </a>
                                        </h3>
                                        <p>(.*?)<em class="vline"></em>(.*?)<em class="vline"></em>(.*?)</p>
                                    </div>
                                    <div class="info-company">
                                        <div class="company-text">
                                            <h3 class="name"><a href=".*?" ka=".*?" target="_blank">(.*?)</a></h3>
                                            <p>(.*?)<em class="vline"></em>(.*?)</p>
                                        </div>
                                    </div>
                                    <div class="info-publis">
                                        <h3 class="name"><img src=".*?" />(.*?)<em class="vline"></em>(.*?)</h3>
                                        <p>(.*?)</p>
                                    </div>
                                    <a href="javascript:;" data-url=".*?"
                                       redirect-url=".*?" target="_blank" class="btn btn-startchat">立即沟通
                                    </a>
                                </div>
                            </li>'''
    info_list = re.findall(info_re,html,re.S)

    return_list = []
    print(info_list)
    for i in info_list:
        info_A = i[8].split('<em class="vline"></em>')
        if len(info_A) == 1:
            info_A = [''] + info_A
        info_A.extend(list(i))
        return_list.append(info_A)
    columns = ['phase','company_size','url', 'skill_type', 'salary',
               'city', 'experience_required','edu_required',
               'company_name', 'post_type', '废弃', 'publisher',
               'publisher_position', 'publi_data']
    info_df = pd.DataFrame(return_list, columns=columns)


    return  info_df
def amend_data(df):
    df.url = df.url.apply(lambda x:'https://www.zhipin.com'+x)
    df = df.drop(columns = ['废弃'])
    return df


dd = True
print('一共有10页')
for i in range(1,11):
    if i == 2:
        dd = None
    html = search(keyword='python',page = i)
    x = re_info(html)
    xx = amend_data(x)
    xx.to_csv('ss.csv',index = None,mode='a',header = dd)
    print('第{}页爬取完毕'.format(i))