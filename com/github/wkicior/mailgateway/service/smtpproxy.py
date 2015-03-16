import smtplib
class SmtpProxy(object):
    def send_mail(self, mail):
        server = smtplib.SMTP('localhost')
        server.sendmail(mail.from_address, mail.address, mail.msg)
        server.quit()
