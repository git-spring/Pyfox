# python socket udp
# udp 没有严格的客户端和服务端,两个都可以发送和接收数据


import socket

# 客户端 发送数据
# 创建socket
skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 创建发送消息和发送目标
msg = b'Hello world'
addr = ('127.0.0.1', 9090)
skt.sendto(msg, addr)
# 接受回复
rst = skt.recvfrom(1024)
print(rst)
print('client done')
# 关闭链接
skt.close()

# 服务端 接收数据
# 创建socket
skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定地址和端口
skt.bind(('127.0.0.1', 9090))
# 循环
while True:
    # 调用接受消息
    data, addr = skt.recvfrom(1024)
    # 接受成功回复消息
    rst = b'I am fine'
    skt.sendto(rst, addr)
    print('server Done')
    # 关闭链接
    skt.close()
