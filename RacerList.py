from Racer import Racer

class RacerList(object):

    def __init__(self):
        self.list = {}

    def update(self, racerid, racer):
        self.list[racerid] = racer
