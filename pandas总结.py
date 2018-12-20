pip install -r requirement.txt




#创建一个dict,键为列元素，值为出现的次数
import collections
collections.Counter(df.A)


#索引，只能索引单个值
df.at['行名','列名']
df.iat[行号, 列号]


#索引小知识
df.loc[df.AAA >= 5,['BBB','CCC']] = 555#会改变b和c列
df[0:1]#索引第0行数据

#Series转成dataframe类型
Series.to_frame()

#每一列的信息，类型和是否有空值
df.info()

#最大数据的行名
df.列.idxmax()


#判断元素类型
df['A'].astype(np.int)


#数列排序后中间的那个数就是中位数
df.median()

#每个数值出现的次数
s.value_counts()

#计算df中有几个不同的元素
df.nunqiue()

#创建日期series，periods为几个元素,freq:Y(年),M(月),D(日),H(时),S(秒),ms(毫秒)
pd.date_range('20130101', periods=6,freq = 'M')


#日期类型
pd.Timestamp('20130102')

pd.to_datetime
df.index.year
df.index.month
df.index.day
data.index.to_period('A')
#A年 M月 W周 Q季度 10A十年
#10AS十年聚合日期第一天开始
#QS季度的开始第一天开始

data.resample('W')


#筛选条件
df.query("列名 == '5'")

#添加一行新列
df.assign(Area=lambda df: df.A*df.B)#返回一个新data
df['Volume'] = df.Length*df.Height*df.Depth#改变原data

#获得这个列名的下标
df.columns.get_loc('列名')


#统计指标
df.describe()

#转置
df.T

#变成一列数据，有两列，一列是表头，一列是value
pd.melt(df)
#pivot(columns,value)

#透视表
df2.pivot_table(values = 'PassengerId',index = 'Survived',columns = 'Sex',aggfunc = 'count')
pd.pivot_table(df,index=["Manager,"Rep"],values=["Price"],aggfunc=np.sum)



#按照索引排序，axis设置轴0是行，1是列，ascending升序或降序
df.sort_index(axis=1, ascending=False)

#按照值排序
df.sort_values(by = 列, ascending = False)

#根据A列排序后选择前n行，第一个最大，第二个最小

df.nlargest(n, 'A')
df.nsmallest(n, 'value')



#查看E列有没有元素two和four,返回bool的Series
df['E'].isin(['two','four'])
df.isin({'A': [1, 3], 'B': [4, 7, 12]})

#at和iat与loc和iloc相似，但at只能索引到具体的一个数值,且速度快
df.at['行','A']
df.iat[0,1]  #第零行第一列

#随机几行,参数frac等于0.5为一半,参数n为n行
df.sample()


#查找，参数regex = 正则，items,axis设置轴
df.filter(items = ['A','B'])
df.filter(regex = 'A')

#是否包含龙华园
df.小区.str.contains('龙华园')

#修改Index,fill_value会填充空值
df.reindex(index=list(), columns=list(),fill_value = 5)

df.reset_reindex#不传值会恢复原索引
reset_index(drop=True, inplace=True)
#drop=True会删除原索引列
                         
#修改表头
df.rename(columns = {'a':'A'})

#删除空值，参数是any的话只要有一个NaN就会删除一整行，
#参数all只有行内所有元素都是NaN才会删除
df1.dropna(how='any')

#删除某列数据
del df['A']                         
df.drop(columns = ['A','B'])

#删除重复的行,subset参数为列名，
#keep='first'表示保留第一次出现的重复行，是默认值。
#keep另外两个取值为"last"和False，
#分别表示保留最后一次出现的重复行和去除所有重复行
#inplace=True表示直接在原来的DataFrame上删除重复项，而默认值False表示生成一个副本
df.drop_duplicates(subset = ['A'],keep = False,inplace = True)



#把空值变成5，填充2个空值
df1.fillna(value=5,limit = 2)

#判断是否为空值
pd.isna(df1)
df1.isnull()
df1.notnull()

#判定元素的布尔值
df.any()#轴上所有元素全为False显示False,有一个是True则为True
df.all() #轴上有一个为False则显示False


#平均值，参数为轴号，默认为0.   0为列，1为行
df.mean(1)


#shift的参数为整数，把前几行变为NaN，本身元素会自动向下移。负数会往上移。
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(0)


#减法运算，df的对应index的所有元素减去s
df.sub(s, axis='index')

#元素累计和，第二行为一二行相加，第三行为二三行相加，第四行以此类推。
np.cumsum(df)
df.apply(np.cumsum)
df.apply(lambda x: x.max() - x.min())


#所有元素变成小写
s.str.lower()

#concat的参数为列表，列表元素为dataframe,把所有元素合为一个
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

#append与concat类似，True自动补齐索引值.
df.append(s, ignore_index=True)

#数据合并，on会将两个表key列中相同的行号聚合，
#how='inner' 参数指的是当左右两个对象中存在不重合的键时，
#取结果的方式：inner 代表交集；outer 代表并集；left 和 right 分别为取一边。
pd.merge(left, right, on='key',how = 'inner')


#A列中相同的元素进行分组
df.groupby('A')
df.groupby(['A','B'])


#元素总共的个数
sevies.size

#groupby中的方法
size() #返回每一组的大小
agg('min') #传递一个func


#堆叠和拆分堆叠
df.stack()
df.unstack()

#索引某一行或列，计算元素出现的次数
df[].value_counts()

#去掉这一列中重复元素后剩余的行数
df.nunique()

#dataframe中每个元素都遍历这个function
列.apply(function)
df.applymap(func)#所有列遍历

#元素按列排序
#字符串按字符串排序规则排序
df.rank(method)#参数有'dense','min','first'











