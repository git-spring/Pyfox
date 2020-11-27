# python 中的类

# 定义一个类
class Foo:
    pass

# 类中定义方法和属性
class Person:
    a = 10
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'hahah'
p = Person('lisi',20)     # 类实例化
print(p.name)
print(p.a)
print(p)

