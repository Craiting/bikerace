class Racer(object):

    def __init__(self, first, last, bib_number):
        self.first = first
        self.last = last
        self.bib_number = bib_number
        self.group = "";
        self.location = 0
        self.timestamp = 0
        self.state = 'OK'

    def update(self, location, timestamp):
        if self.location != location or self.timestamp != timestamp:
            self.state = 'Changed'
        self.location = location
        self.timestamp = timestamp

    def detect_cheating(self, cheatdetector, racerlist):
        self.state = 'OK'
        for racery in racerlist:
            if (self.location == racery.location and self.location != 0):
                if (self.bib_number != racery.bib_number and self.group != racery.group):
                    if (int(self.timestamp) >= int(racery.timestamp)-3000 and int(self.timestamp) <= int(racery.timestamp)+3000):
                        if self not in cheatdetector.suspected:
                            cheatdetector.suspected.append(self)


    def __str__(self):
        return "racer: " + str(self.first) +' #' + str(self.bib_number)

    def __repr__(self):
        return "racer: " + str(self.first) +' #' + str(self.bib_number)
