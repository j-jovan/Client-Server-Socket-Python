import socket

HOST = '192.168.5.3'  # Standard loopback interface address (localhost)
PORT = 6222        # Port to listen on (non-privileged ports are > 1023)

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