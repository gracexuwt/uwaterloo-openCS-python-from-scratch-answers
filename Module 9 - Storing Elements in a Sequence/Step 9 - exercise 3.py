def remove_zero(seq):
    i = 0
    while(0 in seq):
        seq.remove(0)
    return seq