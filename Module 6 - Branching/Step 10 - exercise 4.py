def off_peak(time):
    if(type(time) != type(0) or time < 0 or time >= 24):
        return "Not a time"
    elif(9 <= time <= 17):
        return "Peak"
    else:
        return "Off peak"