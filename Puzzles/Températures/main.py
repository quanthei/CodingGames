import sys
import math

def determine_temperature_most_close_to_0(tested_t : int) -> int:
    if tested_t *-1 == t_more_close: 
        return abs(tested_t)
    elif abs(tested_t) < abs(t_more_close):
        return tested_t 
    else:
        return t_more_close
    
n = int(input())  # the number of temperatures to analyse
if n == 0 : 
    print(0) # If there is no temperture given -> return 0
else:
    t_more_close = 10000
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t_more_close = determine_temperature_most_close_to_0(int(i))
  
    print(t_more_close)