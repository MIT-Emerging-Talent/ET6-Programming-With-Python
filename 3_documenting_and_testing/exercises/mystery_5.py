def mystery_5(a, b):
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
