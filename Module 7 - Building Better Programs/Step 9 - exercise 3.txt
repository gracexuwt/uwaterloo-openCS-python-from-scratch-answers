def cap_first(entry):
    """Returns string formed from entry 
       with first letter captialized.

       Preconditions:
       entry: string

       Parameter:
       entry: string to be capitalized

       Returns: capitalized string
    """
    if len(entry) == 0:
        return entry
    else:
        return entry[0].upper() + entry[1:]

print(cap_first("capitalize"))