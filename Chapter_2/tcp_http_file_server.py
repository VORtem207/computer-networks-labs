from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789


serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()

        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f.read()

        connectionSocket.send("HTTP/1.1 200 OK".encode())
        connectionSocket.send("\r\n\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found".encode())
        connectionSocket.send("\r\n\r\n".encode())

        connectionSocket.close()

serverSocket.close()
sys.exit()
