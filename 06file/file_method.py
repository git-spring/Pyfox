# 文件操作相关的方法
file = open('../star/test.txt', 'r+', encoding='utf8')

# 文件名称
file.name

# 读取
print(file.read())  # 默认读取全部,可指定字符
print(file.readline())  # 默认读取一行,可指定字符数
print(file.readlines())  # 默认读取全部,返回一个列表,每一行作为一个元素

# 写入
s = """\n
送元二使安西    -- 王维
渭城朝雨浥轻尘,客舍青青柳色新。
劝君更尽一杯酒,西出阳关无故人。
"""

file.write(s)  # 写入字符串
# file.write(s.encode('utf8'))   # 针对b模式的写
file.writelines(['1\n', '2\n', '3\n'])  # 可以传入一个序列

# 判断文件是否可读/可写
file.readable()
file.writable()

# 文件内的当前位置，下一次的读写会发生在文件开头这么多字节之后
file.tell()
# 改变当前光标的位置
file.seek(0, 0)  # 定位到开头

# 关闭文件   使用open 打开的文件需要自己手动关闭文件
file.close()

# 使用with open as 打开文件   (这种方式会自动关闭文件)
with open('../star/test.txt', 'r+', encoding='utf8') as file:
    line = file.readline()
    print(line)

# 对于非文本文件，只能使用二进制(b)模式操作
