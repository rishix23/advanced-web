from datetime import date
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models import metadata, Job, Application, Employer

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
        job.id = request.json.get("id", "")
        job.employer_id = request.json.get("employerId", "")
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
        job.employer_id = request.json.get("employerId", "")
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


@app.route("/applications", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def handle_applications():
    if request.method == "GET":
        if not request.args.get("employrId") and not request.args.get("jobId"):
            applications = db.session.query(Application).all()
            return applications_schema.jsonify(applications)

        if request.args.get("employerId") and request.args.get("jobId"):
            applications = db.session.query(Application).filter(
                Application.employer_id == request.args.get("employerId"),
                Application.job_id == request.args.get("jobId"),
            )
            return applications_schema.jsonify(applications)

        if request.args.get("employerId"):
            applications = db.session.query(Application).filter(
                Application.employer_id == request.args.get("employerId")
            )
            return applications_schema.jsonify(applications)

        applications = db.session.query(Application).filter(
            Application.job_id == request.args.get("jobId")
        )
        return applications_schema.jsonify(applications)

    if request.method == "POST":
        application = Application()
        application.id = request.form.get("id")
        application.job_id = request.form.get("jobId")
        application.full_name = request.form.get("fullname")
        application.phone = request.form.get("phone")
        application.email = request.form.get("email")
        application.resume = request.files.get("resume").read()
        db.session.add(application)
        db.session.commit()

        return application_schema.jsonify(application), 201

    if request.method == "PATCH":
        existing_application = db.session.query(Application).get(
            {
                "employer_id": request.args.get("employerId"),
                "job_id": request.args.get("jobId"),
            }
        )

        if not existing_application:
            return "Application does not exist", 400

        if request.json.get("message", None):
            existing_application.message = request.json["message"]

        if request.json.get("status", None):
            existing_application.message = request.json["status"]

        db.session.add(existing_application)
        db.session.commit()

        return "Application updated"


@app.route("/employers", methods=["GET", "POST"])
def handle_employers():
    if request.method == "GET":
        if not request.args:
            employers = db.session.query(Employer).all()
            return employers_schema.jsonify(employers)

        employers = db.session.query(Employer).filter(
            Employer.email == request.args.get("email")
        )

        return employers_schema.jsonify(employers)

    if request.method == "POST":
        employer = Employer()
        employer.id = request.json.get("id", "")
        employer.first_name = request.json.get("firstName", "")
        employer.last_name = request.json.get("lastName", "")
        employer.email = request.json.get("email", "")
        employer.password = request.json.get("password", "")
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
        employer.first_name = request.json.get("firstName", "")
        employer.last_name = request.json.get("lastName", "")
        employer.email = request.json.get("email", "")
        employer.password = request.json.get("password", "")
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
            "employer_id",
            "title",
            "salary",
            "start_date",
            "location",
            "company",
            "sector",
            "description",
            "created",
        )


class ApplicationSchema(ma.Schema):
    class Meta:
        fields = ("id", "job_id", "full_name", "phone", "email", "created")


class EmployerSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email", "password")


# Initialise Schemas
job_schema = JobSchema()
jobs_schema = JobSchema(many=True)

application_schema = ApplicationSchema()
applications_schema = ApplicationSchema(many=True)

employer_schema = EmployerSchema()
employers_schema = EmployerSchema(many=True)

# Functions that allow the frontend to recieve data from api

if __name__ == "__main__":
    app.run(debug=True, port=5001)