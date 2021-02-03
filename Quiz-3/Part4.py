def lis(lis1):
    c = 0
    for i in lis1:
        if i % 2 != 0:
            c += i
    return c
