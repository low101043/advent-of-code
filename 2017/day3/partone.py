import csv
import os

def partone(input):

    num_to_find = int(input)

    facing = 90
    pos = [0,0]
    i = 1

    k = 1

    how_many = 0
    while i != num_to_find:

        j = 0 
        
        
        while i != num_to_find and j < k:

            
            if facing == 0:
                current_y = pos[1]
                pos[1] = current_y + 1
            elif facing == 90:
                current_x = pos[0]
                pos[0] = current_x + 1
            elif facing == 180:
                current_y = pos[1]
                pos[1] = current_y - 1
            elif facing == 270:
                current_x = pos[0]
                pos[0] = current_x - 1
            else:
                print("How did you get here!!!")
            
            j += 1
            i += 1
            print(pos)
        facing = (facing - 90) % 360
        how_many +=1
        if how_many == 2:
            k += 1
            how_many = 0

    print(pos)
    return(abs(pos[0]) + abs(pos[1]))


print(os.getcwd())
with open("2017/day3/input.txt") as data:
    file_to_read = data.read()

print(file_to_read)

print(partone(file_to_read))
