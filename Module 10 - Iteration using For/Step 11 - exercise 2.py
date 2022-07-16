def password(string):
    has_upper = False
    has_lower = False
    has_digit = False
    if(len(string) < 8):
        return False
    for char in string:
        if(char.isupper()):
            has_upper = True
        if(char.islower()):
            has_lower = True
        if(char.isdigit()):
            has_digit = True
        if(has_upper and has_lower and has_digit):
            return True
    return False