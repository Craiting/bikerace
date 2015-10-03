from Racer import Racer

class RacerList(object):

    def __init__(self):
        self.list = {}

    def add(self, racer):
        self.list[racer.bib_number] = racer

    def getRacer(self, bib_number):
        return self.list[str(bib_number)]

    def get_racer_list(self):
        rlist = []
        for racer in self.list:
            rlist.append(self.list[racer])
        return rlist
