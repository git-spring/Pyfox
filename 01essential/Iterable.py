# 可迭代对象(iterable),迭代器(iterator)和生成器(generator)


"""
可迭代对象
    python 的可迭代对象有 列表、元组、字典、集合、字符串等,迭代器可以结合for循环使用
    在python 中
        实现 __iter__ 就是一个可迭代对象
        实现 __iter__ 和 __next__ 两个方法 就是一个迭代器

    for i in d:   原理
    for循环时会调用对象d的__iter__ 方法,这个方法中需要返回一个迭代器对象
    然后会会调用迭代器中的 __next__ 方法
    注意: __iter__ 方法只会调用一次, __next__ 方法会反复调用
    这种调用方式  d.__iter__().__next__()  也是一个迭代过程，只是一次调用只会迭代一次，不会一直迭代
"""


class demo:

    def __init__(self, count):
        self.count = count

    # __iter__ 必须返回一个迭代器(iterator)对象
    def __iter__(self):
        return MyIter(self.count)
        # return self  # 可以返回自身


# 可迭代对象
class MyIter:
    start = 0

    def __init__(self, count):
        # self.start = 0
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if MyIter.start < self.count:
                flag = False
                MyIter.start += 1
                return MyIter.start - 1
            flag = True
            raise StopIteration  # 抛出异常,用于停止迭代
        except StopIteration:
            print('迭代结束了,不要再调用了')
        finally:
            if flag:
                raise StopIteration

d = demo(6)
# for 循环就是调用迭代的方法 __iter__()   __next__()
for i in d:
    print(i)

# 另一种调用方式
# print(d.__iter__().__next__())
# print(d.__iter__().__next__())
# print(d.__iter__().__next__())
# print(d.__iter__().__next__())
# print(d.__iter__().__next__())
# print(d.__iter__().__next__())


# 判断一个对象是不是可迭代对象/迭代器
from collections import Iterable, Iterator

print(isinstance(d, Iterable))
print(isinstance(d, Iterator))
