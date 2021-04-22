"""
JOBS REQUEST HANDLER

Responsible for handling requests directed at the root of this service
"""


def list_methods():
    return request_director.keys()


def handle(request):
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
    "PATCH": patch,
    "DELETE": delete,
}