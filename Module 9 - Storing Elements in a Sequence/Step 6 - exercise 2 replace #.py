def replace(seq, old, new):
    if old in seq:
        if new not in seq:
            seq[seq.index(old)] = new
            return seq