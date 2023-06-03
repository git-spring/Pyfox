# python 中与属性相关的魔术方法
# __getattr__


class Test:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        """
        当访问一个不存在的属性时,这个方法会被调用
        默认会抛出异常,可以自定义
        """
        print('%s 这个变量不存在' % item)
        # raise AttributeError('no attribute ',item)

    def __getattribute__(self, item):
        """ 当一个属性被访问时,会调用这个方法 """
        print('%s 属性被访问了' % item)

    def __setattr__(self, key, value):
        """ 在对一个属性设置值的时候,会调用到这个函数,每个设置值之前都会进入这个方法 """
        print('进入了__setattr__方法,执行了赋值操作 {} = {}'.format(key, value))

    def __delattr__(self, item):
        """ 当一个属性被删除时,这个方法会被调用 """
        print('%s 属性被删除了' % item)


t = Test('lisi', 20)
print(t.age)
t.city  # 访问一个不存在的属性
del t.name  # 删除属性会调用__delattr__方法
