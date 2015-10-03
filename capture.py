import socket
import json
import csv
import thread

from Racer import Racer
from RacerList import RacerList
from GroupList import GroupList
from Group import Group
from ObserverList import ObserverList
from BigScreenObserver import BigScreenObserver
from GUIthread import GUIthread
from CheatDetector import CheatDetector


UDP_IP = "127.0.0.1"
UDP_PORT = 14000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# setup
f = open('SensorSimulator/SensorSimulator/bin/Debug/Group.csv')
csv_f = csv.reader(f)
MyGroupList = GroupList()
myracerlist = RacerList()
for row in csv_f:
    g = Group(row[0],row[1],row[2],row[3],row[4])
    MyGroupList.list.append(g)

f = open('SensorSimulator/SensorSimulator/bin/Debug/Racers.csv')
csv_f = csv.reader(f)
for row in csv_f:
    racer = Racer(row[0], row[1], row[2])
    myracerlist.add(racer)
    MyGroupList.assign_group_to_racer(racer)

mycheatdetector = CheatDetector()
raw_racer_list = myracerlist.get_racer_list()
count = 0;
def captureData(count, myracerlist):
    while True:
        count+=1
        data, addr = sock.recvfrom(1024)
        data = json.loads(data)
        racer = myracerlist.getRacer(data['RacerBibNumber'])
        racer.update(data['SensorId'], data['Timestamp'])

        if count%20 == 0 :
            for ob in myobserverlist.list:
                # print dir(myobserverlist.list[ob])
                myobserverlist.list[ob].update()

try:
    thread.start_new_thread(captureData, (count,myracerlist))
    thread.start_new_thread(mycheatdetector.check_racers, (raw_racer_list))
except Exception as e:
    print "Error: unable to start thread", e


guithread = GUIthread()
guithread.start()
obs = ''
myobserverlist = ObserverList()
while True:
    print '(r) show racers\n(co) create observer\n(lo) list observers\n' + \
         '(bo) become observer\n(sub) subscribe to racer'
    user_input = raw_input(obs+'- ')
    if user_input == 'r':
        for key in myracerlist.list:
            print myracerlist.list[key]
    elif user_input == 'co':
        name = raw_input('Enter observer name: ')
        guithread.stop()
        myobserverlist.add(BigScreenObserver(name))
        guithread = GUIthread()
        guithread.start()
    elif user_input == 'bo':
        obs = raw_input('observer name: ')
        myobserverlist.getObserver(obs)
    elif user_input == 'lo':
        for name in myobserverlist.list:
            print myobserverlist.getObserver(name)
    elif user_input == 'sub':
        racer_bib = raw_input('racer bib number: ')
        curr_obs = myobserverlist.getObserver(obs)
        racer_object = myracerlist.getRacer(racer_bib)
        curr_obs.subscribe(racer_object)
    elif user_input == 'cheat':
        print mycheatdetector.suspected
