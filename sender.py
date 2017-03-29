import socket
from struct import pack

UDP_IP = "127.0.0.1"
UDP_PORT = 1234
print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

DRIER = 56789
WASHING_MACHINE = 290
DATA = pack('>iHH', 1234567890, DRIER, WASHING_MACHINE)  # first 4 bytes is ip
print('szarito:', DRIER)
print('mosogep:', WASHING_MACHINE)
print('data:', DATA)

while True:
    sock.sendto(DATA, (UDP_IP, UDP_PORT))
