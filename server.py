from socket import * 
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
serversock = socket(AF_INET, SOCK_STREAM)
serversock.bind(ADDR)
serversock.listen(2)

while 1:
print 'waiting for connection…'
clientsock, addr = serversock.accept()
print '…connected from:', addr
while 1:
data = clientsock.recv(BUFSIZ)
if not data: break 
clientsock.send(‘echoed’, data)
clientsock.close()
serversock.close()