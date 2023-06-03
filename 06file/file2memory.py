# 将数据写到内存中


from io import StringIO

s_io = StringIO()
s_io.write('hello')  # 将数据写到内存

print('good', file=s_io)  # 把数据打印到内存中
print(s_io.getvalue())  # 从内存中取出数据

s_io.close()
