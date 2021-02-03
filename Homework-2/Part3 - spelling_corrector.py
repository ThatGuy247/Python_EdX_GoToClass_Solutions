def spelling_corrector(s1, s2) -> str:
    
    def replace_1(bad:str, good:str) -> bool:
        """Return True if bad can be converted to good by replacing 1 letter.
        """
        if len(bad) != len(good):
            return False
    
        changes = 0
        for i,ch in enumerate(bad):
            if ch != good[i]:
                return bad[i+1:] == good[i+1:]
    
        return False

    def insert_1(bad:str, good:str) -> bool:
        """Return True if bad can be converted to good by inserting 1 letter.
        """
        if len(bad) != len(good) - 1:
            return False
    
        for i,ch in enumerate(bad):
            if ch != good[i]:
                return bad[i:] == good[i+1:]

        # At this point, all of bad matches first part of good. So it's an
        # append of the last character.
        return True

    def delete_1(bad:str, good:str) -> bool:
        """Return True if bad can be converted to good by deleting 1 letter.
        """
        if len(bad) != len(good) + 1:
            return False
        return insert_1(good, bad)
    
    
    def correction(word:str, correct_spells:list) -> str:
        if len(word) < 3:
            return word
        if word in correct_spells:
            return word
        for good in correct_spells:
            if replace_1(word, good):
                return good
            if insert_1(word, good):
                return good
            if delete_1(word, good):
                return good
    
        return word
        
    words = s1.strip().lower().split()
    correct_lower = [cs.lower() for cs in s2]
    result = [correction(w, correct_lower) for w in words]
    return ' '.join(result)