from datetime import datetime
from com.github.wkicior.mailgateway.model.mail import Mail
from com.github.wkicior.mailgateway.service.smtpproxy import SmtpProxy

__author__ = 'disorder'


class MailService(object):
    def __init__(self):
        self.smtp_proxy = SmtpProxy()

    def send_mail(self, notification):
        mail = Mail(notification.mail, self.compose_message(notification), "Forecast", "Helyeah@gmail.com")
        self.smtp_proxy.send_mail(mail)

    def compose_message(self, notification):
        msg =  notification.msg + "\n" + notification.rating.rating + " starting from "
        msg = msg + datetime.strftime(notification.rating.starting_from, '%d-%m-%Y %H:%M')
        return msg

    
