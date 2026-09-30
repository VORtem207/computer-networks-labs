import sys

from socket import *


print(sys.argv)

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_host, server_port))

message = f"GET /{filename} HTTP/1.1\r\n\r\n"
client_socket.send(message.encode())


while True:
    file = client_socket.recv(1024)

    if b'' == file:
        break

    print(file.decode(), end="")


client_socket.close()
