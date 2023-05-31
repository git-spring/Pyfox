# python 导入模块的方法


# 1. 直接导入整个模块
import time
# 2. from 模块名 import 函数名/变量   只导入模块中的函数/变量 (可以导入多个)
from random import randint, choice
# 3. from 模块名 import *       导入模块中所有的方法和变量
from math import *
# 4. 导入模块并起一个别名
import datetime as dt
# 5. 从模块中导入变量/函数  并起别名
from copy import deepcopy as dp

# import time          导入time模块  使用时需要带上模块名  如: time.time()
# from time import *   导入time模块中的所有内容  可以直接使用time模块中的内容   如 time()


'''
https://www.liaoxuefeng.com/wiki/1016959663602400/1017454145014176
在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。
为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。
在Python中，一个.py文件就称之为一个模块（Module）。
使用模块有什么好处？
最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。
我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。
使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。
但是也要注意，尽量不要与内置函数名字冲突。点这里查看Python的所有内置函数。
你也许还想到，如果不同的人编写的模块名相同怎么办？
为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。
现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放：
mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py
引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：
mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py
文件www.py的模块名就是mycompany.web.www，两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils。
 
自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。
 
创建自己的模块时，要注意：
模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。
'''
