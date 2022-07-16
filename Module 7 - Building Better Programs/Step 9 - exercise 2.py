import math
def select_mod(entry, num):
    """Returns the character in entry 
       at position num modulo string length.

       Preconditions:
       entry: string of length > 0
       num: positive integer

       Parameters:
       entry: string containing chosen character
       num: position in the string 

       Return: a single character
    """
    select = (int)(math.fmod(num, len(entry)))
    return entry[select]

print(select_mod("caterpillar", 13))