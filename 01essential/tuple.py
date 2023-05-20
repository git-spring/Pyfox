# tuple 元组和列表非常相似,区别是列表是可变的数据类型, 而元组是不可变的数据类型

# 定义
tup = ()  # 定义一个空元组
tup = (1, 2, 3, 4, 5)
tup = tuple([1, 2, 3, 4, 5])  # 把 可迭代对象 转化成 元组
print(tup)

# 如果元组只有一个元素,需要添加逗号
tup = ('1')    # <class 'int'>
tup = (1,)    # <class 'tuple'>

# 通过下标获取元素
ele = tup[0]
print(ele)

# 其它方法
tup.index('X')
tup.count('x')




# 不可以修改,增加,删除
## tup[1] = 5  # 元组是不可变元素, 不可以修改
