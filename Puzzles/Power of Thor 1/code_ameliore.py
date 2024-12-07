import sys
import math

light_x, light_y, thor_x, thor_y = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    
    move_x, move_y = "", ""
    
    #Determine move_x -> East/West
    if thor_x > light_x:
        move_x = "W"
        thor_x -= 1
    elif thor_x < light_x:
        move_x = "E"
        thor_x += 1

    #Determine move_y -> North/South
    if thor_y > light_y:
        move_y = "N"
        thor_y -= 1
    elif thor_y < light_y:
        move_y = "S"
        thor_y += 1

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move_y + move_x)