def no_nums(string):
    new = ""
    for char in string:
        if(not char.isdigit()):
            new = new + char
    return new