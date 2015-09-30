class Racer(object):

    def __init__(self, bib_number, location, timestamp):
        self.bib_number = bib_number
        self.location = location
        self.timestamp = timestamp

    def __str__(self):
        return "racer:" + self.bib_number

    def __repr__(self):
        return "racer: " + str(self.bib_number)
