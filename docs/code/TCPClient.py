from socket import *

serverName = "127.0.0.1"
serverPort = 12000

# AF_INET: IPv4; SOCK_STREAM: TCP
# OS specify port number implicitly
clientSocket = socket(AF_INET, SOCK_STREAM)
# TCP is connection oriented handshake
clientSocket.connect((serverName, serverPort))
while True:
    sentence = input("Input lowercase sentence:")
    # no need to add destination address
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print("From Server: ", modifiedSentence.decode())
    if sentence == "quit":
        clientSocket.close()
        break


