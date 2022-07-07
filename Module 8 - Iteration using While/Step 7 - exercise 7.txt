def multisplit(total, split):
    num = 0
    while(total > 1):
        total = (int)(total / split)
        num = num + 1
    return num