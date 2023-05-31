# python 中的单例模式

# python 中实现单例的几种方式

# 1. 使用__new__ 实现
"""
类在实例化的过程中,会先调用__new__ 方法申请内存(我们定义的时候没有写，通常是调用父类(object)的__new__方法),
然后调用__init__ 进行实例的初始化

"""


class Student:
    _instance = None
    flag = True

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name, age):
        # 如果不希望初始化时被覆盖，也可以是不是第一次实例化
        if self.flag:
            self.name = name
            self.age = age
            self.flag = False


s1 = Student('zhangsan', 10)
s2 = Student('lisi', 20)
print(s1 == s2)
print(s1.name)


# 2. 使用装饰器

def singleton(cls):
    instance = {}  # <class 'dict'>

    def wapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls()
        return instance[cls]

    return wapper


@singleton
class ABC:
    pass


a1 = ABC()
a2 = ABC()
print(a1 == a2)

# 3. 使用模块
"""
    python 模块就是单例的,因为在第一次导入模块的时候,会执行模块中的代码,并生成.pyc文件,
    当第二次导入的时候会直接加载.pyc文件,不会再次执行模块的代码。
    所以把相关的代码定义在模块中,就可以获得单例对象

"""
import star.Singleton as s1
import star.Singleton as s2

print(s1.p == s2.p)  # True  多次导入,两个对象是一样的
