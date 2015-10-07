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
        cheatdetector.detect_cheating(self,racerlist)

    def __str__(self):
        return "racer: " + str(self.first) +' #' + str(self.bib_number)

    def __repr__(self):
        return "racer: " + str(self.first) +' #' + str(self.bib_number)
