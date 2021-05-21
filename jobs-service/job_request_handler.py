"""
JOB REQUEST HANDLER

Responsible for handling requests directed at a specific job (/<id>)
"""


def list_methods():
    return request_director.keys()


def handle(request, id):
    return request_director[request.method]()


def get():
    return "Getted"


def post():
    return "Posted"


def put():
    return "Putted"


def patch():
    return "Patched"


def delete():
    return "Deleted"


request_director = {
    "GET": get,
    "POST": post,
    "PUT": put,
    # "PATCH": patch,
    "DELETE": delete,
}