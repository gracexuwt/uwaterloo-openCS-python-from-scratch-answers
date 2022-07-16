def no_zero(seq):
    new = seq[:]
    while(0 in new):
        new.remove(0)
    return new