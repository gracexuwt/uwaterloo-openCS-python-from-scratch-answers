def compare(one, two):
    one.sort()
    two.sort()
    if(len(one) > len(two)):
        length = len(two)
    else:
        length = len(one)
    for i in range(length):
        if(one[i] > two[i]):
            return "Larger"
        elif(one[i] < two[i]):
            return "Smaller"
    if(len(one) > len(two)):
        return "Larger"
    elif(len(two) > len(one)):
        return "Smaller"
    return "Equal"