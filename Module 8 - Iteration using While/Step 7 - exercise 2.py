def increase(num):
    """Determines the sum of num down to 1.

       Preconditions:
       num: int > 0

       Parameter:
       num: the starting number

       Returns: sum of num down to 1
    """
    total = 0
    while num > 0:
        total = total + num
        num = num - 1
    return total

print(increase(5))