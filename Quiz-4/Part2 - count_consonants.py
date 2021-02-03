def count_consonants(string): 
    
    def isConsonant(ch): 
      
        # To handle lower case 
        ch = ch.upper() 
      
        return not (ch == 'A' or ch == 'E' or 
                    ch == 'I' or ch == 'O' or 
                    ch == 'U') and ord(ch) >= 65 and ord(ch) <= 90
      
    count = 0
      
    for i in range(len(string)): 
  
        # To check is character is Consonant 
        if (isConsonant(string[i])): 
            count += 1
              
    return count 