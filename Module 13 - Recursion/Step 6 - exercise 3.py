def all_equal(seq):
    if(len(seq) == 0 or len(seq) == 1):
        return True
    if(seq[0] != seq[1]):
        return False
    return all_equal(seq[1:])