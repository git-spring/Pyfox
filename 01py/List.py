# list  是python 中的列表,是一个可以类型,列表中可以存放任意类型的数据

# 定义list
names = []  # 定义空列表
names = ['zs', 'ls', 'ww', 'wuming']
values = list(range(5))  # 把可迭代对象转成list

# 增加元素
fruits = ['apple', 'peach', 'lemon', 'grape']
fruits.append('pear')  # 在最后添加一个元素
fruits.insert(2, 'orange')  # 在指定下标处插入 一个元素
fruits.extend(('cat', 'dog', 'lion', 'tiger'))  # 拼接另一个可迭代对象
print(fruits)

# 删除元素
fruits = ['apple', 'peach', 'lemon', 'grape']
fruits.remove('grape')  # 删除指定的元素， 若元素不存在会报错
fruits.pop()  # 默认删除最后一个元素
fruits.pop(1)  # 删除指定下标处的元素
del fruits[0]  # del 关键字可以删除元素，也可以删除变量   del fruits 会把变量直接删除
fruits.clear()  # 清空列表
print(fruits)

# 修改元素  列表是可变类型,可以直接修改
names[2] = 'wlw'  # 通过下标修改
print(names)  # ['zs', 'ls', 'wlw', 'wuming']

# 查找
names = ['zs', 'ls', 'ww', 'wuming', 'zs']
name = names[2]  # 获取指定下标的元素
names.index('zs')  # 取得指定元素的下标
names.count('zs')  # 计算个数
print('zs' in names)  # 列表中是否有指定元素

# 遍历列表
fruits = ['apple', 'peach', 'lemon', 'grape']
for i in fruits:
    print(i, end='  ')
print()

# 解包
a, b, c = ['10', 20, 30]
print(a, b, c)

a, b = b, a
print(a, b)

# 反转 & 排序

num = [1, 2, 3, 4, 5]
num.reverse()
num.sort()  # 正序
num.sort(reverse=True)  # 倒序
print(num)



# 列表切片
# 列表的切片和str的切片一样
