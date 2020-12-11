# python 魔术方法中的比较操作

class Test:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        """ 定义< 号操作符的规则 """
        return self.age<other.age

    def __le__(self, other):
        """ 定义<= 号操作符的规则 """
        return len(self.name) <= len(other.name)

    """
    __eq__(self, other)
    __ne__(self, other)
    __gt__(self, other)
    __ge__(self, other)
    这些方法原理都一样,都是用来定义比较操作符的规则
    """


t1 = Test('lisi',30)
t2 = Test('wong',20)
# print(t1 > t2)    没有实现用于比较的魔术方法,两个实例间不能直接比较
print(t1 < t2)     # 或者 t1.__lt__(t2) 这样调用

print(t1.__le__(t2))



"""
算术运算:
    __add__(self, other)	        定义加法的规则：+
    __sub__(self, other)	        定义减法的规则：-
    __mul__(self, other)	        定义乘法的规则：*
    __truediv__(self, other)	    定义真除法的规则：/
    __floordiv__(self, other)	    定义整数除法的规则：//
    __mod__(self, other)	        定义取模算法的规则：%
    __divmod__(self, other)	        定义当被 divmod() 调用时的规则
    __pow__(self, other[, modulo])	定义当被 power() 调用或 ** 运算时的规则
    __lshift__(self, other)	        定义按位左移位的规则：<<
    __rshift__(self, other)	        定义按位右移位的规则：>>
    __and__(self, other)	        定义按位与操作的规则：&
    __xor__(self, other)	        定义按位异或操作的规则：^
    __or__(self, other)	            定义按位或操作的规则：|
    __invert__(self)	            定义按位求反的行为：~


增量运算符:
    __iadd__(self, other)	        定义赋值加法的行为：+=
    __isub__(self, other)	        定义赋值减法的行为：-=
    __imul__(self, other)	        定义赋值乘法的行为：*=
    __itruediv__(self, other)	    定义赋值真除法的行为：/=
    __ifloordiv__(self, other)	    定义赋值整数除法的行为：//=
    __imod__(self, other)	        定义赋值取模算法的行为：%=
    __ipow__(self, other[, modulo])	定义赋值幂运算的行为：**=
    __ilshift__(self, other)	    定义赋值按位左移位的行为：<<=
    __irshift__(self, other)	    定义赋值按位右移位的行为：>>=
    __iand__(self, other)	        定义赋值按位与操作的行为：&=
    __ixor__(self, other)	        定义赋值按位异或操作的行为：^=
    __ior__(self, other)	        定义赋值按位或操作的行为：|=
    


一元操作符:
    __pos__(self)	                定义正号的行为：+
    __neg__(self)	                定义负号的行为：-
    __abs__(self)	                定义当被 abs() 调用时的行为

"""
