# python 中基本的魔术方法

#  __new__ ,__init__,__del__,__call__

class Test:

    def __new__(cls, *args, **kwargs):
        """ 对象实例化时最先调用的方法,用于向计算机申请内存,一般不写,会调用父类的方法 """
        print(args)
        print('__new__方法被调用了')
        return super().__new__(cls)

    def __init__(self, name, age):
        """ 对象实例化时在__new__之后调用,用于初始化对象 """
        print('对象开始初始化')
        self.name = name
        self.age = age

    def __del__(self):
        """ 对象被销毁时会被调用 """
        print('这个实例将被销毁,__del__方法被调用')

    def __call__(self, *args, **kwargs):
        """ 实现__call__方法可以让类的实例像方法一样被调用 """
        print('__call__方法被调用了,参数是:{},{},{}'.format(args[0], args[1], args[2]))


t = Test('lisi', 20)
t('wangwu', 30, 'sz')  # 实现__call__方法后,实例可以像方法一样调用
