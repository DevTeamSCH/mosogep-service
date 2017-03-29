import socket
import time
from struct import unpack

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 1234))

while 1:
    data, (address, port) = s.recvfrom(68)
    level = address.split('.')[-1] # last octett of IP is the level number
    #drier = str(unpack('>H', data[4:6]))
    #washingMachine = str(unpack('>H', data[6:8]))
    #print washingMachine
    #time.sleep(5)

    print('address:', address)
    print('port:', port)
    print('level:', level)

    print('data:', data)
    drier, wahing_machine = unpack('>HH', data[4:8])
    print('szaritogep:', drier)
    print('mosogep:', wahing_machine)
    print()
