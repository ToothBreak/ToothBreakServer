import socket
import serialComm
ip = ""
socketPort = 3300
dataSize = 512

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('waiting for connecting from client')

server.bind(("", socketPort))
server.listen(10)

while(True):
    client, addr = server.accept()
    print('client connected')
    
    # recvData form
    # 1 : bad tooth
    # 0 : good tooth
    recvData = client.recv(dataSize)
    print(recvData)
    recvData.decode("utf-8")

    serialComm.serialWrite(recvData)
    
serialComm.serialClose()
server.close()