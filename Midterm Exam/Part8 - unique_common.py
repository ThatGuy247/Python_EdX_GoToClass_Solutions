def unique_common(a, b):
    o = list(set(a).intersection(set(b)))
    o.sort()
    if not o:
        return
    return o
