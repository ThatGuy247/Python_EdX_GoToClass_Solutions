def n_letter_dictionary(my_string):
    dic = {}
    main_dic = {}
    my_string = my_string.split()
    my_string = list(map(str.casefold, my_string))                  
    for item in my_string:
        dic[item] = dic.get(item, len(item))
    for m,n in sorted(dic.items()):
        main_dic[(n)] = sorted(main_dic.get((n), []) + [m])
    return main_dic

