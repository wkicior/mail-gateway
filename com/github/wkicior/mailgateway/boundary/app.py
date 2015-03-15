from flask import Flask, request, Response, redirect, url_for
#from wwoproxy.service.service import WwoService
import json

app = Flask(__name__)

@app.route("/")
def index():
    return json.dumps({"status" : "OK"})


@app.route("/mail-gateway/notification/", methods=['POST'])
def forecast():
    #wwo_service = WwoService()
    #forecast_dic =  wwo_service.get_forecast(latitude, longitude)
    #res = json.dumps(request.form['plan'])
    res = request.get_json()
    print res
    print "OK"
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run()

