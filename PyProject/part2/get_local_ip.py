import socket

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

# 示例调用
print(get_local_ip())
