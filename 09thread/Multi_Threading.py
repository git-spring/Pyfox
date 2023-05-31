# python 多线程
"""
python 多线程可以使用threading模块来实现
    有两种方法来创建多线程:
    1. 继承Thread类,并重写它的run方法;
    2. 实例化threading.Thread对象时,将线程要执行的任务函数作为参数传入线程。
"""

import threading


# 继承Thread 类，重写run 方法
class ThreadTest(threading.Thread):
    def __init__(self, thread_name):
        super(ThreadTest, self).__init__(name=thread_name)

    # 重写run方法
    def run(self):
        print("%s正在运行中......" % self.name)


for i in range(10):
    ThreadTest("09thread-" + str(i)).start()  # 启动线程


# 实例化threading.Thread对象来创建多线程
def test1():
    for idx in range(50):
        print('test111---%d' % idx)


def test2():
    for idx in range(50):
        print('test222---%d' % idx)


t1 = threading.Thread(target=test1)
t2 = threading.Thread(target=test2)

t1.start()
t2.start()
