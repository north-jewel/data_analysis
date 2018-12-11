import pandas as pd
import requests,re
# from proxiess import Ip


# urla = 'http://www.xicidaili.com/nn/'
# a = Ip()
# html = a.getHTMLText(urla)
# info = a.get_can_ip(a.get_Ip(html))
# A = info[0][0]
# B = info[0][1]
#     # print(A)
#     # print(B)
# proxies = {'https': '{}:{}'.format(A, B), 'http': '{}:{}'.format(A, B)}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
def getHTTPTEXT(url):

    # 网页源码
    html = requests.get(url,headers=header)
    html_info = html.text
    return html_info
    print(html_info)

def get_info(html_text):
    # company_info ='''<li>
    #                                 <div class="job-primary">
    #                                     <div class="info-primary">
    #                                         <h3 class="name">
    #                                             <a href="(.*?)" data-jid=".*?" data-itemid=".*?" data-lid=".*?" data-jobid=".*?" data-index=".*?" ka=".*?" target=".*?">
    #                                                 <div class="job-title">.*?</div>
    #                                                 <span class="red">(.*?)</span>
    #                                                 <div class="info-detail"></div>
    #                                             </a>
    #                                         </h3>
    #                                         <p>(.*?)<em class="vline"></em>.*?<em class="vline"></em>(.*?)</p>
    #                                     </div>
    #                                     <div class="info-company">
    #                                         <div class="company-text">
    #                                             <h3 class="name"><a href=".*?" ka=".*?" target=".*?">(.*?)</a></h3>
    #                                             <p>(.*?)<em class="vline"></em>.*?<em class="vline"></em>(.*?)</p>
    #                                         </div>
    #                                     </div>
    #                                     <div class="info-publis">
    #                                         <h3 class="name"><img src=".*?" />.*?<em class="vline"></em>.*?</h3>
    #                                         <p>.*?</p>
    #                                     </div>
    #                                     <a href=".*?" data-url=".*?"
    #                                        redirect-url=".*?" target=".*?" class=".*?">.*?
    #                                     </a>
    #                                 </div>
    #                             </li>
    # '''

    # 正则出想要的内容
    company_info = '''<li>
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
    company_info = re.findall(company_info,html_text,re.S)
    # print(company_info)

    #循环提出每条数据的第八个  清洗一下  重新返回
    info_list = []
    for i in company_info:
        html_a = i[8].split('<em class="vline"></em>')
        if len(html_a) == 1:
            html_a = ['']+html_a
        html_a.extend(list(i))
        info_list.append(html_a)


        # print(info_list)

        # print(html_a)
        # print(company_info)
    #保存到csv
    columns = ['公司状态','公司规模','链接','职位','薪资','地址','经验','学历','公司名','公司类型','废弃','联系人','职务','时间']
    df_info = pd.DataFrame(info_list,columns = columns)
    # df_info.to_csv('aa.csv',encoding = 'utf_8_sig',index = False)
    # print(df)
    return df_info
    # def company_description(self):
    #     url_list = self.df.链接.apply(lambda x:'https://www.zhipin.com'+x)
#将链接表格内的链接保存完整   用于下个页面的访问
def del_discard(df):
    df['链接'] = df['链接'].apply(lambda x:'https://www.zhipin.com'+x)
    df = df.drop(columns = ['废弃'])  #删除带有标签的那一列
    return df
#代理IP


#传入url 运行  getHTTPTEXT方法

h = True
for i in range(1,11):
    if i == 2:   #当i为2时 不需要header
        h = None
    url = 'https://www.zhipin.com/c101010100/?query={}&page={}&ka=page-next'.format('python',i)
    x = getHTTPTEXT(url)
    xx = get_info(x)
    xxx = del_discard(xx)
    xxx.to_csv('information.csv',mode='a',header = h,index = None,encoding='utf_8_sig')
    print('第{}页'.format(i))
