# Write a function upper_lower that consumes a string plain and produces a string with the same characters 
# as in plain except that all letters in the first half of the string are in upper case and all the rest of the letters are in lower case. 
# Non-letters should be the same.
# If the length of the string is odd, the "first half" should contain the middle character

import math
def upper_lower(plain):
    mid = (int)(math.ceil(len(plain)/2))
    return plain[:mid].upper() + plain[mid:].lower()