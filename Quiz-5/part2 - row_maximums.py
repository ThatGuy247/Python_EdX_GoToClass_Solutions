def row_maximums(list2d):
    rowlen = len(list2d)
    outdict = {}
    keylist = []
    vallist = []

    for i in range(rowlen):
        collen = len(list2d[i])
        maxval = 0
        for j in range(collen):
            if list2d[i][j] > maxval:
                maxval = list2d[i][j]
        vallist.append(maxval)
        keylist.append('row '+str(i)+' max')

    outdict = dict(zip(keylist, vallist))
    return (outdict)