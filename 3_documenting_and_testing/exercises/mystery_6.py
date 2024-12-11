def mystery_6(a, b):
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
