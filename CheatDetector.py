
class CheatDetector(object):

    def __init__(self):
        self.suspected = []
        self.cheaters = []

    def check_racers(self, racers):
        for racerx in racers:
            for racery in racers:
                if (racerx.location == racery.location and racerx.location != 0):
                    if (racerx.bib_number != racery.bib_number and racerx.group != racery.group):
                        if (int(racerx.timestamp) >= int(racery.timestamp)-3000 and int(racerx.timestamp) <= int(racery.timestamp)+3000):
                            if racerx not in self.suspected:
                                self.suspected.append(racerx)
                            else:
                                if racerx not in self.cheaters:
                                    self.cheaters.append(racerx)
                                    print('cheater',racerx)
