def pattern_sum(a, b):
    lis =[]
    for i in range(1,b+1):
        lis.append(i*str(a))
        
    return sum(list(map(int, lis)))
