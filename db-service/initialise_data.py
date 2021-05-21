from models import Job, User, Application
from app import app, db
from datetime import datetime
import os
import json

with open(f"{os.pardir}{os.sep}mock_jobs.json", "r") as reader:
    data = json.loads(reader.read())

with (app.app_context()):
    for record in data:
        entity = Job(
            id=record["id"],
            title=record["title"],
            salary=record.get("salary", 0),
            start_date=datetime.strptime(record["startDate"], "%Y-%m-%d")
            if record.get("startDate")
            else datetime.utcnow(),
            location=record["location"],
            company=record["company"],
            sector=record.get("sector", "Init sector"),
            description=record.get("description", "Init description"),
            created=datetime.strptime(record["created"], "%Y-%m-%d")
            if record.get("created")
            else datetime.utcnow(),
        )

        db.session.add(entity)

    db.session.commit()

with open(f"{os.pardir}{os.sep}mock_users.json", "r") as reader:
    data = json.loads(reader.read())

with (app.app_context()):
    for record in data:
        entity = User(
            id=record["id"],
            first_name=record["firstName"],
            last_name=record["lastName"],
            age=record.get("age", 0),
            created=datetime.strptime(record["created"], "%Y-%m-%d")
            if record.get("created")
            else datetime.utcnow(),
        )

        db.session.add(entity)

    db.session.commit()


with open(f"{os.pardir}{os.sep}mock_applications.json", "r") as reader:
    data = json.loads(reader.read())

with (app.app_context()):
    for record in data:
        entity = Application(
            user_id=record["userId"],
            job_id=record["jobId"],
            status=record["status"],
            message=record.get("message", "Init message"),
            created=datetime.strptime(record["created"], "%Y-%m-%d")
            if record.get("created")
            else datetime.utcnow(),
        )

        db.session.add(entity)

    db.session.commit()
