def four_i(num):
    return type(num) == type("") and len(num) >= 4 and num[3] == "i"