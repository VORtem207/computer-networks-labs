import time

from socket import *
from datetime import datetime

server_address = ('localhost', 12000)

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)


for i in range(1, 11):
    message = f"Ping {i} {datetime.now().strftime("%H:%M:%S")}"
    print(message)

    start_time = time.perf_counter()

    client_socket.sendto(
        message.encode(),
        server_address,
    )

    try:
        answer, address = client_socket.recvfrom(2048)

        end_time = time.perf_counter()
        rtt = end_time - start_time

        print(f"Answer: {answer.decode()} | RTT: {rtt}")

    except timeout:
        print("Request timed out")


client_socket.close()
