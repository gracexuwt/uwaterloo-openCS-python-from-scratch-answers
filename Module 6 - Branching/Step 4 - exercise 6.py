def is_time(hour,minute):
    if(0 <= hour <=23 and 0 <= minute <= 59):
        return "Passes"
    return "Fails"