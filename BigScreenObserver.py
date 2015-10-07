from gi.repository import Gtk

from Observer import Observer


class BigScreenObserver(Observer):

    def __init__(self, name):
        super(BigScreenObserver, self).__init__(name)
        self.builder = Gtk.Builder()
        self.builder.add_from_file("GUI/BigScreen.glade")
        self.window = self.builder.get_object("window1")
        self.window.show_all()
        # self.builder.get_object("label1").set_text('hi')

    def update(self):
        for idx, racer in enumerate(self.subscribedtolist):
            label = 'label' + str(idx+1)
            text = str(racer.first) + '\t' + str(racer.last) + '\t' \
            + str(racer.bib_number) + '\t' + str(racer.location) \
            + '\t' + str(racer.timestamp)
            try:
                self.builder.get_object(label).set_text(text)
            except:
                print('cant')

    def clear_screen(self):
        for i in range(1,14):
            self.builder.get_object('label'+str(i)).set_text(' ')
