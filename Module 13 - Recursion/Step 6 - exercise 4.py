def is_multiple(number, factor):
    return number % factor == 0
    
def divides_all(seq, factor):
    if(len(seq) == 0):
        return True
    if(not is_multiple(seq[0], factor)):
        return False
    return divides_all(seq[1:], factor)