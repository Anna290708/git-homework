def unique_characters(s):
    seen = []
    for i in s:
        if i in seen:
            return False
        seen.append(i)
    return True



print(unique_characters("abctrs")) 
