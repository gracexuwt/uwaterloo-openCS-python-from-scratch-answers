import math
big = 8 * 10
small = 6 * 10
one = 2 * (big + small)
all_rooms = 20 * one
one_can_coverage = 5 * 350
cans = math.ceil(all_rooms / one_can_coverage)
print(cans)