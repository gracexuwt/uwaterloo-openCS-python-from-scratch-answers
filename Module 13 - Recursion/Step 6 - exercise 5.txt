def contains(seq, item):
    if(len(seq) == 0):
        return False
    if(seq[0] == item):
        return True
    return contains(seq[1:], item)