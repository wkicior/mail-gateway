import logging
import cherrypy
from logging.handlers import RotatingFileHandler 
from flask import Flask, request, redirect, url_for
import json
from com.github.wkicior.mailgateway.model.notification import Notification, Rating
from com.github.wkicior.mailgateway.service.mailservice import MailService

app = Flask(__name__)

@app.route("/")
def index():
    app.logger.error('notifiaction called')
    return json.dumps({"status" : "OK"})


@app.route("/notifications/send", methods=['POST'])
def forecast():
    cherrypy.log('Notification send')
    mail_service = MailService()
    res = request.get_json()
    cherrypy.log('rating')
    rating = Rating(res['rating']['rating'], res['rating']['startingFrom'])

    notification = Notification(res['plan']['email'], res['message'], rating)
    mail_service.send_mail(notification)
    cherrypy.log('Notification sent: ' + str(notification))
    return redirect(url_for('index'))



if __name__ == "__main__":
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('/tmp/python.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.run()

