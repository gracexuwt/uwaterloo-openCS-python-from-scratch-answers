def code_ending(end):
    if(end[-1].isalpha() and end[-2].isalpha() and end[-3].isdigit()):
        return True
    return False

def code_eight(string):
    if(string[:2].isalpha() and string[2].isdigit() and not string[3].isspace() and string[4].isspace()):
        return True
    return False

def uk_code(entry):
    """Determines if a string can be a postal code.

       Preconditions:
       entry: string of letters, digits, spaces only

       Parameters:
       entry: possible postal code

       Returns "Code" if of one of the following forms:
       "A9 9AA", "A9A 9AA", "A99 9AA", "AA9 9AA",
       "AA9A 9AA", "AA99 9AA" where 9 is any digit and
       A is any letter,
       and "Not code" otherwise
    """

    ## Return "Not code" if the length is not between 6 and 8
    if len(entry)<6 or len(entry) > 8:
        return "Not code"

    ## Return "Not code" if it does not start with a letter 
    ## or end of the form  ' 9AA'
    if(not entry[0].isalpha() or not code_ending(entry)):
        return "Not code"

    ## Return "Code" for valid codes of length 6
    if(len(entry) == 6 and entry[0].isalpha() and entry[1].isdigit() and entry[2].isspace()):
        return "Code"

    ## Return "Code" for valid codes of length 7
    if(len(entry) == 7 and entry[3].isspace() and not entry[1:3].isspace()):
        return "Code"

    ## Return "Code" for valid codes of length 8
    if(len(entry) == 8 and code_eight(entry)):
        return "Code"

    ## Return "Not code" for all other inputs
    return "Not code"