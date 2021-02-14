def MY_2D_LIST(n):
    my_list = []
    for i in range (1,n+1):
        if i == 1:
            sublist = [1]
            my_list.append (sublist)
        elif i == 2:
            sublist = [1, 1]
            my_list.append (sublist)
        else:
            sublist = [1]
            for j in range(1,i-1):
                tempval = my_list[i-2][j] + my_list[i-2][j-1]
                sublist.append(tempval)
            sublist.append(1)
            my_list.append(sublist)
    return (my_list)
