from flask import Flask, request, render_template, Response
from datetime import datetime
import cv_creator as cv 

app = Flask(__name__)

# @app.route("/", methods=["POST", "GET"])
# def index():
#     return render_template("index.html")

@app.route("/CVTemplate1", methods=['POST'])
def createTemplate1():
    resp = Response()
    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response = request.get_json()
    print("im here")
    print(response)
    cv.template1()
    return "200"
 
if __name__ == "__main__":
    app.run()