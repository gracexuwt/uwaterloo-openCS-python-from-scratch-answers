def total_bill(cost, age, tax):
    if(cost < 100 and age >= 65):
        return cost * .9 * (1 + tax) + 5
    elif(age >= 65):
        return cost * .9 * (1 + tax)
    elif(cost < 100):
        return cost * (1 + tax) + 5
    else:
        return cost * (1 + tax)