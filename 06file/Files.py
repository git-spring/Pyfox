# python 的文件操作
# open() 函数用于打开一个文件,创建一个 file 对象,相关的方法才可以调用它进行读写


context = open('../star/test.txt','r',encoding='utf8')
print(context.read())

context = open('../star/test.txt','w')
context.write('writefiles')

context = open('../star/test.txt','a')
context.write('appendfiles')


# 文件的打开方式
"""
    r : 只读模式,打开文件后只能读取,不能写入内容,python 默认的方式
    w : 写入模式,只能写入,不能读取文件,如果文件存在则会覆盖里面的内容,不存在会新建文件
    b : 以二进制的形式打开文件  
    a : 追加
    另外的方式详见文档   https://www.runoob.com/python3/python3-func-open.html
组合
    rb : 以二进制的形式读取
    rw : 以二进制的形式写入
"""

