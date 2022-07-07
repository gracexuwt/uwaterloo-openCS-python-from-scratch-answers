UNITS = ["zero", "one", "two", "three", "four", "five",
         "six", "seven", "eight", "nine"]

TENS = ["", "", "twenty", "thirty", "forty", "fifty", 
         "sixty", "seventy", "eighty", "ninety"]

TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]

TWENTY = 20
TEN = 10

def two_digit_word(num):
    if((int)(num / 10) == 1):
        unit = num % 10
        return TEENS[unit]
    else:
        ten = (int)(num / 10)
        unit = num % 10
        return TENS[ten] + "-" + UNITS[unit]