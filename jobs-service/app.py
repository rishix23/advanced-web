from flask import Flask, request, make_response, jsonify
from datetime import datetime
import jobs_request_handler
import job_request_handler

app = Flask(__name__)


@app.route("/", methods=['GET','POST','OPTIONS'])
def jobs():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
    else:
        return  _corsify_actual_response(jsonify(jobs_request_handler.handle(request)))


@app.route("/<id>", methods=job_request_handler.list_methods())
def job(id):
    return job_request_handler.handle(request, id)

#Necessary headers to allow frontend to authenticate api

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
    app.run(debug=True, port=5000)