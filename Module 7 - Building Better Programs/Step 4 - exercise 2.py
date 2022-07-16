DOZEN = 12         # number of items in a dozen
BAKERS_DOZEN = 13  # number of items in a baker's dozen
DOZEN_COST = 10    # cost of a dozen
SINGLE_COST = 1    # cost of a single item

def bakers(items):
    """Determines cost of items with baker's dozen discount.

       Preconditions:
       items: int > 0

       Parameters:
       items: number of items 
   
       Returns: total cost with discount of 13 for the cost of a dozen
    """   
    ## Determine numbers of groups of 13 and extras
    total_cost = (items // BAKERS_DOZEN) * DOZEN_COST
    extras = items % BAKERS_DOZEN
    ## If there are twelve extras, use dozen_cost
    if extras == DOZEN:
        total_cost += DOZEN_COST
    ## If there are fewer than twelve extras, use single_cost
    else:
        total_cost = total_cost + extras * SINGLE_COST
    return total_cost