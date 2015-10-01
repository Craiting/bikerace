import socket
import json
import csv
import thread

from Racer import Racer
from RacerList import RacerList
from GroupList import GroupList
from Group import Group


UDP_IP = "127.0.0.1"
UDP_PORT = 14000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# setup
f = open('SensorSimulator/SensorSimulator/bin/Debug/Group.csv')
csv_f = csv.reader(f)
MyGroupList = GroupList()
for row in csv_f:
    g = Group(row[0],row[1],row[2],row[3],row[4])
    MyGroupList.list.append(g)
count = 0;
myracerlist = RacerList()
def captureData(count, myracerlist):
    while True:
        count+=1
        data, addr = sock.recvfrom(1024)
        data = json.loads(data)
        racer = Racer(data['RacerBibNumber'], data['SensorId'], data['Timestamp'])
        MyGroupList.assign_group_to_racer(racer)
        if data['RacerBibNumber'] not in myracerlist.list:
            myracerlist.list[data['RacerBibNumber']] = racer
        else:
            pass

        # print data
        if count%150 == 0 :
            pass
            # print myracerlist.list,len(myracerlist.list),"\n\n"


try:
    thread.start_new_thread(captureData, (count,myracerlist))
except Exception as e:
    print "Error: unable to start thread", e

obs = ''
while True:
    print '(r) show racers\n(co) create observer\n(lo) list observers\n' + \
         '(bo) become observer'
    user_input = raw_input(obs+'- ')
    if user_input == 'r':
        for racer in myracerlist.list:
            print racer
    elif user_input == 'co':
        name = raw_input('Enter observer name: ')
        print name
    elif user_input == 'bo':
        obs = raw_input('observer: ')
