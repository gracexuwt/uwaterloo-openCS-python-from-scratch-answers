def equals(one, two):
    if(len(one) != len(two)):
        return False
    for i in range (len(one)):
        if(type(one[i]) != type(two[i]) or one[i] != two[i]):
            return False
    return True