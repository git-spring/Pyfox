# sys  模块提供了一系列有关Python运行环境的变量和函数

import sys

# 命令行参数list 第
arg0 = sys.argv[0]   # 第 0 个是文件本身
arg1 = sys.argv[1]   # 第 1 个参数
arg2 = sys.argv[2]   # 第 2 个参数
# 返回模块的搜索路径,初始化时使用PYTHONPATH环境变量的值 ( 引用的模块会从这些路径下去寻找)
dir_list = sys.path
# 返回所有导入的模块的列表
sys.modules.keys()
# 返回系统导入的模块字段,key是模块名,value是模块
sys.modules
# 获取python 解释器的版本信息
sys.version
# 返回操作平台名称
sys.platform
# 标准输入,可以循环输入
sys.stdin.read()
# 标准输出
sys.stdout.write('aaaa')
sys.stdout.writeline('bbbb') # 无换行输出
# 错误输出
sys.stderr.write('')

# 输出重定向   # 对应的内容会输出到文件中
# sys.stdin = open('../star/stdin.txt','w',encoding='utf8')      # 从文件输入
sys.stdout = open('../star/stdout.txt','w',encoding='utf8')
print('stdout output 标准输出')
sys.stderr = open('../star/stderr.txt','w',encoding='utf8')
print(1/0)

# 退出程序,指定状态码
sys.exit(0)