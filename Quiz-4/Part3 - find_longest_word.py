def find_longest_word(input_string):  
    longest_word =  max(input_string.split(' '), key=len)
    a = len(longest_word)
    l = []
    for item in input_string.split(' '):
        if len(item) == a:
            l.append(item)
    return str(l[-1])