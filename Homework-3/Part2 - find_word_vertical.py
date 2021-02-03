def find_word_vertical(crosswords, word):
    if (not crosswords) or (not word):
        return
    
    lis = []
    dic = {}
    for j in range(len(crosswords)):
        lis.append([item[j] for item in crosswords])
    
    for k in range(len(lis)):
        dic[k] = ''.join(lis[k])
            
    for i in range(len(list(dic.values()))):
        if word in list(dic.values())[i] or word == list(dic.values())[i]:
            bla = [lis[i].index(word[0]), i]
            return bla
            
    return