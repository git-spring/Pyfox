# python 中的类

# 定义一个类
class Foo:
    pass

# 类中定义方法和属性
class Foo:
    a = 10
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'hahah'
p = Foo('lisi',20)     # 类实例化
print(p.name)
print(p.a)
print(p)


# 类属性和实例属性

class Person:
    race = 'human'
    def __init__(self,name,age):
        self.name = name
        self.age = age

"""
类属性:定义在__init__ 方法里面的属性, 可以由类或者实例调用,类属性在实例间是共享的
实例属性: 直接定义在类里面的属性,只能由实例调用
"""
p1 = Person('lisi',20)
p2 = Person('wangwu',18)
print(p1.name,p1.age)   # 调用实例属性

print(Person.race)   # 调用类属性

p1.race = 'super human'  # 这个不是修改类属性，而是在p1这个对象中添加一个race属性
print(Person.race)
Person.race= 'super human'  # 修改类属性