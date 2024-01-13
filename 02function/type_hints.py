# 类型注解 tpye hitns
# 对变量,方法形参,返回值等进行注解,提高代码可读性
# 非强制,也不能限定对象的类型,仅作为提示


# 基础数据类型注解
age: int = 10
name: str = 'zhangsan'

# 基础容器类型注解
my_list: list = [1, 2, 4]
my_tuple: tuple = (5, 6,)
my_dict: dict = {'name': 'lisi', 'age': 19}

# 在注释中注解
my_list1 = [1, 2, 4]   # type:list
my_tuple1 = (5, 6,)    # type:tuple

# 注释并不一定和对象类型一致,因为只是作为提示
my_list2:list = {'name': 'lisi', 'age': 19}  # 语法可以通过,执行无问题



## 方法的注解
# -> int 表示返回值是int类型
def add(a:int,b:int) -> int:
    return a+b


## Union 联合注解
# 当对象可以有多个类型的时候可以使用联合注解
# 需导入包 from typing import Union

from typing import Union, Optional
# 这里表示函数unpack的形参建议是list或tuple
def unpack(pack:Union[list,tuple]) :
    first = pack[0]
    return first



## Optional
# 可选的,当可能是我们期望的类型,或者为空的时候,可以选择Optional做注解
# 参数可能为int或者None
# 这里可能返回int,也有可能返回None, 所以用Optional比较合适
def even(a:Optional[int]) -> Optional[int]:
    if a == None:
        return None
    elif a/2 == 0:
        return a

