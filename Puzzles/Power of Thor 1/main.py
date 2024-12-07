import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thor_actual_position = [initial_tx, initial_ty]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    move_to_make = "" #Reset the move variable at the biginning of each turn
    
    #Determine North/South
    if thor_actual_position[1] > light_y:
        move_to_make += "N"
        thor_actual_position[1] -= 1
    elif thor_actual_position[1] < light_y:
        move_to_make += "S"
        thor_actual_position[1] += 1

    #Determine East/West
    if thor_actual_position[0] > light_x:
        move_to_make += "W"
        thor_actual_position[0] -= 1
    elif thor_actual_position[0] < light_x:
        move_to_make += "E"
        thor_actual_position[0] += 1

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move_to_make)