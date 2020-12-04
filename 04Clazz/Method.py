# python 中的方法
# 实例方法/静态方法/类方法

"""
实例方法
    定义在类中,方法定义时需要self参数
    可以使用实例对象调用,调用时对象会自动传递当前对象参数到self
    也可以使用类调用,用类调用时需要手动传递对象到self
"""


class Person1:
    age = 19
    def test(self, name):
        print('这是个实例方法')
        print(name)
        print(self.age)


p1 = Person1()
p1.test('zhangsan')  # 通过实例对象调用,self参数不需要传递
Person1.test(p1, 'zhangsan')  # 通过类调用,需要手动传入对象



"""
静态方法
    定义时通过@staticmethod装饰,
    不需要self参数
    可以通过类和实例调用
    
使用
    在开发时,如果需要在类中封装一个方法,这个方法:
    既不需要访问实例属性或者调用实例方法
    也不需要访问类属性或者调用类方法
    这个时候,可以把这个方法封装成一个静态方法
"""


class Person2:
    @staticmethod
    def test():
        print('这是个静态方法')


p2 = Person2()
Person2.test()    # 通过类调用
p2.test()         # 通过实例调用


"""
类方法
    定义时通过@classmethon装饰
    定义时需要cls(指向当前类)参数
    在类方法内部可以直接访问类属性或者调用其他的类方法

使用
    可以通过cls调用类的属性
    也可以通过cls调用其他的类方法
    调用时不需要传递cls参数
"""

class Person3:

    race = 'human'

    @classmethod
    def test(cls):
        print(cls.race)    # 类方法可以访问类属性
        print('这是个类方法')

    def test1(self):
        # print(race)     # 实例方法不能访问类属性
        pass
p3 = Person3()
p3.test()
Person3.test()
