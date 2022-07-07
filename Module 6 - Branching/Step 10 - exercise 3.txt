def integer_type(num):
    if(type(num) != type(0)):
        return "Not an integer"
    elif(num % 2 == 0):
        return "Even integer"
    else:
        return "Odd integer"