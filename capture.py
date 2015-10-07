import socket
import json
import csv
import threading
from gi.repository import Gtk


from Racer import Racer
from RacerList import RacerList
from GroupList import GroupList
from Group import Group
from ObserverList import ObserverList
from BigScreenObserver import BigScreenObserver
# from GUIthread import GUIthread
from CheatDetector import CheatDetector
from EmailDecorator import EmailDecorator


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
            print(builder.get_object("Obs"+str(num)).get_text())
            if builder.get_object("Obs"+str(num)).get_text() == "":
                builder.get_object("Obs"+str(num)).set_text(obs_name)
                break
    else:
        print('need to enter a name')
    Gtk.main()

def clear_subscribed_list():
    for i in range(1, 21):
        builder.get_object('Sub'+str(i)).set_text(" ")

def get_subscribed_to(observer):
    for i in range(0, len(observer.subscribedtolist)):
        builder.get_object('Sub'+str(i+1)).set_text(str(observer.subscribedtolist[i].bib_number))

def racer_select(item, other):
    box = builder.get_object('subscribe_entry')
    box.set_text(item.get_text()[5:])

def select_observer(item, other):
    box = builder.get_object('observer_entry')
    box.set_text(item.get_text())
    obs = myobserverlist.getObserver(item.get_text())
    clear_subscribed_list()
    get_subscribed_to(obs)

def unsubscribe_select(item, other):
    box = builder.get_object('unsubscribe_entry')
    box.set_text(item.get_text())

def subscribe(evnt):
    obs = builder.get_object('observer_entry').get_text()
    curr_obs = myobserverlist.getObserver(str(obs))
    if not curr_obs: return False
    racer_bib = builder.get_object('subscribe_entry').get_text()
    racer_object = myracerlist.getRacer(racer_bib)
    curr_obs.subscribe(racer_object)
    get_subscribed_to(curr_obs)

def unsubscribe(evnt):
    obs = builder.get_object('observer_entry').get_text()
    curr_obs = myobserverlist.getObserver(str(obs))
    if not curr_obs: return False
    racer_bib = builder.get_object('unsubscribe_entry').get_text()
    racer_object = myracerlist.getRacer(racer_bib)
    curr_obs.unsubscribe(racer_object)
    clear_subscribed_list()
    get_subscribed_to(curr_obs)

def openemailwindow(evnt):
    Gtk.main_quit()
    b = Gtk.Builder()
    global emailbuilder
    emailbuilder = b
    b.add_from_file("GUI/emailwindow.glade")
    window = b.get_object("emailwindow")
    window.show_all()
    b.connect_signals(emailhandlers)
    Gtk.main()

def settype(evnt):
     emailbuilder.get_object("typedisplay").set_text(evnt.get_label())

def submitemail(evnt):
    typ = emailbuilder.get_object("typedisplay").get_text()
    email = emailbuilder.get_object("emailentry").get_text()
    # get observer in obs
    obs = OfficialEmailDecorator(obs, email, typ) # finish this thought it adds email and type to an observer
    emailbuilder.get_object("emailwindow").destroy()


emailbuilder = ""

emailhandlers = {
    "settype": settype,
    "submitemail": submitemail
}

handlers = {
    "add_observer": add_observer,
    "racer_select": racer_select,
    "select_observer": select_observer,
    "subscribe": subscribe,
    "unsubscribe_select": unsubscribe_select,
    "unsubscribe": unsubscribe,
    "openemailwindow": openemailwindow
}

# setup
builder = Gtk.Builder()
builder.add_from_file("GUI/controller.glade")
controller_window = builder.get_object("window1")
controller_window.show_all()
builder.connect_signals(handlers)
# for email window



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
    threading.Thread(target=captureData, args=(count,myracerlist)).start()
    # thread.start_new_thread(captureData, (count,myracerlist))
    # thread.start_new_thread(get_inputs, ())
except Exception as e:
    print("Error: unable to start thread", e)

Gtk.main()
