def reverse_dictionary(input_dict):
    new_dict = {}
    new_keylist = list(new_dict.keys())
    inp_keylist = list(input_dict.keys())
    new_vallist = []

    for item in inp_keylist:
        inp_vallist = input_dict[item]

        for valitem in inp_vallist:
            new_vallist = []
            if new_keylist.count(valitem.lower()) == 0:
                new_keylist.append(valitem.lower())
                new_vallist.append(item.lower())
                new_dict[valitem.lower()] = new_vallist

            else:
                new_dict[valitem.lower()].append(item.lower())
                new_dict[valitem.lower()].sort()
    return (new_dict)