def reverse(seq):
    if(len(seq) == 0):
        return []
    return [seq[-1]] + reverse(seq[:-1])