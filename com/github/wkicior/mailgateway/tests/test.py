import os
import unittest
import tempfile
import mox
import json
from com.github.wkicior.mailgateway.model.mail import Mail
from com.github.wkicior.mailgateway.model.notification import Notification, Rating
from com.github.wkicior.mailgateway.service.mailservice import MailService
from com.github.wkicior.mailgateway.service.smtpproxy import SmtpProxy


class TestParser(unittest.TestCase):
    def setUp(self):
        self.smtp_proxy_mocker = mox.Mox()
        self.smtp_proxy = self.smtp_proxy_mocker.CreateMock(SmtpProxy)
        self.mail_service = MailService()
        self.mail_service.smtp_proxy = self.smtp_proxy


    def test_parse(self):
        self.smtp_proxy.send_mail(Mail("user@localhost", "msg\nPROMISING starting from 12-12-2010 12:00", "Forecast", "Helyeah@gmail.com"))
        self.smtp_proxy_mocker.ReplayAll()
        
        self.mail_service.send_mail(Notification("user@localhost", "msg", Rating("PROMISING", "2010-12-12T12:00:00.000Z")))
        self.smtp_proxy_mocker.VerifyAll()


if __name__ == '__main__':
    unittest.main()


