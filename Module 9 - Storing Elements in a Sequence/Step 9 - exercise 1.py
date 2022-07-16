def sum(seq):
    if(len(seq) == 0):
        return 0
    i = 0
    sums = 0
    while(i < len(seq)):
        sums = sums + seq[i]
        i = i + 1
    return sums