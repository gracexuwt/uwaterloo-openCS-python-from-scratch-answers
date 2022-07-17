def is_sorted(seq):
    if(len(seq) == 0 or len(seq) == 1):
        return True
    if(seq[0] > seq[1]):
        return False
    return is_sorted(seq[1:])