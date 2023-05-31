# python 的循环

# for ... in ...
# for ... in ... 中in后面必须是可迭代对象，python 中可迭代对象有str,list,tuple,dict
# range()
for x in range(5):
    print(x)
# str
for x in 'lisi':
    print(x)
# list
for x in list(range(5)):
    print(x)
# tuple
for x in tuple(range(5)):
    print(x)

# dict
dic = {'name': 'zhang', 'age': 25, 'planet': 'Mars'}
for (x, y) in dic.items():
    print(x, y)

for key in dic.keys():
    print(key)

for value in dic.values():
    print(value)

# for ... else
# 100 到200 之间所有的质数
for num in range(100, 201):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        # print('%d 是一个质数 ' % num)
        pass

# while
i = 0
while i < 5:
    print(i)
    i += 1
