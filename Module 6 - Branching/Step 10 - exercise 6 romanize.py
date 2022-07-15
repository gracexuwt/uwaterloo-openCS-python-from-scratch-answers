def romanize(num):
    string = ""
    if(4 < num < 9):
        string = "V"
    if(num == 1 or num == 6):
        string = string + "I"
    elif(num == 2 or num == 7):
        string = string + "II"
    elif(num == 3  or num == 8):
        string = string + "III"
    elif(num == 4):
        string = "IV"
    elif(num == 9):
        string = "IX"
    elif(num == 10):
        string = "X"
    return string