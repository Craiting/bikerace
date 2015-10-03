import threading
from gi.repository import Gtk

class GUIthread(threading.Thread):
    def run(self):
        Gtk.main()
    def stop(self):
        Gtk.main_quit()
