import requests
import re
import pandas as pd
import numpy as np

def xiangxi(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

    html = requests.get(url,headers = headers)
    return html.text





def re_xiangxi(df_info,url):

    ino_re = '''<div class="detail-content">
                        
                        <div class="job-sec">
                            <h3>职位描述</h3>
                            <div class="text">
                                    (.*)
                            </div>
                        </div>
                        
                        
                        
                            
                            
                                
                                    <div class="job-sec">
                                        <h3>团队介绍</h3>
                                        (.*)
                                        
                                        <div class="job-tags">
                                            
                                                (.*)
                                            
                                        </div>
                                        
                                    </div>
                                
                                
                                    <div class="job-sec company-info">
                                        <h3>公司介绍</h3>
                                        <div class="text">
                                                (.*)
                                        </div>
                                        <a ka="job-comintroduce" href=".*?" target="_blank" class="look-all"><span>...</span>查看全部</a>
                                    </div>'''
    map_re = '<div class="location-address">(.*)</div>'

    gongshang_re = '''<div class="level-list">
                                            <li><span>法人代表：</span>(.*)</li>
                                            <li><span>注册资金：</span>(.*)</li>
                                            <li class="res-time"><span>成立时间：</span>(.*)</li>
                                            <li class="company-type"><span>企业类型：</span>(.*)</li>
                                            <li class="manage-state"><span>经营状态：</span>.*</li>
                                        </div>'''

    x = xiangxi(url)
    info_list = re.findall(ino_re,x,re.S)[0]

    gongshang = re.findall(gongshang_re,x)
    if len(gongshang):
        gongshang = gongshang[0]
    else:
        gongshang = ['','','','']
    map = re.findall(map_re,x)


    value_all = list(info_list)+list(gongshang)+map
    print(value_all)
    print(len(value_all))
    print(columns1+columns2+columns3)
    print(len(columns1+columns2+columns3))
    df_info.loc[df_info['url'].isin([url]), columns1+columns2+columns3] = value_all
    # df_info = qingxi(df_info)
    #df_info.to_csv('ww.csv',index = None)

    return df_info



def qingxi(df_info):
    df_info.job_required = df_info.job_required.apply(lambda x:x.replace('<br/>','/'))
    df_info.team = df_info.team.apply(lambda x:x.replace('</div>','').replace('<div class="text">',''))
    df_info.company_welfare = df_info.company_welfare.apply(lambda x:x.replace('<span>','').replace('</span>','')
                                                .replace('\n',',').replace(' ','').replace(',,','/'))
    df_info.company_description = df_info.company_description.apply(lambda x:x.replace('<br/>',''))
    return df_info


df_info = pd.read_csv('ss.csv')
columns1 = ['job_required', 'team', 'company_welfare', 'company_description']
columns2 = ['legal_representative', 'registered_capital', 'date_created', 'company_type']
columns3 = ['company_location']
columns_all = list(df_info.columns) + columns1 + columns2 + columns3
df_info = df_info.reindex(columns=columns_all,
                    fill_value=np.NaN)
print(df_info)
print(list(df_info.columns))

url = 'https://www.zhipin.com/job_detail/dacb23b5117958091HR40t24EFc~.html'
leng = len(df_info)
print('有{}条数据'.format(leng))
for i in range(leng):
    url = df_info.url[i]
    df_info = re_xiangxi(df_info,url)
    print('第{}条爬取完毕'.format(i+1))
df_info = qingxi(df_info)
df_info.to_csv('www.csv',index = None)
print('全部爬取完毕')
