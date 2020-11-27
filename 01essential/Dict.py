# dict 是python 中的字典数据类型,以k-v键值对的形式存储数据
# dict 是一种可变的、可迭代对象

# 定义
d = {}  # 定义一个空字典
d = {'name': 'lisi', 'age': 25, 'wage': 3000}

'''
注意:
    1. 字典中的key只能是不可变数据类型 (str,number,tuple)
    2. 字典中的 value 可以是任意数据类型
    3. 字典中的key 不能重复,如果重复的话,后面的数据会覆盖前面的数据
    4. 字典中保存的数据是无序的,不能通过下标获取元素
    5. 字典不支持加法(+)运算
'''

person = {'name': 'lisi', 'age': 25}
# 增加/修改元素
person['name'] = 'zhangsan'  # 如果key 存在则修改
person['weight'] = 50  # 如果key 不存在则新增

# 获取元素
## 通过key 获取value
ele = person['name']  # 如果key不存在,会报错
## 通过get 获取value ,key 不存在可以返回默认值
ele = person.get('name1', 'default value')

# 删除元素
person.pop('name')  # 删除指定元素
del person['age']
item = person.popitem()  # 删除随机一个元素,并把元素的键值对作为一个元组返回  ('weight', 50)
person.clear()  # 清空字典
del person

# 两个字典合并成一个字典  update
d1 = {'name': 'lisi', 'age': 25, 'wage': 3000, 'emp_no': 9999}
d2 = {'emp_no': 9999, 'birthday': '1990-12-12', 'hiredate': '2018-12-12'}
d1.update(d2)  # d2 合并到 d1

# 遍历
people = {'name': 'lisi', 'age': 25, 'weight': 50}

## 1  遍历所有的key
for x in people:
    print((x, people[x]))

for x in people.keys():
    print((x, people[x]))

## 2  遍历所有的键值对
for k, v in people.items():
    print(k, v)

for x in people.items():
    print(x)

## 3 遍历所有的value
for v in people.values():
    print(v)

# 字典推导式
d1 = {'name': 'lisi', 'age': 25, 'wage': 3000, 'emp_no': 9999}
d2 = {v: k for k, v in d1.items()}
print(d2)
