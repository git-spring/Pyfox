# 私有变量

class Person:
    race = ''

    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def __test(self):
        print('私有方法被调用了')


"""
python 以双下划线开头的变量是私有变量，不能直接获取

获取方式:
    1. 使用对象._类名__私有属性变量名
    2. 定义get/set方法获取
"""
p = Person('Tom', 20, 100)
# print(p.name,p.age,p.__money)   # __city 属性不能直接获取
print(p._Person__money)  # 通过 对象._类名__私有属性变量名  获取到私有变量

"""
私有方法:
    以双下划线开头的方法是私有方法,不能直接调用
    调用方法和私有属性的调用方法一样
    
"""
# p.__test()    # 不能调用
p._Person__test()  # 调用私有方法
