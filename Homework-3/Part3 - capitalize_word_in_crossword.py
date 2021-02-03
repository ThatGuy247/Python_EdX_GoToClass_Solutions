def find_word_horizontal(crossword,word):
    if not crossword or not word:
        return None
    for index,row in enumerate(crossword):
        temp_str=''.join(row)
        if temp_str.find(word)>=0:
            return [index,temp_str.find(word)]
    return None
def find_word_vertical(crossword,word):
    if not crossword or not word:
        return None    
    number_of_columns=len(crossword[0])
    for col_index in range (number_of_columns):
        temp_str=''
        for row_index in range(len(crossword)):
            temp_str=temp_str+crossword[row_index][col_index]
        if temp_str.find(word)>=0:
            return [temp_str.find(word),col_index]
    return None
def capitalize_word_in_crossword(crossword,word):
    if not crossword or not word:
        return None    
    found_position= _find_word_horizontal(crossword,word)
    if found_position:
        for k in range(len(word)):
            crossword[found_position[0]][found_position[1]+k]=crossword[found_position[0]][found_position[1]+k].upper()
        return crossword 
    found_position= _find_word_vertical(crossword,word)
    if found_position:
        for k in range(len(word)):
            crossword[found_position[0]+k][found_position[1]]=crossword[found_position[0]+k][found_position[1]].upper()
    return crossword