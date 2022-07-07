def is_multiple(number, factor):
    return number % factor == 0
    
def leap_year(year):
    if(is_multiple(year,100) and is_multiple(year,4) and is_multiple(year,400)):
        return "Leap year"
    elif(is_multiple(year,4) and not is_multiple(year,100)):
        return "Leap year"
    else:
        return "Common year"