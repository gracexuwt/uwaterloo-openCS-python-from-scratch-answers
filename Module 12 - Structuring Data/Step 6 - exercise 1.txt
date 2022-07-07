def number_pixels(seq, colour):
    count = 0
    for item in seq:
        for i in item:
            if i == colour:
                count = count + 1
    return count