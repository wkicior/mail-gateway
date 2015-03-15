from flask import Flask, request, Response
#from wwoproxy.service.service import WwoService
import json

app = Flask(__name__)

@app.route("/mail-gateway/notification/")
def forecast():
    #wwo_service = WwoService()
    #forecast_dic =  wwo_service.get_forecast(latitude, longitude)
    res = json.dumps({"Status" : "OK"})
    return Response(response=res, status=200, mimetype="application/json")

@app.route("/")
def index():
    return json.dumps({"status" : "OK"})

if __name__ == "__main__":
    app.run()

