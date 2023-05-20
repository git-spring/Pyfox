# 生成器(generator)

"""
具有yield关键字的函数就是生成器
python 中生成器是一种特殊的迭代器,生成器自动实现了__iter__ 和 __next__ 方法
生成器在迭代的过程中可以改变当前迭代值,而修改普通迭代器的当前迭代值往往会发生异常,影响程序的执行。


"""


# 定义一个生成器
def my_generator(num):
    now = 0
    while now < num:
        var = yield now  # 返回当前迭代值
        now = now + 1 if var is None else var   # var 为 None,迭代值自增1,否则重新设定当前迭代值为 var
        # now += 1

gen = my_generator(10)
next(gen)
# 打印当前的迭代值
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

# 重新设定当前迭代的值
gen.send(1)
print(gen.__next__())

print(dir(gen))  # 打印对象的方法,可以看到 __iter__  __next__ 方法都在其中
