def repeat_print(num):
    """Prints the input num times.
 
       Preconditions:
       num: positive integer 
    
       Parameter:
       num: the number of times and what is printed

       Side effect: prints num num times.
    """
    count = num
    while count > 0:
        print(num)
        count = count - 1

repeat_print(5)