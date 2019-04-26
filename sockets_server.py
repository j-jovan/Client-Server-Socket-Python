import socket

########################################################

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 1))
    IP = s.getsockname()[0]
    s.close()
    return IP

########################################################

HOST = get_ip()
PORT = 6222

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print ("Server listening on "+ HOST+"...")
while(1):
	conn, addr = s.accept()	
	print addr, "says",
	while True:
	    data = conn.recv(1024)
	    if not data:
	        break
	    print data
