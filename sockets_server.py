import socket

HOST = '192.168.5.3'
PORT = 6222

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print ("Server started, listening...")
while(1):
	conn, addr = s.accept()	
	print addr, "says",
	while True:
	    data = conn.recv(1024)
	    if not data:
	        break
	    print data