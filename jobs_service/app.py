from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import jobs_request_handler
import job_request_handler

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../app.db"
db = SQLAlchemy(app)


class Job(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Integer, nullable=True)
    start_date = db.Column(db.DateTime, nullable=True)
    location = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(50), nullable=False)
    sector = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Job %r>" % self.id


@app.route("/", methods=jobs_request_handler.list_methods())
def jobs():
    return jobs_request_handler.handle(request)


@app.route("/<id>", methods=job_request_handler.list_methods())
def job(id):
    return job_request_handler.handle(request, id)


if __name__ == "__main__":
    app.run(debug=True)