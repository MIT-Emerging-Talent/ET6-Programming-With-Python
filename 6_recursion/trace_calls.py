def trace_calls(func):
    """
    Decorates functions to print a trace of calls, arguments and return values.
    """

    depth = -1
    indent = ". "

    def wrapped(*args, **kwargs):
        nonlocal depth, indent

        if depth < 0:
            print("\n")

        depth += 1

        # print current function call
        print(f"{indent * depth}{func.__name__}({', '.join(map(str, args))})")

        # call the function
        result = func(*args, **kwargs)

        # print current return value
        print(f"{indent * depth}{result}")

        depth -= 1
        if depth < 0:
            print("\n")

        return result

    return wrapped
