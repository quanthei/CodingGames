import sys
import math

light_x, light_y, thor_x, thor_y = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())

    move_x = "W" * (thor_x > light_x) + "E" * (thor_x < light_x) ; thor_x += (light_x > thor_x) - (light_x < thor_x)
    move_y = "N" * (thor_y > light_y) + "S" * (thor_y < light_y) ; thor_y += (light_y > thor_y) - (light_y < thor_y)

    print(move_y + move_x)