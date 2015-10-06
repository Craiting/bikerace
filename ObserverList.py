from Observer import Observer

class ObserverList:

    def __init__(self):
        self.list = {}

    def add(self, observer):
        self.list[observer.name] = observer

    def get_list(self):
        full_list = []
        for item in self.list:
            full_list.append(item)
        return full_list

    def getObserver(self, name):
        try:
            return self.list[str(name)]
        except:
            print("no observer named " + name)
            return False
