BULLETS = 351
FINE = 321
BRILLIANT = 291
SUPERIOR = 261
LARGE = 231
EXTRA_LARGE = 201
JUMBO = 181
EXTRA_JUMBO = 161
GIANT = 141
COLOSSAL = 121
SUPER_COLOSSAL = 111
MAMMOTH = 101
SUPER_MAMMOTH = 91

def olive_sizes(number):
    """Returns a string for the type of olive
       given the number per kilogram.

       Preconditions:
       number: integer in range from 91 to 351, inclusive

       Parameter:
       number: number of olives in one kilogram

       Return: a string giving type of olive
    """

    if number <= BULLETS:
        return "Bullets"
    elif number >= FINE:
        return "Fine"
    elif number >= BRILLIANT:
        return "Brilliant"
    elif number >= SUPERIOR:
        return "Superior"
    elif number >= LARGE:
        return "Large"
    elif number >= EXTRA_LARGE:
        return "Extra Large"
    elif number >= JUMBO:
        return "Jumbo"
    elif number >= EXTRA_JUMBO:
        return "Extra Jumbo"
    elif number >= GIANT:
        return "Giant"
    elif number >= COLOSSAL:
        return "Colossal"
    elif number >= SUPER_COLOSSAL:
        return "Super Colossal"
    elif number >= MAMMOTH:
        return "Mammoth"
    else:
        return "Super Mammoth"

print(olive_sizes(142))