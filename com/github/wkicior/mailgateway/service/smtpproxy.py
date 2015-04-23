import smtplib
import cherrypy
from com.github.wkicior.mailgateway.settings import *
class SmtpProxy(object):
    def send_mail(self, mail):
        try:
            server = smtplib.SMTP(SMTP_SERVER)
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            message = 'Subject: %s\n\n%s' % ('Notification', mail.msg)
            server.sendmail(mail.from_address, mail.address, message)
            server.quit()
        except Exception as e:
            cherrypy.log('error!' + str(e))
