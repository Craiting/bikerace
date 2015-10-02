from Observer import Observer

class ObserverList:

    def __init__(self):
        self.list = {}

    def add(self, observer):
        self.list[observer.name] = observer

    def getObserver(self, name):
        try:
            return self.list[str(name)]
        except:
            print "no observer named " + name
