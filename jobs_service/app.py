from flask import Flask, request
from datetime import datetime
import jobs_request_handler
import job_request_handler

app = Flask(__name__)


@app.route("/", methods=jobs_request_handler.list_methods())
def jobs():
    return jobs_request_handler.handle(request)


@app.route("/<id>", methods=job_request_handler.list_methods())
def job(id):
    return job_request_handler.handle(request, id)


if __name__ == "__main__":
    app.run(debug=True, port=5000)