import csv
import os

def partone(input):
    
    houses_visited = set([(0,0)])
    current_pos = [0,0]
    for letter in input:
        if letter == "^":
            y_axis = current_pos[1]
            current_pos[1] = y_axis + 1
        elif letter == ">":
            x_axis = current_pos[0]
            current_pos[0] = x_axis + 1
        elif letter == "v":
            y_axis = current_pos[1]
            current_pos[1] = y_axis - 1
        elif letter == "<":
            x_axis = current_pos[0]
            current_pos[0] = x_axis - 1
        else:
            print("ERROR")
        
        tuple_data = tuple(current_pos)
        houses_visited.add(tuple_data)

    return len(houses_visited)
        

def parttwo(input):

    houses_visited = set([(0,0)])
    current_pos_fc = [0,0]
    current_pos_rfc = [0,0]

    fc = True

    for letter in input:
        
        if fc == True:
            if letter == "^":
                y_axis = current_pos_fc[1]
                current_pos_fc[1] = y_axis + 1
            elif letter == ">":
                x_axis = current_pos_fc[0]
                current_pos_fc[0] = x_axis + 1
            elif letter == "v":
                y_axis = current_pos_fc[1]
                current_pos_fc[1] = y_axis - 1
            elif letter == "<":
                x_axis = current_pos_fc[0]
                current_pos_fc[0] = x_axis - 1
            else:
                print("ERROR")

            tuple_data = tuple(current_pos_fc)
            houses_visited.add(tuple_data)
        else:
            if letter == "^":
                y_axis = current_pos_rfc[1]
                current_pos_rfc[1] = y_axis + 1
            elif letter == ">":
                x_axis = current_pos_rfc[0]
                current_pos_rfc[0] = x_axis + 1
            elif letter == "v":
                y_axis = current_pos_rfc[1]
                current_pos_rfc[1] = y_axis - 1
            elif letter == "<":
                x_axis = current_pos_rfc[0]
                current_pos_rfc[0] = x_axis - 1
            else:
                print("ERROR")

            tuple_data = tuple(current_pos_rfc)
            houses_visited.add(tuple_data)

        fc = not fc

    return len(houses_visited)

print(os.getcwd())
with open("2015/day3/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
print(parttwo(file_to_read))