from spider import Spider
import pandas as pd
import numpy as np
import threading,_thread
from collections import deque
class Lianjia():
    def __init__(self, url='https://bj.lianjia.com/ershoufang/', charset='utf-8'):
        self.url = url
        self.charset = charset
        self.queue_list = deque(self.get_url_list())
        self.house_info_list = []

    def get_url_list(self):
        house_url_list = []
        url_list = []
        url_regex = '<div class="item" data-houseid=".*?"><a class="img" href="(.*?)" target="_blank"'
        for x in range(1, 101):
            house_url_list.append(self.url + 'pg{}/'.format(x))
            print(x)
        for u in house_url_list:
            url_list += Spider(u).get_info(url_list=url_regex)['url_list']
        return url_list

    def save_file(self):
        while True:
            if not self.queue_list:
                print(threading.active_count())
                if threading.active_count() > 2:
                    print(threading.active_count())
                    break
                elif threading.active_count() == 2:
                    print(threading.active_count())
                    b = pd.DataFrame(np.array(self.house_info_list),
                                        columns=['标题', '建筑面积', '建筑类型', '建筑年份', '挂牌', '上次交易', '地区', '区域', '小区',
                                                 '单价(元/平米)', '总价(万)', '户型',
                                                 '楼层', '总楼层', '关注人数', '带看', '朝向', '装修'])
                    b.to_csv('house.csv', encoding='gbk', index=False)
                    break

            i = self.queue_list.popleft()
            print(i)
            title_regex = '<h1 class="main" title=".*?">(.*?)</h1>'  # 标题
            build_area_regex = '<li><span class="label">建筑面积</span>(.*?)㎡</li>'  # 建筑面积
            tower_regex = '<li><span class="label">建筑类型</span>(.*?)</li>'  # 建筑类型
            yearbuilt_regex = '<div class="area"><div class="mainInfo">.*?</div><div class="subInfo">(.*?)建/.*?</div>'  # 建筑年份
            hang_board_regex = '<span class="label">挂牌时间</span>[\s\S]*?<span>(.*?)</span>'  # 挂牌
            last_deal_regex = '<span class="label">上次交易</span>[\s\S]*?<span>(.*?)</span>'  # 上次交易
            hang_board_duration_regex = ''  # 挂牌时长
            diqu_regex = '<span class="label">所在区域</span><span class="info"><a href=".*?" target="_blank">(.*?)</a>&nbsp;<a href=".*?" target="_blank">.*?</a>'  # 地区
            quyu_regex = '<span class="label">所在区域</span><span class="info"><a href=".*?" target="_blank">.*?</a>&nbsp;<a href=".*?" target="_blank">(.*?)</a>'  # 区域
            xiaoqu_regex = '<a href="/xiaoqu/.*?/" target="_blank" class="info ">(.*?)</a>'  # 小区
            unit_price_regex = '<span class="unitPriceValue">(.*?)<i>元/平米</i>'  # 单价(元/平米)
            total_price_regex = '<span class="total">(.*?)</span><span class="unit"><span>万</span>'  # 总价(万)
            house_type_regex = '<li><span class="label">房屋户型</span>(.*?)</li>'  # 户型
            floor_regex = '<li><span class="label">所在楼层</span>(.*?) .*?</li>'  # 楼层
            all_floor_regex = '<li><span class="label">所在楼层</span>.*?共(.*?)层.</li>'  # 总楼层
            attention_regex = '<span id="favCount" class="count">(.*?)</span>人关注'  # 关注人数
            look_regex = '<span id="cartCount" class="count">(.*?)</span>人看过'  # 带看
            aspect_regex = '<li><span class="label">房屋朝向</span>(.*?)</li>'  # 朝向
            finish_regex = '<li><span class="label">装修情况</span>(.*?)</li>'  # 装修
            info = Spider(i).get_info(title=title_regex, build_area=build_area_regex, tower=tower_regex,
                                          yearbuilt=yearbuilt_regex,
                                          hang_board=hang_board_regex, last_deal=last_deal_regex, diqu=diqu_regex,
                                          quyu=quyu_regex,
                                          xiaoqu=xiaoqu_regex, unit_price=unit_price_regex,
                                          total_price=total_price_regex, house_type=house_type_regex,
                                          floor=floor_regex, all_floor=all_floor_regex, attention=attention_regex,
                                          look=look_regex, aspect=aspect_regex,
                                          finish=finish_regex)
            info_list = []
            print(info)
            for x in info.values():
                if not x:
                    info_list.append(None)
                else:
                    info_list.append(x[0].replace(u'\u2764', u' '))
            self.house_info_list.append(info_list)
            print(len(self.house_info_list))

    def save(self):
        return  pd.DataFrame(np.array(a.house_info_list),
                     columns=['标题', '建筑面积', '建筑类型', '建筑年份', '挂牌', '上次交易', '地区', '区域', '小区', '单价(元/平米)', '总价(万)', '户型',
                              '楼层', '总楼层', '关注人数', '带看', '朝向', '装修'])

    def my_thread(self):
        pool = []
        for i in range(100):
            pool.append(threading.Thread(target=self.save_file))
        for i in pool:
            i.start()


if __name__ == '__main__':
    a = Lianjia()
    b = a.my_thread()
