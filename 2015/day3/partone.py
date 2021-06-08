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
        

print(os.getcwd())
with open("2015/day3/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))