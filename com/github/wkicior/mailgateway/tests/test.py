import os
import unittest
import tempfile
import mox
import json
from com.github.wkicior.mailgateway.model.mail import Mail
from com.github.wkicior.mailgateway.model.notification import Notification
from com.github.wkicior.mailgateway.service.mailservice import MailService
from com.github.wkicior.mailgateway.service.smtpproxy import SmtpProxy


class TestParser(unittest.TestCase):
    def setUp(self):
        self.smtp_proxy_mocker = mox.Mox()
        self.smtp_proxy = self.smtp_proxy_mocker.CreateMock(SmtpProxy)
        self.mail_service = MailService()
        self.mail_service.smtp_proxy = self.smtp_proxy


    def test_parse(self):
        self.smtp_proxy.send_mail(Mail("user@localhost", "msg", "Forecast", "Helyeah@gmail.com"))
        self.smtp_proxy_mocker.ReplayAll()
        self.mail_service.send_mail(Notification("user@localhost", "msg"))
        self.smtp_proxy_mocker.VerifyAll()

if __name__ == '__main__':
    unittest.main()


