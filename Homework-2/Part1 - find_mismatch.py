def find_mismatch(a, b):
    if len(a) != len(b):
        return 2
    a, b = a.casefold(), b.casefold()
    if a == b:
        return 0
    error = False
    for a, b in zip(a, b):
        if a != b:
            if error:
                return 2
            error = True
    return 1
