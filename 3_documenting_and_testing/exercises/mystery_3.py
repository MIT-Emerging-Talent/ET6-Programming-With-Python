def mystery_3(a, b=None):
    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
