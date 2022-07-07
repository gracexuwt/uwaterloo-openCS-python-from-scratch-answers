def no_nums(string):
    new = ""
    length = 0
    while(length < len(string)):
        if(not string[length].isdigit()):
            new = new + string[length]
        length = length + 1
    return new