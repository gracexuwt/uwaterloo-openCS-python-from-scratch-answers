def multisplit(total, split):
    if(total <= 1):
        return 0
    return multisplit(total / split, split) + 1