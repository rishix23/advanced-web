from flask.wrappers import Response
import json


def parse_args_into_query_object(args, obj):
    output = {}
    arg_keys = [key for key in args.keys()]
    obj_keys = [key for key in obj.__dict__.keys()]
    bad_keys = [key for key in arg_keys if key not in obj_keys]

    if bad_keys:
        return output

    for key in arg_keys:
        output[key] = args.get(key)

    return output


def wrap_response(status, data):
    return Response(
        content_type="application/json", status=status, response=json.dumps(data)
    )
