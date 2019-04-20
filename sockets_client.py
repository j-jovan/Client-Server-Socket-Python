import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

arg = ('192.168.5.3', 6222)

s.connect(arg)

s.sendall('Message')

s.close()