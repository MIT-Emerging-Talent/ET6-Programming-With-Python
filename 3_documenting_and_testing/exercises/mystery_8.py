def mystery_8(a, b):
    c = []
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]
    return c
