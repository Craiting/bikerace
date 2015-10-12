from EmailDecorator import EmailDecorator

class officialEmailList(EmailDecorator):

    def __init(self):
        super(officialEmailList, self).__init__(observer,email)
        self.list = {}

    def add(self, decorated):
        self.list[decorated.email] = decorated
