def is_multiple(number, factor):
    return number % factor == 0
    
def rel_prime(one, two):
    if(one > two):
        num = two
    else:
        num = one
    for factor in range(2,num):
        if(is_multiple(one,factor) and is_multiple(two,factor)):
            return False
    return True