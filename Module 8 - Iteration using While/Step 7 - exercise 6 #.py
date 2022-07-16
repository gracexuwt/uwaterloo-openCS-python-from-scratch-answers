def swap_case(string):
    new = ""
    length = 0
    while(length < len(string)):
        if(string[length].isalpha() and string[length].isupper()):
            new = new + string[length].lower()
        elif(string[length].isalpha() and string[length].islower()):
            new = new + string[length].upper()
        else:
            new = new + string[length]
        length = length + 1
    return new