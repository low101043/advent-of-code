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


def parttwo(input):

    num_to_find = int(input)

    facing = 90
    pos = [0,0]
    i = 1

    k = 1

    values = {(0,0):1}

    how_many = 0
    l = 0
    c = 0

    while l <= num_to_find: #and c <2:

        j = 0 
        
        
        while l <= num_to_find and j < k:
            #if l > 0:
            #    print(l)

            
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
            
            #print(i)
            #print(pos)
            total = 0
            for x_value in range(pos[0]-1, pos[0]+2):
                for y_value in range(pos[1]-1, pos[1]+2):
                    
                    if [x_value, y_value] != pos:
                        #print(x_value, y_value)
                        if (x_value, y_value) in values.keys():
                            #print(x_value, y_value)
                            #print(values[(x_value, y_value)])
                            total += values[(x_value, y_value)]
                            #print(total)
                            #print("\n")
            #print(total)
            values[(pos[0], pos[1])] = total
            j += 1
            i += 1
            l = total

            #print(values)
            
            #print("\n")
            #print(pos)
            #print(total)

        
        facing = (facing - 90) % 360
        how_many +=1
        if how_many == 2:
            k += 1
            how_many = 0

        #c += 1
        #print(c)

    print(pos)
    return l
    


print(os.getcwd())
with open("2017/day3/input.txt") as data:
    file_to_read = data.read()

print(file_to_read)

print(parttwo(file_to_read))
