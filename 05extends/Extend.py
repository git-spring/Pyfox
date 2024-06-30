# python 中的继承

class A(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


class B(A):
    def __init__(self, name, age,school):
        A.__init__(self,name,age)
        self.school=school
        super(B, self).__init__(name,age)


class C(A):
    def __init__(self, name, age):
        self.name = name
        self.age = age
