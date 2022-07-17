def shuffle(l1, l2):
    l = zip(l1,l2)
    new = []
    for item in l:
        for t in item:
            new = new + [t]
    return new