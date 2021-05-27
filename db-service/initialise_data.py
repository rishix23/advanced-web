from models import Job, Employer
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
            employer_id=record["employerId"],
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

with open(f"{os.pardir}{os.sep}mock_employers.json", "r") as reader:
    data = json.loads(reader.read())

with (app.app_context()):
    for record in data:
        entity = Employer(
            id=record["id"],
            first_name=record["firstName"],
            last_name=record["lastName"],
            email=record.get("email", ""),
            password=record.get("password", ""),
            created=datetime.strptime(record["created"], "%Y-%m-%d")
            if record.get("created")
            else datetime.utcnow(),
        )

        db.session.add(entity)

    db.session.commit()
