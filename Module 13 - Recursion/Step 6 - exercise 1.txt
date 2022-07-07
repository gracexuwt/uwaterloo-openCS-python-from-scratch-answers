def has_digit(string):
    if(len(string) == 0):
        return False
    if(string[0].isdigit()):
        return True
    else:
        return has_digit(string[1:])