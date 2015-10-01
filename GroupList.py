from Group import Group
from Racer import Racer

class GroupList(object):

    def __init__(self):
        self.list = [] # list of the groups

    def assign_group_to_racer(self, racer):
        for group in self.list:
            if int(racer.bib_number) >= int(group.low_bib) and int(racer.bib_number) <= int(group.hi_bib):
                racer.group = group
                break
