from socket import *
from time import sleep

serverName = "127.0.0.1"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# serverPort is welcome port
serverSocket.bind((serverName, serverPort))

# wait and listen for client requests
# max number of queued connections
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    while True:
        sentence = connectionSocket.recv(1024).decode()
        # instead of server first close connection, server wait for client to close
        # thus avoid TIME_WAIT and address bind error
        if not sentence: break
        capitalizedSentence = sentence.upper()
        # TCP connection accepted, no need to add destination addr
        print("receive: %s from %s, send: %s" % (sentence, addr, capitalizedSentence))
        connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
