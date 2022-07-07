def multisplit(total, split):
    num = 0
    for counter in range(total):
        total = total / split
        num = num + 1
        if(total <= 1):
            break
    return num