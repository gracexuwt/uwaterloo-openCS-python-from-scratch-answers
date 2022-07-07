def code(string, d):
    new = ""
    for char in string:
        if char in d:
            new = new + d[char]
        else:
            new = new + char
    return new