import socket
import json
import csv
import thread
from gi.repository import Gtk


from Racer import Racer
from RacerList import RacerList
from GroupList import GroupList
from Group import Group
from ObserverList import ObserverList
from BigScreenObserver import BigScreenObserver
# from GUIthread import GUIthread
from CheatDetector import CheatDetector


UDP_IP = "127.0.0.1"
UDP_PORT = 14000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def add_observer(evnt):
    Gtk.main_quit()
    obs_name = builder.get_object("observer_entry").get_text()
    if obs_name != '':
        myobserverlist.add(BigScreenObserver(obs_name))
        for num in range(1,21):
            print builder.get_object("Obs"+str(num)).get_text()
            if builder.get_object("Obs"+str(num)).get_text() == "":
                builder.get_object("Obs"+str(num)).set_text(obs_name)
                break
    else:
        print 'need to enter a name'
    Gtk.main()

def racer_select(item, other):
    box = builder.get_object('subscribe_entry')
    box.set_text(item.get_text()[5:])

def select_observer(item, other):
    box = builder.get_object('observer_entry')
    box.set_text(item.get_text())
    obs = myobserverlist.getObserver(item.get_text())

def subscribe(evnt):
    print 'here'
    obs = builder.get_object('observer_entry').get_text()
    curr_obs = myobserverlist.getObserver(str(obs))
    if not curr_obs: return False
    racer_bib = builder.get_object('subscribe_entry').get_text()
    racer_object = myracerlist.getRacer(racer_bib)
    curr_obs.subscribe(racer_object)


handlers = {
    "add_observer": add_observer,
    "racer_select": racer_select,
    "select_observer": select_observer,
    "subscribe": subscribe
}

# setup
builder = Gtk.Builder()
builder.add_from_file("GUI/controller.glade")
controller_window = builder.get_object("window1")
controller_window.show_all()
builder.connect_signals(handlers)

f = open('SensorSimulator/SensorSimulator/bin/Debug/Group.csv')
csv_f = csv.reader(f)
MyGroupList = GroupList()
myracerlist = RacerList()
for row in csv_f:
    g = Group(row[0],row[1],row[2],row[3],row[4])
    MyGroupList.list.append(g)

f = open('SensorSimulator/SensorSimulator/bin/Debug/Racers.csv')
csv_f = csv.reader(f)
racer_counter = 0
for row in csv_f:
    racer_counter+=1
    racer = Racer(row[0], row[1], row[2])
    myracerlist.add(racer)
    MyGroupList.assign_group_to_racer(racer)
    if racer_counter <= 156:
        label = builder.get_object('Rac'+str(racer_counter))
        label.set_text('Bib #'+str(racer.bib_number))

mycheatdetector = CheatDetector()
raw_racer_list = myracerlist.get_racer_list()
# def getCheaters():
#     while True:
#         mycheatdetector.check_racers(raw_racer_list)
count = 0;
def captureData(count, myracerlist):
    while True:
        count+=1
        data, addr = sock.recvfrom(1024)
        data = json.loads(data)
        racer = myracerlist.getRacer(data['RacerBibNumber'])
        racer.update(data['SensorId'], data['Timestamp'])
        if racer.state != "OK":
            racer.detect_cheating(mycheatdetector, raw_racer_list)

        if count%10 == 0 :
            for ob in myobserverlist.list:
                # print dir(myobserverlist.list[ob])
                myobserverlist.list[ob].update()

obs = ''
myobserverlist = ObserverList()

try:
    thread.start_new_thread(captureData, (count,myracerlist))
    # thread.start_new_thread(get_inputs, ())
except Exception as e:
    print "Error: unable to start thread", e

Gtk.main()

def get_inputs():
    while True:
        print '(r) show racers\n(co) create observer\n(lo) list observers\n' + \
             '(bo) become observer\n(sub) subscribe to racer'
        user_input = raw_input(obs+'- ')
        if user_input == 'r':
            for key in myracerlist.list:
                print myracerlist.list[key]
        elif user_input == 'co':
            name = raw_input('Enter observer name: ')
            # guithread.stop()
            Gtk.main_quit()
            myobserverlist.add(BigScreenObserver(name))
            Gtk.main()
            # guithread = GUIthread()
            # guithread.start()
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
