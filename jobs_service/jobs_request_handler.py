"""
JOBS REQUEST HANDLER

Responsible for handling requests directed at the root of this service
"""

from utils import parse_args_into_query_object
import json


def list_methods():
    return request_director.keys()


def handle(request):
    return request_director[request.method](request)


# Job.query.order_by(Job.id).all()
def get(request):
    with open("mock_jobs.json", "r") as reader:
        data = json.loads(reader.read())

    if not request.args:
        return str(data)

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


def post():
    # db.session.add(job)
    # db.session.commit
    return "Posted"


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
    # "POST": post,
    # "PUT": put,
    # "PATCH": patch,
    # "DELETE": delete,
}