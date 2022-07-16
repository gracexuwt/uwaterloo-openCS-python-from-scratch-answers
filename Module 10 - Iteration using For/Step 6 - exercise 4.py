def swap_case(string):
    new = "";
    for char in string:
        if(char.isupper()):
            new += (char.lower());
        elif(char.islower()):
            new += (char.upper());
        else:
            new += char;
    return new;