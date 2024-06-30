# python socket tcp

import socket

# 客户端
# 创建socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 与服务端建立链接
skt.connect(('127.0.0.1', 9000))
# 发送消息
msg = b'Hello'
skt.send(msg)
# 接受服务端返回值并打印
res = skt.recv(100)
print(res.decode('utf-8'))
# 关闭会话链接
skt.close()

# 服务端

# 创建socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口和ip,必须为元组类型
skt.bind(('127.0.0.1', 9000))
# 侦听访问端口
skt.listen()
# 此处循环表示服务器持续提供服务
while True:
    # conn表示接受的数据流,addr表示客户端的地址
    conn, addr = skt.accept()
    # 接受客户端发送消息并打印
    msg = conn.recv(1024)
    print(msg.decode('utf-8'))
    print(msg, type(msg))
    # 为客户端返回消息,表示接受成功
    conn.send(msg.upper())
    # 关闭本次通信
    conn.close()
    # 关闭链接
    skt.close()
