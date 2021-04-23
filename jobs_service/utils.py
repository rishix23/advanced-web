def parse_args_into_query_object(args, obj):
    output = {}
    arg_keys = [key for key in args.keys()]
    obj_keys = [key for key in obj.keys()]
    bad_keys = [key for key in arg_keys if key not in obj_keys]

    if bad_keys:
        return output

    for key in arg_keys:
        output[key] = args.get(key)

    return output