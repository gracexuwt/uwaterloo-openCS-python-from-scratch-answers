def yarn_size(stitches):
    """Determines yarn size given 4 inches of stitches.

       Preconditions:
       stitches: int > 0; 6 <= value <= 32
     
       Parameter:
       stitches: average number of stitches in 4 inches

       Returns: yarn size
    """
    BULKY_MAX = 0
    if 6 <= stitches <= 11:
        return "Super bulky"
    elif 12 <= stitches <= 15:
        return "Bulky"
    elif 16 <= stitches <= 20:
        return "Medium"
    elif 21 <= stitches <= 22:
        return "Light"
    elif 23 <= stitches <= 24:
        return "Light or Fine"
    elif 25 <= stitches <= 26:
        return "Fine"
    else:
        return "Super fine"