import sys


print(sys.argv)
a = '11 22  333     6666'
b = a.split(' ', 5)
print(b)

a = [1, 4, 6, 3, 98, 3, 7, 9]
a.sort()
print(a)

import keyword

print(keyword.kwlist)

student = [{"name": "小C", "age": 12, "score": 90},
           {"name": "小D", "age": 13, "score": 84},
           {"name": "小A", "age": 14, "score": 85},
           {"name": "小E", "age": 15, "score": 89},
           {"name": "小F", "age": 21, "score": 88}]

student.sort(key=lambda a: a['age'])
print(student)

# 75、列表嵌套元组，分别按字母和数字排序
a = [(6, 7), (1, 2, 3, 'a', 'c'), (3, 5, 'i', 9, 't', 'c')]
a.sort(key=lambda x: x[0])
print(a)

dic = {"name": "zs", "sex": "man", "city": "beijing"}
foo = zip(dic.keys(), dic.values())
foo = [i for i in foo]
print("字典转成列表嵌套元组", foo)
foo.sort(key=lambda x: x[0])
print(foo)
print(dic.keys(), type(dic.keys()))
a = [1, 2, 3, 4]
b = tuple(a)
print(b)






c=int('1.9')
d = int   ( 1.9 )
print(c,'    ',d ,end='  ')
