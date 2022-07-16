def my_power(base, exponent):
    num = 1
    while(exponent > 0):
        num = num * base
        exponent = exponent -1
    return num