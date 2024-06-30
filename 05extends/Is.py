# is isinstance  issubclass

# is 用来比较是不是同一个对象,比较的是两个对象的地址

class A:
    pass

a1 = A()
a2 = A()

print(a1 is a2)      # id(a1)==id(a2)?
print(type(a1) == A)

# isinstance 用来判断一个对象是否由指定类或其父类的实例

class B(A):
    pass

b1 = B()

print(isinstance(b1,B))    # True
print(isinstance(b1,A))    # True


# issubclass  用来判断一个类是否是另一个类的子类

print(issubclass(B,A))     # True
