def multiplication_table(inp):
    outlist = []

    for i in range(1,inp+1):
        rowlist = []
        for j in range(1, inp+1):
            rowlist.append(i*j)
        outlist.append(rowlist)
    return (outlist)