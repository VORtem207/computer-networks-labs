import time

from socket import *
from datetime import datetime

server_address = ('localhost', 12000)

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

rtts = []


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
        rtts.append(rtt)

        print(f"Answer: {answer.decode()} | RTT: {rtt}")

    except timeout:
        print("Request timed out")


packet_loss_rate = int((10 - len(rtts)) / 10 * 100)

if len(rtts) > 0:
    min_rtt = min(rtts)
    max_rtt = max(rtts)
    avg_rtt = sum(rtts)/len(rtts)

    print(
        f"Statistics: Min RTT: {min_rtt}"
        f" | Max RTT: {max_rtt}"
        f" | Average RTT: {avg_rtt}"
        f" | Package loss rate: {packet_loss_rate}%"
    )

else:
    print(f"No RTTs found | Package loss rate: {packet_loss_rate}%")


client_socket.close()
