import socket
from Racer import Racer
from RacerList import RacerList
import json

UDP_IP = "127.0.0.1"
UDP_PORT = 14001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
count = 0;
racerlist = RacerList()
while True:
    count+=1
    data, addr = sock.recvfrom(1024)
    data = json.loads(data)
    racer = Racer(data['RacerBibNumber'], data['SensorId'], data['Timestamp'])
    if data['RacerBibNumber'] not in RaceList:
        RaceList[data['RacerBibNumber']] = racer
    else:
        print 'pass'

    # print data
    if count%150 == 0 :
        print RaceList,len(RaceList),"\n\n"
