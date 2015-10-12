from Observer import Observer

class OfficialEmailDecorator(Observer):

    def __init__(self, observer, email, obstype):
        super(OfficialEmailDecorator,self).__init__(observer.name)
        self.email = email
        self.type = obstype
