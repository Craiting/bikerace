from Racer import Racer

class RacerList(object):

    def __init__(self):
        self.list = {}

    # def update(self, racer):
    #     self.list[racerid] = racer

    def add(self, racer):
        self.list[racer.bib_number] = racer

    def getRacer(self, bib_number):
        return self.list[str(bib_number)]
