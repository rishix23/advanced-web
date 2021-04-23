from models import Job
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
            salary=record["salary"],
            start_date=datetime.strptime(record["startDate"], "%Y-%m-%d"),
            location=record["location"],
            company=record["company"],
            sector=record["sector"],
            description=record["description"],
            created=datetime.strptime(record["created"], "%Y-%m-%d"),
        )

        db.session.add(entity)

    db.session.commit()
