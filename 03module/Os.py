# os 模块提供了多数操作系统的功能接口函数
# 当os模块被导入后,它会自适应于不同的操作系统平台,根据不同的平台进行相应的操作

import os
import stat

# 查看正在使用的工作平台
os.name
# 查看当前所在路径
os.getcwd()
# 列出指定目录下所有的文件和目录名, . 表示当前目录  .. 表示上级目录
os.listdir('E:\\05pythonProject\Pyfox\\03module')
# 删除指定的文件,文件不存在会报错
os.remove('test.py')
os.unlink('test.py')
# 删除指定目录,只能删除空目录  删除非空目录, 使用shutil.rmtree()
os.rmdir('../test')
# 删除多层目录
os.removedirs('abc/test')
# 创建目录 只能创建一层
os.mkdir('test')
# 创建多层目录
os.makedirs('abc/test')
# 重命名文件
os.rename('test.py', 'Test1.py')
# 改变当前工作目录
os.chdir('..')
# 查看文件属性
os.stat('Test1.py')
# 修改文件权限
os.chmod('Test1.py', stat.S_IWOTH)

## os.path

# 将文件路径和文件名分割(会将最后一个目录作为文件名而分离)
os.path.split('E:\\05pythonProject\Pyfox\\03module\Test.py')  # ('E:\\05pythonProject\\Pyfox\\03module', 'test.py')
# 将文件路径和文件扩展名分割成一个元组
os.path.splitext('E:\\05pythonProject\Pyfox\\03module\Test.py')  # ('E:\\05pythonProject\\Pyfox\\03module\\test', '.py')
# 返回路径的目录部分
dirname = os.path.dirname('E:\\05pythonProject\Pyfox\\03module\Test.py')  # E:\05pythonProject\Pyfox\03module
# 返回路径的文件名部分
basename = os.path.basename('E:\\05pythonProject\Pyfox\\03module\Test.py')  # test.py
# 将文件路径和文件名凑成完整文件路径
os.path.join(dirname, basename)
# 获取文件的绝对路径
os.path.abspath('test.py')
# 判断是否是绝对路径
os.path.isabs('test.py')
# 获取文件或者目录是否存在
os.path.exists('../03module')
# 判断是否是目录
os.path.isdir('../03module')
# 判断是否是文件
os.path.isfile('test.py')
# 返回文件大小
os.path.getsize('test.py')
