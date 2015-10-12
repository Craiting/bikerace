
class EmailDecorator(object):

    def __init__(self, obs, email):
        self.decorated = obs
        self.email = email
        self.decorated = {'email':email,'observer':obs}
