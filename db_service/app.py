from datetime import date
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models import metadata, Job, User, Application, Employer
import uuid

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(metadata=metadata)
db.init_app(app)
ma = Marshmallow(app)

with app.app_context():
    db.create_all()


@app.route("/jobs", methods=["GET", "POST"])
def handle_jobs():
    if request.method == "GET":
        jobs = db.session.query(Job).all()
        return jobs_schema.jsonify(jobs)

    if request.method == "POST":
        job = Job()
        job.id = str(uuid.uuid4())
        job.title = "Title"
        job.salary = 300
        # job.start_date = datetime.datetime.strptime("2021-09-01", "")
        job.start_date = date(2021, 10, 1)
        job.location = "Guildford"
        job.company = "New Company"
        job.sector = "Technology"
        job.description = (
            "Come and work for one of Guildford's fastest growing startups!"
        )
        db.session.add(job)
        db.session.commit()


@app.route("/jobs/<id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def handle_job(id):
    job = db.session.query(Job).get({"id": id})
    return job_schema.jsonify(job)


@app.route("/users", methods=["GET", "POST"])
def handle_users():
    users = db.session.query(User).all()
    return users_schema.jsonify(users)


@app.route("/users/<id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def handle_user(id):
    user = db.session.query(User).get({"id": id})
    return user_schema.jsonify(user)


@app.route("/applications", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def handle_applications():
    applications = db.session.query(Application).all()
    return applications_schema.jsonify(applications)


@app.route("/employers", methods=["GET", "POST"])
def handle_employers():
    employers = db.session.query(Employer).all()
    return employers_schema.jsonify(employers)


@app.route("/employers/<id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def handle_employer(id):
    employer = db.session.query(Employer).get({"id": id})
    return employer_schema.jsonify(employer)


# Define Schemas
class JobSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "title",
            "salary",
            "start_date",
            "location",
            "company",
            "sector",
            "description",
            "created",
        )


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "age", "created")


class ApplicationSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "job_id", "status", "message", "created")


class EmployerSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")


# Initialise Schemas
job_schema = JobSchema()
jobs_schema = JobSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

application_schema = ApplicationSchema()
applications_schema = ApplicationSchema(many=True)

employer_schema = EmployerSchema()
employers_schema = EmployerSchema(many=True)


if __name__ == "__main__":
    app.run(debug=True, port=5001)