import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


#清洗数据
def write_csv():
    with open('end_info.txt','r',encoding='utf-8') as f:
        info = f.readlines() #内容 列表
        # print(info)
        a = 1
        c = 1
        b = True
        for i in info:
            # print(i)
            try:
                info_dict = eval(i)
            except:
                pass
            else:
                if '北京' in info_dict['city']:
                    # 把是北京地区的所有公司的福利添加到txt中
                    with open('company_welfare.txt','a',encoding='utf-8') as f:
                        f.write(info_dict['company_welfare'])
                        f.write('\n')
                #  清洗地区的数据

                #     if info_dict['city'] == '北京':
                #         # print(info_dict)
                #         info_dict['city'] = '未知地区'
                #     if '北京-' in info_dict['city']:
                #         info_dict['city'] = info_dict['city'].replace('北京-','')
                #         df = pd.DataFrame(info_dict, index=[0])
                #     if a == 2:
                #         b = False
                #     df.to_csv('end_info.csv',header=b,mode='a',index = None,encoding='utf_8_sig')
                #     print(a)
                #     a += 1
                # else:
                #     if c == 2:
                #         b = False
                #     df.to_csv('end_info_2.csv', header=b, mode='a', index=None, encoding='utf_8_sig')
                #     # print(info_dict['city'])
                #     a += 1
                #     c += 1
            return info_dict

#数据展示
class Data_show:

# 北京各地区提供岗位的多少  柱状图展示
    def skill_count(self,df):
        group_city = df_info.groupby(['city']).count()
        x = np.arange(13)
        y = group_city['skill_type'].values
        plt.bar(x,y)
        plt.title('各地区提供岗位的次数')
        ax = plt.gca()
        ax.set_xticklabels(x, rotation=40)
        lab = '东城区', '丰台区', '大兴区', '延庆区', '房山区', '昌平区', '朝阳区', '海淀区', '石景山区', '西城区', '通州区', '门头沟区', '顺义区'
        plt.xticks(x, lab)
        for x, y in zip(x, y):
            plt.text(x, y, '%.0f' % y, ha='center', va='bottom')
        plt.savefig('pict')
        return plt.show()

# 公司工作的年限要求的  柱状图展示
    def work_time(self,df):
        a = df.groupby(['experience_required']).count()
        # print(a)
        x = np.arange(7)
        y = a['company_name'].values
        print(y)
        plt.bar(x,y)
        # plt.title('工作年限的要求')
        lab = '10年以上经验','1年经验','2年经验','3-4年经验','5-7年经验','8-9年经验','无工作经验'
        plt.xticks(x,lab)
        plt.ylabel('公司数量',color= 'red')
        plt.xlabel('工作经验要求',color= 'red')
        for x, y in zip(x, y):
            plt.text(x, y, '%.0f' % y, ha='center', va='bottom')
        plt.savefig('work_time_pict')
        return plt.show()

# 技能工作要求
    def work_required(self,df):
        #读取到csv  索引出技能那一列
        jineng_list = df['job_required'].values
        # print(type(jineng_list))
        #类型是列表  迭代技能列表
        for i in jineng_list:
            # info = i.replace('岗位职责：', '').replace('工作描述:','').replace('工作职责','').replace('职责','').replace('岗位要求','').replace('任职要求','').replace('职责要求','').replace('职责描述','')
            #替换掉不需要的字符
            info = re.sub('[岗位职责：工作描述:工作职责,【岗位】：职责:岗位要求:任职要求:职责要求:职责描述:工作内容:【岗位职责】：主要职责:技能要求:岗位:工作内容:岗位说明:精准营销应用场景项目背景测试资格廊坊银行持续集成代码流水线程师]','',i)
            #写入txt   用于传入词云
            with open('work_require.txt', 'a', encoding='utf-8') as f:
                f.write(info)
                f.write('\n')
        return info




if __name__ == '__main__':
    df_info = pd.read_csv('end_info.csv')
    a = Data_show()
    # a.skill_count(x,y,lab)
    # a.work_time(df_info)
    # a.work_required(df_info)
    a.xinzi(df_info)