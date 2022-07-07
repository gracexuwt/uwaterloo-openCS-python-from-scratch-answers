def total_bill(cost, age, tax):
    if(age >= 65):
        return cost * (1 - .1) * (1 + tax)
    return cost * (1 + tax)