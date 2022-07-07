def is_multiple(number, factor):
    return number % factor == 0
    
def divides_all(seq, factor):
    i = 0
    while(i < len(seq)):
        if(not is_multiple(seq[i],factor)):
            return False
        i = i + 1
    return True