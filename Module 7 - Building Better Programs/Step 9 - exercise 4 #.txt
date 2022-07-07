import math
def exchange(entry):
    """Returns string with middle and last
       character exchanged.

       Preconditions:
       entry: string of odd length > 0

       Parameter:
       entry: string as basis for new string

       Returns: string like entry but with
                middle and last positions exchanged
    """
    if(len(entry) == 1):
       return entry
    mid = math.floor(len(entry) / 2)
    last = 2 * mid
    first_part = entry[:mid]
    mid_char = entry[mid]
    second_part = entry[(mid+1):last]
    last_char = entry[last]
    return first_part + last_char + second_part + mid_char

print(exchange("caterpillar"))
print(exchange("cat"))