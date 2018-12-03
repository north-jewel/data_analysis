url = 'https://bj.lianjia.com/ershoufang/pg1/'
'''
<a class="img" href="https://bj.lianjia.com/ershoufang/101103229329.html" target="_blank" data-bl="list" data-log_index="1" data-housecode="101103229329" data-is_focus="1"  data-el="ershoufang">
<a class="img" href="https://bj.lianjia.com/ershoufang/.*?" target="_blank" data-bl="list" data-log_index=".*?" data-housecode="{}" data-is_focus="1"  data-el="ershoufang">
<a class="title" href="https://bj.lianjia.com/ershoufang/101103229329.html" target="_blank" data-bl="list" data-log_index="1" data-housecode="101103229329" data-is_focus="1"  data-el="ershoufang">北京西城月坛99年南北通透大两居，双阳台，采光无遮挡</a>
</a><a class="title" href="https://bj.lianjia.com/ershoufang/.*?" target="_blank" data-bl="list" data-log_index=".*?" data-housecode="{.*?}" data-is_focus="1"  data-el="ershoufang">.*?</a>
'''
import requests
import re
charset = 'utf-8'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
res_url = requests.get(url,headers = headers)
res_url.encoding = charset
html = res_url.text

reg_info = '<div class="item" data-houseid="(.*?)">'

reg_ingo_list = re.findall(reg_info,html,)
for i in range(len(reg_ingo_list)):
    house_url = 'https://bj.lianjia.com/ershoufang/{}.html'.format(reg_ingo_list[i])
    house_res = requests.get(url,headers = headers)
    house_res.encoding = charset
    house_html = house_res.text
    print(house_html)
