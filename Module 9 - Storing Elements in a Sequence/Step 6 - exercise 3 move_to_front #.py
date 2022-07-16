def move_to_front(seq, item):
    if(item in seq and seq.index(item) != 0):
        seq.remove(item)
        seq[:] = [item] + seq[:]