
class CheatDetector(object):

    def __init__(self):
        self.suspected = []
        self.cheaters = []

    def detect_cheating(self, racer, racerlist):
        for racery in racerlist:
            if (racer.location == racery.location and racer.location != 0):
                if (racer.bib_number != racery.bib_number and racer.group != racery.group):
                    if (int(racer.timestamp) >= int(racery.timestamp)-3000 and int(racer.timestamp) <= int(racery.timestamp)+3000):
                        if racer not in self.suspected:
                            self.suspected.append(racer)
                            print('suspects',self.suspected)
                        elif racer not in self.cheaters:
                            self.cheaters.append(racer)
                            print('cheaters',self.cheaters)
