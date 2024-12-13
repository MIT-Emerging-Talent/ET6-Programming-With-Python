def mystery_4(a):
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
