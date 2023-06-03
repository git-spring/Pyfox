# raise 关键字
# 程序运行时遇到异常,会自动抛出异常,停止程序
# 但是python 中也可以手动抛出异常, raise 关键字用于手动抛出异常


class Person:
    pass


try:

    obj = Person()
    if obj is None:
        print('对象是None')
        raise NameError('Name not found globally.')  # 手动抛出异常
    print('{} 初始化成功! '.format(obj))
except TypeError as et:  # 这里可以捕获其它异常
    print('ERROR %$#^&*@#%')
finally:
    print('代码结束')
