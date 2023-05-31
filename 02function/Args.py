# python 中函数的参数分类

'''
1.位置参数
    调用时参数按照顺序传递给函数
    且调用时传递的参数个数要和函数定义时个数相同
'''


def test1(name, age, gender):
    print(name, age, gender, end='\t')


test1('lisi', 20, 'female')
print()

'''
2.关键字参数
    函数调用时可以指定参数的名称,可以不按顺序传递
    如果调用时既有位置参数,又有关键字参数,关键字参数必须放在位置参数之前
'''


def test2(name, age, gender):
    print(name, age, gender, end='\t')


test2('lisi', gender='female', age=20)
print()

'''
3.默认参数
    默认参数是在函数定义时给定参数默认值,定义时写在参数的最后
    函数调用时可以传递也可以不传递
    如果不传递就使用默认值,传递就使用传递的值
'''


def test3(name, age, gender='female'):
    print(name, age, gender, end='\t')


test3('lisi', 20)
test3('lisi', 20, 'male')
print()

'''
4.可变参数
    当不确定需要传递多少个参数时,可以使用可变参数(0个或多个)
    * 传入的参数会被封装成一个元组
    ** 传入的参数会被封装成一个字典, 传参时键值对之间用等号连接
'''


def test4(a, b, *args):
    print(a)
    print(b)
    print(type(args))
    sum = 0
    for num in args:
        sum += num
    print('和为 %d' % sum)


test4(20, 30, 10, 40)  # 前面两个数会传递给a,b  后面的会封装成元组传递给args


def test5(**kwargs):
    print(type(kwargs))
    print(kwargs)


test5(name='lisi', age=20)

'''
5.命名关键字参数
    如果函数需要指定参数名称,那么可以使用命名关键字参数
    在定义函数时,用*号把参数分隔,*号后面的参数在调用时需要指定和定义时一样的参数名称
    如果函数定义时已经有一个可变参数了,就可以不用单独写*号了
'''


def test6(name, age, *, gender):
    print(name, age, gender, end='\t')


test6('lisi', 20, gender='female')  # 后面的gender 必须指定
print()


def test7(name, age, *hobby, gender):  # 此时的gender 也是一个命名关键字参数
    print(name, age, hobby, gender, end='\t')


test7('lisi', '20', 'reading', 'swimming', 'hiking', 'eating', gender='female')  # gender 需要指定参数名称
print()
