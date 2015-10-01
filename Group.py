class Group(object):

    def __init__(self, gid, name, starting_time, low_bib, hi_bib):
        self.gid = gid
        self.name = name
        self.starting_time = starting_time
        self.low_bib = low_bib
        self.hi_bib = hi_bib

    def __str__(self):
        return "<group:" + str(self.gid) + '-' + self.name + '>'

    def __repr__(self):
        return "<group:" + str(self.gid) + '-' + self.name + '>'
