def trace_recursion(func):
    """
    Print a trace of calls, arguments and return values to the terminal.
    Errors are printed at the depth they occurred.
    """

    depth = -1
    indent = ". "
    log = False

    def wrapped(*args, **kwargs):
        nonlocal depth, indent, log

        if depth < 0:
            print("\n")
            log = True

        depth += 1

        print(f"{indent * depth}{func.__name__}({', '.join(map(str, args))})")

        try:
            result = func(*args, **kwargs)

        except RecursionError as rerror:
            raise rerror
        except Exception as error:
            if log:
                print(f"{'x ' * depth}{type(error).__name__}: {error}\n")

            depth = -1
            log = False
            
            return type(error).__name__
        else:
            print(f"{indent * depth}{result}")

            depth -= 1
            if depth < 0:
                print("\n")

            return result

    return wrapped
