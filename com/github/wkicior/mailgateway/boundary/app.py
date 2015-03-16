from flask import Flask, request, redirect, url_for
#from wwoproxy.service.service import WwoService
import json
from com.github.wkicior.mailgateway.model.notification import Notification
from com.github.wkicior.mailgateway.service.mailservice import MailService

app = Flask(__name__)

@app.route("/")
def index():
    return json.dumps({"status" : "OK"})


@app.route("/mail-gateway/notification/", methods=['POST'])
def forecast():
    mail_service = MailService()
    res = request.get_json()
    notification = Notification(res['plan']['email'], res['message'])
    mail_service.send_mail(notification)
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run()

