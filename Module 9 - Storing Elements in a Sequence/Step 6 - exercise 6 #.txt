def shift(seq):
    if(len(seq) < 1):
        return seq
    return seq.append(seq.pop(0))