DOZEN = 12         # number of items in a dozen
BAKERS_DOZEN = 13  # number of items in a baker's dozen

def bakers(items, dozen, single):
    """Determines cost of items with baker's dozen discount.

       Preconditions:
       items: int > 0

       Parameters:
       items: number of items, dozen cost, single cost
   
       Returns: total cost with discount of 13 for the cost of a dozen
    """   

    total_cost = (items // DOZEN) * dozen
    extras = items % DOZEN
    if extras == DOZEN:
        total_cost = total_cost + dozen
    elif items != 13:
        total_cost = total_cost + extras * single
    return total_cost