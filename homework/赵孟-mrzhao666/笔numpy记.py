import numpy

#找数组内元素等于1的坐标
np.argwhere(arr3 == 1)
#把能被2整除的元素提出来
np.extract(a%2==0,a)
#1000  10000  随机1000到10000的数
r = np.random.random((2,3))
r*(10000-1000)+1000

#创建数组，元素随机0到7，长度为10
np.random.randint(0, 7, size=10)
#圆周率
numpy.pi

#创建数组
p = numpy.array([1,2,3])

#创建范围为0-10的数组,并设定步长为5
p = numpy.arange(0,10,5)

#创建范围为0-10的数组，并设定元素个数为10
p = numpy.linspace(0,10,10)

#创建一个数组，内容随机，取决于内存的状态，dtype为float64.
p = numpy.empty((2,3))

#创建范围在0-1的随机数组
p = numpy.random.rand(3,2)



#创建一个3行5列元素全为0的数字,可以指定元素的类型
numpy.zeros((3,5),dtype = numpy.init16)

#该方法返回x基数为10的自然对数
np.log10()

#计算2的几次方等于4
log(4,2)

#求平均值
p.mean()

#求标准差
p.std()

#求和、求最大值、求最小值
p.sum()
p.max()
p.min()

#求最大值所在位置
p.argmax()

#获取每一列的结果
p.sum(axis=0)
#获取每一行的结果
p.sum(axis=1)
#mean函数也可以设置axis
p.mean(axis=0)


#数组维度
p.ndim

#修改类型
a.astype(np.int)

#数组类型
p.dtype.name
p.dtype

#数组元素总数
p.size

#数组中每个元素的大小
p.itemsize

#数组的大小
p.shape(3,3)  #不改变数组本身   其中一个参数为-1的话会自动计算
p.resize(3,3)  #改变数组本身



#矩阵的运算和数组不同
* = @
a.dot(b)


#数组变成可迭代的列表
p.flat[:]


#四舍五入 np.round
#舍去 np.floor
#进一 np.ceil

#把数组变为一行
p.ravel


#转置  行变列，列变行
p.T

#三种复制方法
b = a #地址完全相同，
b = a.view()  #地址不同，但改变b元素，a也会跟着改变
b = a.copy()  #完全复制，b和a完全无关系


#两个数组合一
np.vstack((a,b))

#两个数组每一行合一
np.hstack((a,b))

#条件判断  满足条件找a,不满足找b
np.where(条件,a,b)

#验证两个数组是否相等
np.allclose(x,a)

#改变shape元组元素的位置
np.tranpose()

#计算数组内元素的个数
np.bincount(x)


#数组转换为list
a.tolist()

#排序后输出元素的索引
a.argsort()
#排序
np.sort(a,axis)


a = np.convolve([1,3,2],[2,2,3],mode = 'full')
#'full'
#结果是元素长度-1
#           <-- 1  3  2
#  3  2  2  -->
#'valid'
#堆叠是后的值
#'same'
#full运算之后从中心开始取值，长度多大，返回多大

















