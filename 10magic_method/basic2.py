# __len__,__repr__,__str__


class Test:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.city = args[2]
        self.lens = len(args)

    def __len__(self):
        """
        定义len(obj)时的动作,没有__len__方法不能使用len方法
        这里是返回实例化时的参数个数
        """
        return self.lens

    def __repr__(self):
        """
        定义直接打印实例时的输出信息,默认是类名和地址
        重写了此方法后,可以直接使用repr(obj)
        """
        return '{} [ name = {}, age = {}, city = {} ]'.format(self.__class__, self.name, self.age, self.city)

    def __str__(self):
        """ 与__repr__ 方法作用相同"""
        print(11111)
        return '{} [ name = {}, age = {}, city = {} ]'.format(self.__class__, self.name, self.age, self.city)


t = Test('lisi', 20, 'earth')
print(len(t))
print(t)
print(repr(t))
print(str(t))
