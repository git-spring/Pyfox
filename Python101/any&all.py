a = (1, 2, 3, 4, 5, '',)
print(a, '  all()  ', all(a))
b = (1, 2, 3, 4, 5, '1',)
print(b, '  all()  ', all(b))
e = ['', False, 0, [], {}, ()]
print(e, '  all()  ', all(e))
c = [1, 2, 3, '']
print(c, '  any()  ', any(c))
d = [1, 2, 3, 4, 5]
print(d, '  any()  ', any(d))
e = ['', False, 0, [], {}, ()]
print(e, '  any()  ', any(e))

# python any() all() 方法  ,可以用来判断 值是否为空.
# any 只要iterable 中有一个为真, 则返回真.
# all 有一个 为假 ,返回假.
# python 中的'假' ,包含  {} , [] , 0 , False, ()

