def construct_dictionary_from_lists(names, ages, scores)
    dic={}
    for i in range(len(names))
        dic[names[i]] = [ages[i], scores[i], 'pass' if scores[i]= 60 else 'fail']
    return dic
        
