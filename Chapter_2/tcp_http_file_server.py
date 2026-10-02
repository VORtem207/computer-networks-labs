import threading

from socket import *


serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789


serverSocket.bind(('', serverPort))
serverSocket.listen(1)


def handle_client(client_socket: socket):
    try:
        message = client_socket.recv(1024).decode()

        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f.read()

        client_socket.send("HTTP/1.1 200 OK".encode())
        client_socket.send("\r\n\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            client_socket.send(outputdata[i].encode())

        client_socket.send("\r\n".encode())
        client_socket.close()

    except IOError:
        # Send response message for file not found
        client_socket.send("HTTP/1.1 404 Not Found".encode())
        client_socket.send("\r\n\r\n".encode())

        client_socket.close()


while True:
    print('Ready to serve...')
    client_socket, addr = serverSocket.accept()
    t = threading.Thread(target=handle_client, args=(client_socket,))
    t.start()
