def parse_args_into_query_object(args, obj):
    output = {}
    arg_keys = [key for key in args.keys()]
    obj_keys = [key for key in obj.keys()]
    bad_keys = [key for key in arg_keys if key not in obj_keys]

    if bad_keys:
        return output

    common_keys = list(set(arg_keys) | set(obj_keys))

    for key in common_keys:
        output[key] = args.get(key)

    return output