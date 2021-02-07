def one_to_2D(inlist, r, c):
    cnt = 0
    rowlist = []
    outlist = []
    ilen = len(inlist)

    for i in range(ilen):
        if i == r*c:
            break

        rowlist.append(inlist[i])
        cnt = cnt + 1
        if cnt == c:
            outlist.append (rowlist)
            rowlist = []
            cnt = 0

    if (i < r*c) and (cnt < c) and (cnt > 0):
        for j in range(cnt,c):
            rowlist.append(None)
        outlist.append(rowlist)
        i = i + c - cnt
    print (i, i//c)

    if i < r*c:
        for j in range(i//c+1,r):
            rowlist = []
            for k in range(c):
                rowlist.append(None)
            outlist.append(rowlist)

    return (outlist)