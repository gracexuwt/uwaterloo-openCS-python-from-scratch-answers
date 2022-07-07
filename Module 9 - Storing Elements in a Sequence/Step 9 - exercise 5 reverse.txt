def reverse(seq):
    if(len(seq) == 0):
        seq = seq[:]
    else:
        i = 0
        while(i < (int)(len(seq) / 2)):
            temp = seq[i]
            seq[i] = seq[-(i + 1)]
            seq[-(i + 1)] = temp
            i = i + 1
    return seq