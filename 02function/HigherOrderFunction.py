# 高阶函数
# 一个函数能接收另一个函数作为参数, 这样的函数称为高阶函数

# python 中常用高阶函数

"""
# map
参数：
    func: 执行的函数
    *iter: 可迭代对象
"""

def add(a):
    return a * 2

res = map(add, [1, 2, 3,4,5,6])
print(list(res))  # map 对象,可以转换成list输出

"""
# reduce
# reduce函数在python3中被放置到functools模块中,要使用需要引入
参数:
    function  : 执行的函数
    sequence  : 序列,会做为参数反复传入执行的函数
    initial   : 初始值,可以不传入

传入的序列反复调用 add 函数 1+2+4+7+8
如果有初始值,则结果为10+1+2+4+7+8
"""
from functools import reduce

def add(a,b):
    return a + b

x = [1,2,4,7,8]
res = reduce(add,x)
print(res)


'''
# filter
参数:
    func:过滤函数,可以是匿名函数
    iterator:可迭代对象
    
把符合要求的数据过滤出来
'''
def fil(x):
    return x>5

res = filter(fil,range(9))
print(list(res))

"""
# max
参数:
    *args     : 一个可变参数,用于比较
    key=None  : 比较规则,可不传
    
获取一个容器中的最大值,可以自定义比较规则
"""
res = max(['apple','pear','orange'],key = lambda x:len(x))
print(res)

"""
# min
参数:
    *args     : 一个可变参数,用于比较
    key=None  : 比较规则,可不传

获取最小值,与max的使用方法类似
"""
res = min(['apple','pear','orange'],key = lambda x:len(x))
print(res)

"""
# sorted
"""
sorted()