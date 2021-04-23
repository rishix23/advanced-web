from flask import Flask
from flask_sqlalchemy import SQLAlchemy, request
from models import metadata, Job, User, Application, Employer

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../app.db"
db = SQLAlchemy(metadata=metadata)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/job", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def index():
    return "Get"


if __name__ == "__main__":
    app.run(debug=True, port=5001)