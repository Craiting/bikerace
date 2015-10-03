class Observer(object):

    def __init__(self, name):
        self.name = name
        self.subscribedtolist = []

    def subscribe(self, racer):
        if racer not in self.subscribedtolist:
            self.subscribedtolist.append(racer)
            print 'subscribed to ' + str(racer)

    def unsubscribe(self, racer):
        self.subscribedtolist.remove(racer)

    def __repr__(self):
        return "<observer: " + self.name + ">"
