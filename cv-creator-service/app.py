from flask import Flask, request, render_template, Response, make_response, jsonify
from datetime import datetime
import cv_creator as cv 

app = Flask(__name__)

# @app.route("/", methods=["POST", "GET"])
# def index():
#     return render_template("index.html")

@app.route("/CVTemplate1", methods=['POST', "OPTIONS"])
def createTemplate1():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
    elif request.method == "POST": # The actual request following the prefligh
        info = jsonify({"order_id": 123, "status": "shipped"})
        #resp = Response()
        #resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        #response = request.get_json()
        #print("im here")
        #print(response)
        #cv.template1()
        return _corsify_actual_response(info)
 
def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run()