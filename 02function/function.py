# python 函数
# 函数是可重复使用的，用来实现单一，或相关联功能的代码段

# 定义
def func_name1():
    pass


# 带参数的函数
def func_name2(name):
    print(name)


# 函数内部也可以定义函数
def outer():
    x = 1

    def inner():
        print('this is a inner function')


# 调用函数
func_name1()
func_name2('lisi')
