import sys
import math

def determine_temperature_most_close_to_0(tested_t : int) -> int:
    return 0 if n == 0 # If there is no temperture given -> return 0
    return tested_t if abs(tested_t) < abs(t_more_close) else return t_more_close

t_more_close = 10000
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t_more_close = determine_temperature_most_close_to_0(int(i))

print(t_more_close)