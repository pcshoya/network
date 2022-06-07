import socket

res = socket.getaddrinfo('kbs.co.kr', 80)
print(res)

sock = socket.socket()
print(sock)