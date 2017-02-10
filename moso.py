import socket
import time
from struct import unpack

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 1234))

while 1 :
    data, (address, port) = s.recvfrom(68)
    level = address.split('.')[-1] # last octett of IP is the level number
    print data
    #drier = str(unpack('>H', data[4:6]))
    #washingMachine = str(unpack('>H', data[6:8]))
    #print washingMachine
    #time.sleep(5)
    # szaritogep = str(unpack('>H', data[4:6])[0])
    # mosogep = str(unpack('>H', data[6:8])[0])
