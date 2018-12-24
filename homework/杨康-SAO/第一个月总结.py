一、数据类型：
1、整数
2、浮点
    有除法或浮点类型值参与的运算返回的总是浮点类型值
3、字符串
    a、增
        #append()   用不了
        #insert()   用不了
        用新建字符串的方式去增
        +
        
    b、删
        del
        #remove()   用不了
        #pop()      用不了
        用新建字符串的方式去删
        
    c、改
        用新建字符串的方式去改
        
    d、查
        index()
            格式：xxstr.index(字符串)
            xxstr.index(要查询的字符串[，起始位置[，结束位置]])
        xxstr[位置]
        xxstr[起始位置：结束位置]
        xxstr[起始位置：]
        xxstr[:结束位置]
    总结：
        1、字符串本身不能改变
        2、只能查，只能通过新建字符串的方式去增、改、删
            
                    
4、列表
    a、增
        xxlist.append(添加的元素)#注该函数只有唯一参数     
        xxlist.insert(位置，元素)#注该函数有且必给两个参数
        +  #新建列表
    b、删
    
        del
        xxlist.pop([位置])#返回元素值并删除当前元素       
        xxlist.remove(元素)#注该函数有且必给一个参数
        查、改结合实现删目的
        
    c、改
    
        #index()
        xxlist[位置] = 指定元素
        xxlist[选定一个切片范围] = 列表#/元素/元组
        
        
    d、查
        xxlist.index(要查询的字符串[，起始位置[，结束位置]])
        xxlist.count(要查询的字符串[，起始位置[，结束位置]]
        xxlist[位置]
        xxlist[起始位置：结束位置]
        xxlist[起始位置：]
        xxlist[:结束位置]
        xxlist[:]#注复制一个列表
    总结：
        1、列表本身可变

字符串和列表性质总结：
                     
    1、字符串不可变，列表可变
    2、索引方法一至
    3、字符串用新建的方式实现增，删，改；
       增，删，改几乎所有的方法都是为列表设计
        
        
        
5、元组  #元组是一种特殊的字符串
#6、复数
#7、字典
二、控制流程
for    
while                    
if
elif
else
break
continue
pass                     
def
return
del
lambda x:x**2
in
is
and
or
not
not is
not in
from
import
None
True
False
                     
三、函数，方法
A、内置函数                     
range()
round()
print()
len()
max()
min()
str()
list()
dict()
set()
int()
float()
zip()
input()
sorted()
reversed()#
map()
type()
enumerate()
abs()
sum()
format()
pow()
isinstance()
bool()
id()

B、标准库                   
random.randrange()
random.randint()
random.choice()
random.sample()
random.random()

collections.deque


C、扩展库
pip requests.get(url)


D、列表的方法                     
index()
append()
extend()
pop()
remove()
insert()
sort()
count()

E、字典的方法
keys()
values()
items()
copy()
clear()
get()

D、字符串、元组的方法
strip()
index()
count()                     



