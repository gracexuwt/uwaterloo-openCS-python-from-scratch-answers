string = input("Please input a string of length at least two")
length = (int)(len(string)/2)
print(string[:length].upper() + string[length:].lower())