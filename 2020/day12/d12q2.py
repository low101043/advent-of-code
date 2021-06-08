import csv
import os

print(os.getcwd())
with open("2020/day12/day12Input1.txt") as data:
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


waypoint_north = 1
waypoint_east = 10
for tuple_data in numbers:
    #print(tuple_data)
    #print(tuple_data[0])
    if tuple_data[0] == "N":
        waypoint_north += tuple_data[1]

    elif tuple_data[0] == "S":
        waypoint_north -= tuple_data[1]

    elif tuple_data[0] == "E":
        waypoint_east += tuple_data[1]

    elif tuple_data[0] == "W":
        waypoint_east -= tuple_data[1]

    elif tuple_data[0] == "R":
        data = tuple_data[1]
        while data != 0:
            temp = waypoint_north
            waypoint_north = -1 *waypoint_east
            waypoint_east = temp
            data -= 90

    elif tuple_data[0] == "L":
        #print("Here")
        data = tuple_data[1]
        while data != 0:
            temp = waypoint_north
            waypoint_north = waypoint_east
            waypoint_east = -1 *temp
            data -= 90
    
    else:
        if waypoint_north < 0:
            south += abs(waypoint_north) * tuple_data[1]
        else:
            north += waypoint_north * tuple_data[1]
        if waypoint_east < 0:
            west += abs(waypoint_east) * tuple_data[1]
        else:
            east += waypoint_east * tuple_data[1]

    print(north, south, east, west)
    print(waypoint_east, waypoint_north)
    print("\n")

y_axis = abs(north - south)
x_axis = abs(east - west)

print(y_axis, x_axis)
print(y_axis + x_axis)