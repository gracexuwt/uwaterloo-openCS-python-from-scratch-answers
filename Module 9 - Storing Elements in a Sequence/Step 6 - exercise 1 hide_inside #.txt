def hide_inside(seq, item, pos):
    if(pos >= len(seq)):
        seq = seq + [item]
    elif(pos == 0):
        seq = [item] + seq
    else:
        seq = seq[:pos] + [item] + seq[pos:]
        
    return seq