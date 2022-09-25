from socket import *

# which host
serverName = "127.0.0.1"

# which process
serverPort = 13000

# AF_INET: IPv4, SOCK_DGRAM: UDP
# OS binds a port number to client socket implicitly
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("Input lowercase sentence:")
    if message == "quit":
        break
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    #  buffer size: 2048
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("%s send msg: %s" % (serverAddress, modifiedMessage.decode()))
clientSocket.close()
