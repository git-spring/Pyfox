from random import randint
# from math import *
import math

print(math.pi)


class Test:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name,age)


    def __call__(self, *args, **kwargs):
        print('{},{},{}'.format(args[0],args[1],args[2]))

t = Test('lisi',20)
t('age',30,1111)