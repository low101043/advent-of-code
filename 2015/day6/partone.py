import csv
import os

def partone(input):
    split_input = input.split("\n")
    for line in split_input:
        print(line)
        if line[4] == " " and line[7] == "f":
            # Must be turn off
            turnOff(line[9:])
            
        
        elif line[4] == " ":
            # Must be turn on
            turnOn(line[8:])
        else:
            # Must be toggle
            toggle(line[7:])

    total = 0
    for row in global_lighting:
        for light in row:
            if light == True:
                total += 1
    return total

def coord_data(data):
    comma_split = data.find(",")
    through = data.find(" through ")

    coord_one = [int(data[:comma_split]), int(data[comma_split+1: through])]
    

    second_part = data[through + 9:]
    comma_split_2 = second_part.find(",")
    
    coord_two = [int(second_part[:comma_split_2]), int(second_part[comma_split_2+1:])]

    return coord_one, coord_two

def turnOff(data):
    coord_one, coord_two = coord_data(data)
    for i in range(coord_one[0], coord_two[0] + 1):
        for j in range(coord_one[1], coord_two[1] + 1):
            global_lighting[i][j] = False
    

    

def turnOn(data):
    coord_one, coord_two = coord_data(data)
    for i in range(coord_one[0], coord_two[0] + 1):
        for j in range(coord_one[1], coord_two[1] + 1):
            global_lighting[i][j] = True
    

def toggle(data):
    coord_one, coord_two = coord_data(data)
    for i in range(coord_one[0], coord_two[0] + 1):
        for j in range(coord_one[1], coord_two[1] + 1):
            
            global_lighting[i][j] = not global_lighting[i][j]

global_lighting = [[False for i in range(1000)] for i in range(1000)]
#print(global_lighting)
print(os.getcwd())
with open("2015/day6/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
