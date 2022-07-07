def helper(num, offset):
    if(65 <= num + offset <= 90):
        return num + offset
    while(offset != 0):
        if(offset > 0):
            offset = offset - 1
            if(num == 90):
                num = 65
            else:
                num = num + 1
        else:
            offset = offset + 1
            if(num == 65):
                num = 90
            else:
                num = num - 1
    return num

def caesar(string, offset):
    new = ""
    for char in string:
        new = new + chr(helper(ord(char), offset))
    return new