"""
JOBS REQUEST HANDLER

Responsible for handling requests directed at the root of this service
"""

from utils import parse_args_into_query_object
from models import Job
from datetime import datetime
import json
import uuid
import requests


def list_methods():
    return request_director.keys()


def handle(request):
    return request_director[request.method](request)

def get(request):
    if not request.args:
        resp = requests.get("http://localhost:5001/jobs")
        return resp.json()

    query_obj = parse_args_into_query_object(
        request.args, {"id": None, "company": None}
    )

    # If we get an empty query object, it's a bad request

    jobs = []

    for job in data:
        for key, value in query_obj.items():
            if value:
                if job[key] == value:
                    jobs.append(job)

    return str(jobs)


def post(request):
    # db.session.add(job)
    # db.session.commit
    job = Job(
        id="1", title="Ttle", location="Ldn", company="TSLA", created=datetime.utcnow()
    )
    return str(job)


def put():
    return "Putted"


def patch():
    return "Patched"


# Job.query.get_or_404()
# db.session.delete()
# db.session.commit()
def delete():
    return "Deleted"


request_director = {
    "GET": get,
    "POST": post,
    # "PUT": put,
    # "PATCH": patch,
    # "DELETE": delete,
}