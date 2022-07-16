def add_up():
    num = 0
    user = input("Input a number (Type Stop to stop)")
    while(user != "Stop"):
        num = num + int(user)
        user = input("Input a number (Type Stop to stop)")
    return num