from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from models import metadata, Job, User, Application, Employer

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(metadata=metadata)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/jobs", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def handle_jobs():
    jobs = db.session.query(Job).all()
    return str(jobs)


@app.route("/users", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def handle_users():
    users = db.session.query(User).all()
    return str(users)


@app.route("/applications", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def handle_applications():
    applications = db.session.query(Application).all()
    return str(applications)


@app.route("/employers", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def handle_employers():
    employers = db.session.query(Employer).all()
    return str(employers)


if __name__ == "__main__":
    app.run(debug=True, port=5001)