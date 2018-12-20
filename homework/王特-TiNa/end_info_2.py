# import json
#
# with open('end_info.txt','r',encoding='utf-8') as f:
#     lines = f.readlines()
#     a = 1
#     for dic in lines:
#         try:
#             dic2 = eval(dic)
#         except Exception as e:
#             print('\n')
#             print('第{}行出错'.format(a))
#             print(e)
#             print('\n')
#             a += 1
#         else:
#             with open('end_info_3.txt','a',encoding='utf-8') as ff:
#                 ff.write(dic)
#                 print('第{}行写入完成'.format(a))
#                 a += 1

import pandas as pd

columns = ["skill_type","city","company_name","company_size","company_type","company_description","company_location","salary","job_required","experience_required","company_welfare"]
with open('end_info_3.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    a = 1
    c = 1
    head = True
    for dic in lines:
        dic = eval(dic)
        if dic['city'].startswith('北京'):
            with open(r'analyze\company_welfare.txt','a',encoding='utf-8') as f:
                f.write(dic['company_welfare'])
                f.write('\n')
            with open(r'analyze\job_required.txt','a',encoding='utf-8') as ff:
                ff.write(dic['job_required'])
                ff.write('\n')
            with open(r'analyze\experience_required.txt','a',encoding='utf-8') as fff:
                fff.write(dic['experience_required'])
                fff.write('\n')
            print('第{}条信息已保存至txt中'.format(a))

            if '北京-' in dic['city']:
                dic['city'] = dic['city'].replace('北京-','')
            elif len(dic['city']) == 2:
                dic['city'] = '未知区'
            df = pd.DataFrame(dic, index=[0])
            if a == 1:
                head = True
            else:
                head = False
            df.to_csv(r'analyze\end_info_3.csv', index=False, header=head,encoding='utf_8_sig', mode='a')
            print('第{}条存储完成！'.format(a))
            print('\n')
            a += 1
        else:
            df2 = pd.DataFrame(dic, index=[0])
            if c == 1:
                b = True
            df2.to_csv(r'非北京.csv', index=False, header=head,encoding='utf_8_sig', mode='a')
            print('第{}条外地信息乱入'.format(c))
            c += 1


