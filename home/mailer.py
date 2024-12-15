from __future__ import print_function

import base64
from email.message import EmailMessage
import smtplib, ssl

class Mailer():

    def __init__(self, name, send_to, message):
        self.smpt_server ={"url": "localhost", "port": 1025}
        self.app_email= {"email": "revolt@localhost.com", "passwd":"Kousemaeker@100"}
        self.name=name
        self.send_to=send_to
        self.message=message


    def send(self):
        """Create and insert a draft email.
        Print the returned draft's message and id.
        Returns: Draft object, including draft id and message meta data.

        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
        """
    
    
        message = EmailMessage()

        message.set_content('This is automated draft mail')

        message['To'] = self.send_to
        message['From'] = self.app_email["email"]
        message['Subject'] = 'Automated Mail'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        smtp_ins = smtplib.SMTP(self.smpt_server["url"])
        #smtp_ins.set_debuglevel(True)
        smtp_ins.ehlo()
        smtp_ins.starttls()
        smtp_ins.ehlo()
        
        #smtp_ins.login(self.app_email["email"], self.app_email["email"])
        smtp_ins.sendmail(self.app_email["email"], self.send_to, "Hey")
        print("complete")
    
        #print(F'An error occurred: {error}')
        msg = None
    
        return msg


m=Mailer("James", "cadetcyuzuzo@gmail.com", "Hi. Test.")
m.send()