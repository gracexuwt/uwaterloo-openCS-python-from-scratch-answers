def max_diff(seq):
    new = seq[:]
    new.sort()
    return new[-1] - new[0]