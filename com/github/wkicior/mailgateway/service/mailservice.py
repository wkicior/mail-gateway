from com.github.wkicior.mailgateway.model.mail import Mail
from com.github.wkicior.mailgateway.service.smtpproxy import SmtpProxy

__author__ = 'disorder'


class MailService(object):
    def __init__(self):
        self.smtp_proxy = SmtpProxy()

    def send_mail(self, notification):
        mail = Mail(notification.mail, notification.msg, "Forecast", "Helyeah@gmail.com")
        self.smtp_proxy.send_mail(mail)