def character_count(s):
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


print(character_count("hello"))