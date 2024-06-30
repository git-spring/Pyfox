# 闭包
import time
"""
在一个外部函数中定义了一个内部函数,当内部函数引用了外部函数的变量,
并且外部函数的返回值是内部函数的引用,这个时候被引用的变量和内部函数就组成一个闭包
组成的闭包在外部函数被执行完后,引用的变量不会被立即释放,内部函数依然可以调用


1 闭包条件
　　在一个外函数中定义了一个内函数
    内函数里运用了外函数的临时变量
    并且外函数的返回值是内函数的引用

2 闭包的特点
    让外部访问函数内部变量成为可能
    局部变量会常驻在内存中
    可以避免使用全局变量
    缺点： 会造成内存泄露 (有一块内存空间被长期占用)

"""

# 创建闭包
# 变量name 和内部函数 inner 组成一个闭包
# age 没有被内部函数引用，所以不组成闭包

def outer():
    name = 'python'
    age = 19
    def inner():
        print(name)
    print(inner.__closure__)
    return inner

outer()
outer()()    # 先执行外部函数，再执行内部函数


# 闭包的应用
# 装饰器 decorator
# 装饰器的使用
def outer(fn):
    print('外部函数被调用')
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('内部函数被调用')
        print('代码耗时 %d s '% (end-start))
    return inner


@outer       #  @outer会做两件事 1.调用outer函数，2. 把被装饰的函数传递给fn (outer(fn)中的fn)
def test():
    print('被装饰的函数')
    x = 0
    for i in range(1,10000000):
        x+=1
    print(x)

test()

# todo : decorator