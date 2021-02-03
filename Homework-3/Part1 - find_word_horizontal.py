def find_word_horizontal(crosswords, word):
    if (not crosswords) or (not word):
        return
    dic = {}
    c = 0
    for item in crosswords:
        dic[c] = ''.join(item)
        c+=1
    for i in range(len(list(dic.values()))):
        if word in list(dic.values())[i] or word == list(dic.values())[i]:
            bla = [i, crosswords[i].index(word[0])]
            return bla
            
    return