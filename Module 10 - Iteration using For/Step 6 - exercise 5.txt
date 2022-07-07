def all_upper(entry):
    """Determines if a string is all upper-case letters

       Preconditions:
       entry: string

       Parameter:
       entry: candidate string to check

       Returns: True if so, False otherwise
    """
    for char in entry:
        if(not char.isalpha() or char.islower()):
            return False
    return True

def all_digit(entry):
    """Determines if a string is all digits

       Preconditions:
       entry: string

       Parameter:
       entry: candidate string to check

       Returns: True if so, False otherwise
    """
    for char in entry:
        if(not char.isdigit()):
            return False
    return True

def postal_code(entry):
    """Determines if a string is A9A 9A9 in form.

       Preconditions:
       entry: string

       Parameter:
       entry: candidate string to check

       Returns: True if so, False otherwise
    """

    ## Check length
    if(len(entry) != 7):
        return False
    ## Form a string caps of the "A" entries
    caps = entry[0] + entry[2] + entry[5]
    ## Form a string nums of the "9" entries
    nums = entry[1] + entry[4] + entry[6]
    ## Check for the middle blank
    if(not entry[3].isspace()):
        return False
    ## Check that caps is all upper-case
    if(not all_upper(caps)):
        return False
    ## Check that nums is all digits
    if(not all_digit(nums)):
        return False
    return True