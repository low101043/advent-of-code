import csv
import os

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2020/day12")
with open("day12Input1.txt") as data:
    file_to_read = data.read()

number_to_add = ""
data_to_add = []
numbers = []

for letter in file_to_read:
    if (letter == "\n" and number_to_add != ""):
        number_as_int = int(number_to_add)
        data_to_add.append(number_as_int)
        numbers.append(data_to_add)
        data_to_add = []
        number_to_add = ""
    elif (letter.isalpha()):
        data_to_add.append(letter)

    else:
        number_to_add += str(letter)

print(numbers)

west = 0
east = 0
north = 0
south = 0
angle = 90
for tuple_data in numbers:
    #print(tuple_data)
    #print(tuple_data[0])
    if tuple_data[0] == "N":
        north += tuple_data[1]

    elif tuple_data[0] == "S":
        south += tuple_data[1]

    elif tuple_data[0] == "E":
        east += tuple_data[1]

    elif tuple_data[0] == "W":
        west += tuple_data[1]

    elif tuple_data[0] == "R":
        angle += tuple_data[1]
        angle = angle % 360

    elif tuple_data[0] == "L":
        #print("Here")
        angle -= tuple_data[1]
        while angle < 0:
            angle += 360
        angle = angle % 360
    
    else:
        if angle == 0:
            north += tuple_data[1]
        elif angle == 90:
            east += tuple_data[1]
        elif angle == 180:
            south += tuple_data[1]
        elif angle == 270:
            west += tuple_data[1]
        else:
            print("MUCK UP!")

    print(angle)
    
    print(north, south, east, west)

y_axis = abs(north - south)
x_axis = abs(east - west)

print(y_axis, x_axis)
print(y_axis + x_axis)