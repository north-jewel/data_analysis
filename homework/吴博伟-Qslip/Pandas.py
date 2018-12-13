##############################################################################
# DataFrame是Series的容器，Panel是DataFrame的容器
# Series  一种类似于一维数组的对象，是由一组数据(各种NumPy数据类型)
#         以及一组与之相关的数据标签(即索引)组成。
#         仅由一组数据也可产生简单的Series对象
'属性或方法':
    axes-->返回行轴标签列表
    dtype-->返回对象的数据类型(dtype)
    empty-->如果系列为空，则返回True
    ndim-->返回底层数据的维度，默认定义：1
    size-->返回基础数据中的元素数
    values-->酱系列作为ndarray返回
    head()-->返回前n行
    tail()-->返回最后n行
'参数:pd.Series(data,index,dtype,copy)'
    date-->数据采取各种形式、如：ndarray,list,constants
    index-->索引值必须是唯一的和散列的，与数据的长度相等。
            默认np.arange(n),如果没有索引将被传递。
    dtype-->dtype用于数据类型。如果没有，将推断数据类型
    copy-->复制数据，默认为false
'创建series方式：'
    1、通过一个列表创建-->pd.Series([1, 2, 5, np.nan, 6, 8])
    2、从ndarray创建-->pd.Series(np.array(['a','b','c','d']))
	3、通过字典创建-->pd.Series({'a':1,'b':2,'c':3})
'Series值的获取：'
	1、通过方括号+索引的方式读取对应索引的数据，有可能返回多条数据
	2、通过方括号+下标值（标签）的方式读取对应下标值的数据，下标值的取值范围为：[0，len(Series.values))；
		另外下标值也可以是负数，表示从右往左获取数据
	ser1 = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
	通过索引获取数据：ser1[:3]|ser1[::2]|ser1[4:2:-1]
	通过标签（下标值）获取数据：ser1['a':'b']|ser1['a':'d':2]|ser1['e':'c':-1]|ser1[['a','b']]
'Series的运算：'
	ser2 = pd.Series({'a':941,'b':431,'c':7555})
	输出大于500的值：ser2[ser2>500]
	计算加：ser2+10|计算减：ser2-10|计算乘：ser2*10
	两个series相加：ser1+ser2:对应位置的元素想加，其他位置为NAN
	计算各个元素的指数e的x次方  e 约等于 2.71828：np.exp(series)
	各个元素的绝对值：np.abs(series)
	sign()计算各个元素的正负号: 1 正数，0：零，-1：负数：np.sign(series)
'Series自动对齐：'
		当多个series对象之间进行运算的时候，如果不同series之间具有不同的索引值，
		那么运算会自动对齐不同索引值的数据，如果某个series没有某个索引值，那么最终结果会赋值为NaN
'Series及其索引的name属性：'
	Series对象本身以及索引都具有一个name属性，默认为空，根据需要可以进行赋值操作
	ser1.name = '字母'：a    1		    ser1.index.name= '索引'： 索引
			    b    2					a    1
			    c    3					b    2
                            d   -5					c    3
			    e    5					d   -5
			    Name: 字母, dtype: int64			e    5
                                                                        Name: 字母, dtype: int64
'Series的增删改查：'
	ser3 =  Series([100, 200], index=['g', 'h'])
	增：ser1['f'] = 100|ser1.append(ser3)
	删： drop 删除元素之后返回副本|pop 删除源数据
	ser1.drop('c')|ser1.drop(['a','d'])#删除元素返回副本|不改变源数据
	ser1.pop('d')#返回被删除的源数据|改变源数据
	改：通过标签，索引数据赋值
'Series常用函数：'
	1、Series.copy():复制一个Series
	2、Series.reindex([x,y,...], fill_value=NaN):重返回一个适应新索引的新对象，将缺失值填充为fill_value
		ser4 = pd.Series(['Tom', 'Kim', 'Andy'], index=['No.1', 'No.2', 'No.3'])
		rser4 = ser4.reindex(['No.0', 'No.1', 'No.2', 'No.3', 'No.4'])#不填充
		rser4 = ser4.reindex(['No.0', 'No.1', 'No.2', 'No.3', 'No.4'], fill_value='XXX')#填充缺失值
	3、Series.reindex([x,y,...], method=NaN)：返回适应新索引的新对象，填充方式为method
		method:
		  #ffill或pad: 前向（或进位）填充 
		  #bfill或backfill: 后向（或进位）填充
		rser4 = ser4.reindex(['No.0', 'No.1', 'No.4', 'No.5'], method='ffill')
		rser4s = ser4.reindex(['No.0', 'No.1', 'No.4', 'No.5'], method='bfill')
	4、Series.map(func)元素函数向量化：
		ser5 = pd.Series([1, 3, 5], index=['No.1', 'No.2', 'No.3'])
		ser5.map(lambda x:x*2)|ser5.map(np.exp)|ser5.map(math.exp)
	5、Series排序函数
		Series.argmax()返回含有最大值的索引位置
		Series.argmin()返回含有最小值的索引位置
		Series.sort_index(ascending=True):根据索引返回已排序的新对象
		Series.sort_values(ascending=True):根据值返回已排序的对象，NaN值在末尾
'Series.rank()排名方法：'
	#排名是按照排序(降序/升序)结果，用排名数值(1~n)，替换数值
	Series.rank(method='average', ascending=True, axis=0):为各组分配一个平均排名
	rank的method:
	'average'：在相等分组中，为各个值分配平均排名
	'max','min'：使用整个分组中的最小排名
	'first'：按值在原始数据中出现的顺序排名
######################################################################
#DataFrame是一个二维的表结构。Pandas的dataframe可以存储许多种不同的数据类型，
#		 并且每一个坐标轴都有自己的标签。你可以把它想象成一个series的字典项
'属性或方法:'
	df.T-->转置行和列
	df.axes-->返回一个列，行轴标签和列轴标签作为唯一成员
	df.dtype-->返回对象的数据类型
	df.empty-->如果df完全为空[无项目]，则返回为True; 如果任何轴的长度为0，则返回为True。
	df.ndim-->轴/数组维度大小
	df.shape-->返回表示df维度的数组
	df.size-->df中的元素数
	df.values-->df的Numpy表示
	df.head()-->返回开头前几行，默认为5行
	df.tail()-->返回最后n行，默认为5行
'参数pandas.DataFrame( data, index, columns, dtype, copy)：'
	data-->数据采取各种形式，如:ndarray，series，map，lists，dict，constant和另一个DataFrame
	index-->对于行标签，要用于结果帧的索引是可选缺省值np.arrange(n)，如果没有传递索引值
	columns-->对于列标签，可选的默认语法是 - np.arange(n)。 这只有在没有索引传递的情况下才是这样
	dtype-->每列的数据类型
	copy-->如果默认值为False，则此命令(或任何它)用于复制数据。
'创建df的方式：'
	创建日期索引序列：
		dates = pd.date_range('20180101',periods=6)#periods周期
		type(dates):pandas.core.indexes.datetimes.DatetimeIndex
		创建以时间为索引的df
		df =pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
