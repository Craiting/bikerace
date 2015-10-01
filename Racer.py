class Racer(object):

    def __init__(self, first, last, bib_number):
        self.first = first
        self.last = last
        self.bib_number = bib_number
        self.group = "";
        self.location = 0
        self.timestamp = 0

    def update(self, location, timestamp):
        self.location = location
        self.timestamp = timestamp


    def __str__(self):
        return "racer: " + str(self.first) +' #' + str(self.bib_number)

    def __repr__(self):
        return "racer: " + str(self.first) +' #' + str(self.bib_number)
