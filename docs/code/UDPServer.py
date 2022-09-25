from socket import *

serverPort = 13000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print("receive: %s; send to %s msg: %s" % (message.decode(), clientAddress, modifiedMessage))
    serverSocket.sendto(modifiedMessage.encode(),
                        clientAddress)
