def full(x):
    lis = []
    for i in range(1,x):
        if x % i == 0:
            lis.append(i)
    if sum(lis) == x:
        return True
    else:
        return False
