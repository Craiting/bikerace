import smtplib
from email.mime.text import MIMEText

class EmailDecorator(object):

    def __init__(self, obs, email):
        self.decorated = obs
        self.email = email
        self.decorated = {'email':email,'observer':obs}

    # This function is not completely working.
    def send_emails(self):
        fp = open(textfile, 'rb')
        msg = MIMEText(fp.read())
        fp.close()
        msg['Subject'] = 'Email from Bike Race'
        msg['From'] = 'agro@gmail.com'
        msg['To'] = self.email
        s = smtplib.SMTP('localhost')
        s.sendmail('agro@gmail.com', [self.email], msg.as_string())
        s.quit()
