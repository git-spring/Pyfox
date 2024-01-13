# print 的一些基本用法


print('test1', "test2", '''test3''', """test4""")
print('''
海上升明月
天涯共此时
''')

# 使用+号,中间没有空格, 逗号会有空格
print('情人怨遥夜,' + '竟夕起相思')

# 换行
print('将end参数修改为其他符号,则不会换行', end='\u2764')
print('接着上一行,没有换行')
# 间隔符
print('可以间隔符参数', '----', sep='$')

# 格式化输出
name = 'zhangsan'
age = 10
weight = 30.36
print('%s 今年 %d岁,体重%.2f kg' %(name, age, weight))


# 配合format函数使用
print('{name} 今年 {age}岁,体重{weight} kg'.format(name= name, age=age, weight=weight))
print('{0} 今年 {1}岁,体重{2} kg'.format(name, age, weight))


