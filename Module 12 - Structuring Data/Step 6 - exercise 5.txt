def bound_chars(string, bound):
    d = {}
    for char in string:
        if(char not in d):
            d[char] = 1
        else:
            d[char] = d[char] + 1
    if(len(d) <= bound):
        return True
    return False