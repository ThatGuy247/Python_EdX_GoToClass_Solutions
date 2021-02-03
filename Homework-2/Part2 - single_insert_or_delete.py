def single_insert_or_delete(s1,s2)
    s1,s2 = s1.lower(), s2.lower()
    count = 0
    if s1 == s2
        return 0
    elif len(s1) == len(s2)
        return 2
    elif len(s1) - len(s2) == -1
        if s1 == s2[-1]
            return 1
        else
            for i in range(len(s2))
                if s1 == s2[i] + s2[i+1]
                    return 1
            else
               return 2
    elif len(s1) - len(s2) == 1
        if s1[-1] == s2 or s1[1] == s2
            return 1
        else
            for i in range(len(s1))
                if s2 == s1[i] + s1[i+1]
                    return 1
            else
                 return 2  

    else
        return 2