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
        job.title = request.json.get("title", "")
        job.salary = request.json.get("salary", 0)
        # Assuming a date arrives in the format YYYY-MM-DD
        request_date = request.json.get("startDate", str(date.today()))
        job.start_date = date(
            int(request_date[0:4]), int(request_date[5:7]), int(request_date[8:10])
        )
        job.location = request.json.get("location", "")
        job.company = request.json.get("company", "")
        job.sector = request.json.get("sector", "")
        job.description = request.json.get("description", "")
        db.session.add(job)
        db.session.commit()

        return job_schema.jsonify(job), 201


@app.route("/jobs/<id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def handle_job(id):
    if request.method == "GET":
        job = db.session.query(Job).get({"id": id})
        return job_schema.jsonify(job)

    if request.method == "PUT":
        job = db.session.query(Job).get({"id": id})
        if not job:
            return "Job not found", 400

        job = Job()
        job.id = id
        job.title = request.json.get("title", "")
        job.salary = request.json.get("salary", 0)
        # Assuming a date arrives in the format YYYY-MM-DD
        request_date = request.json.get("startDate", str(date.today()))
        job.start_date = date(
            int(request_date[0:4]), int(request_date[5:7]), int(request_date[8:10])
        )
        job.location = request.json.get("location", "")
        job.company = request.json.get("company", "")
        job.sector = request.json.get("sector", "")
        job.description = request.json.get("description", "")
        db.session.add(job)
        db.session.commit()

        return job_schema.jsonify(job)

    # MAYBE DON'T SUPPORT PATCH
    # if request.method == "PATCH":
    #     job = db.session.query(Job).get({"id": id})
    #     if not job:
    #         return "Job not found", 400

    #     new_job = Job()
    #     new_job.id = id
    #     new_job.title = job.title
    #     new_job.salary = job.salary
    #     new_job.start_date = job.start_date
    #     new_job.location = job.location
    #     new_job.company = job.company
    #     new_job.sector = job.sector
    #     new_job.description = job.description
    #     for key, value in request.json.items():
    #         if key == "start_date":
    #             new_job = date(int(value[0:4]), int(value[5:7]), int(value[8:10]))
    #         else:
    #             new_job[key] = value

    #     db.session.add(new_job)
    #     db.session.commit()

    #     return job_schema.jsonify(new_job)

    if request.method == "DELETE":
        job = db.session.query(Job).get({"id": id})
        if not job:
            return "Job not found", 400

        db.session.delete(job)
        db.session.commit()

        return f"Deleted job with id: {job.id}"


@app.route("/users", methods=["GET", "POST"])
def handle_users():
    if request.method == "GET":
        users = db.session.query(User).all()
        return users_schema.jsonify(users)

    if request.method == "POST":
        user = User()
        user.id = str(uuid.uuid4())
        user.first_name = request.json.get("firstName", "")
        user.last_name = request.json.get("lastName", "")
        user.age = request.json.get("age", 0)
        db.session.add(user)
        db.session.commit()

        return user_schema.jsonify(user), 201


@app.route("/users/<id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def handle_user(id):
    if request.method == "GET":
        user = db.session.query(User).get({"id": id})
        return user_schema.jsonify(user)

    if request.method == "PUT":
        user = db.session.query(User).get({"id": id})
        if not user:
            return "user not found", 400

        user = User()
        user.id = id
        user.first_name = request.json.get("firstName", "")
        user.last_name = request.json.get("lastName", "")
        user.age = request.json.get("age", 0)
        db.session.add(user)
        db.session.commit()

        return user_schema.jsonify(user)

    # MAYBE DON'T SUPPORT PATCH
    # if request.method == "PATCH":
    #     user = db.session.query(user).get({"id": id})
    #     if not user:
    #         return "user not found", 400

    #     new_user = user()
    #     new_user.id = id
    #     new_user.title = user.title
    #     new_user.salary = user.salary
    #     new_user.start_date = user.start_date
    #     new_user.location = user.location
    #     new_user.company = user.company
    #     new_user.sector = user.sector
    #     new_user.description = user.description
    #     for key, value in request.json.items():
    #         if key == "start_date":
    #             new_user = date(int(value[0:4]), int(value[5:7]), int(value[8:10]))
    #         else:
    #             new_user[key] = value

    #     db.session.add(new_user)
    #     db.session.commit()

    #     return user_schema.jsonify(new_user)

    if request.method == "DELETE":
        user = db.session.query(User).get({"id": id})
        if not user:
            return "User not found", 400

        db.session.delete(user)
        db.session.commit()

        return f"Deleted user with id: {user.id}"


@app.route("/applications", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def handle_applications():
    applications = db.session.query(Application).all()
    return applications_schema.jsonify(applications)


@app.route("/employers", methods=["GET", "POST"])
def handle_employers():
    if request.method == "GET":
        employers = db.session.query(Employer).all()
        return employers_schema.jsonify(employers)

    if request.method == "POST":
        employer = Employer()
        employer.id = str(uuid.uuid4())
        employer.name = request.json.get("name", "")
        db.session.add(employer)
        db.session.commit()

        return employer_schema.jsonify(employer), 201


@app.route("/employers/<id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def handle_employer(id):
    if request.method == "GET":
        employer = db.session.query(Employer).get({"id": id})
        return employer_schema.jsonify(employer)

    if request.method == "PUT":
        employer = db.session.query(Employer).get({"id": id})
        if not employer:
            return "Employer not found", 400

        employer = Employer()
        employer.id = id
        employer.name = request.json.get("name", "")
        db.session.add(employer)
        db.session.commit()

        return employer_schema.jsonify(employer)

    # MAYBE DON'T SUPPORT PATCH
    # if request.method == "PATCH":
    #     employer = db.session.query(employer).get({"id": id})
    #     if not employer:
    #         return "employer not found", 400

    #     new_employer = employer()
    #     new_employer.id = id
    #     new_employer.title = employer.title
    #     new_employer.salary = employer.salary
    #     new_employer.start_date = employer.start_date
    #     new_employer.location = employer.location
    #     new_employer.company = employer.company
    #     new_employer.sector = employer.sector
    #     new_employer.description = employer.description
    #     for key, value in request.json.items():
    #         if key == "start_date":
    #             new_employer = date(int(value[0:4]), int(value[5:7]), int(value[8:10]))
    #         else:
    #             new_employer[key] = value

    #     db.session.add(new_employer)
    #     db.session.commit()

    #     return employer_schema.jsonify(new_employer)

    if request.method == "DELETE":
        employer = db.session.query(Employer).get({"id": id})
        if not employer:
            return "employer not found", 400

        db.session.delete(employer)
        db.session.commit()

        return f"Deleted employer with id: {employer.id}"


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