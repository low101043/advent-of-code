import csv
import os
from copy import copy, deepcopy

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/2020/day11")
with open("day11Input1.txt") as data:
    file_to_read = data.read()

number_to_add = []
numbers = []

for letter in file_to_read:
    if (letter == "\n" and number_to_add != []):
        number_as_int = number_to_add
        numbers.append(number_as_int)
        number_to_add = []
    else:
        number_to_add += str(letter)

print(numbers)

previous_value = []
new_value = deepcopy(numbers)
#print(new_value)
print(new_value[0-1])

while new_value != previous_value:

    previous_value = deepcopy(new_value)
    print("\n\n")
    print(previous_value)
    for i in range(len(previous_value)):
        for j in range(len(previous_value[i])):
            new_value[i][j] = ""
    print(previous_value)
    print(new_value)
    print("\n")
    for i in range(len(previous_value)):
        for j in range(len(previous_value[i])):

            #print("Debug: ", i, j)
            if previous_value[i][j] == ".":
                new_value[i][j] = "."
            else:
            
                next_to = [False for i in range(8)]


                try:
                    if (i -1 < 0):
                        pass
                    elif (j - 1< 0):
                        pass
                    elif previous_value[i-1][j-1] == "#":
                        next_to[0] = True
                except:
                    print("Error")

                try:
                    if (i -1 < 0):
                        pass
                    elif previous_value[i-1][j] == "#":
                        next_to[1] = True
                except:
                    print("Error")

                try:
                    if (i -1 < 0):
                        pass
                    elif previous_value[i-1][j+1] == "#":
                        next_to[2] = True
                except:
                    print("Error")

                try:
                    if (j-1 < 0):
                        pass
                    elif previous_value[i][j-1] == "#":
                        next_to[3] = True
                except:
                    print("Error")

                try:
                    if previous_value[i][j+1] == "#":
                        next_to[4] = True
                except:
                    print("Error")
        
                try:
                    if (j-1 < 0):
                        pass
                    elif previous_value[i+1][j-1] == "#":
                        next_to[5] = True
                except:
                    print("Error")
        
                try:
                    if previous_value[i+1][j] == "#":
                        next_to[6] = True
                except:
                    print("Error")

                try:

                    if previous_value[i+1][j+1] == "#":
                        next_to[7] = True
                except:
                    print("Error")

                seats_occupied = [True for place in next_to if place == True]

                print(len(seats_occupied))
                if (len(seats_occupied) >= 4 and previous_value[i][j] == "#"):
                    
                    new_value[i][j] = "L"
                elif (len(seats_occupied) == 0 and previous_value[i][j] == "L"):
                    new_value[i][j] = "#"
                else:
                    new_value[i][j] = deepcopy(previous_value[i][j])
    print(new_value)
        

print(new_value)
seats_occupied_final = 0
for i in new_value:
    for j in i:
        if j == "#":
            seats_occupied_final += 1

print(seats_occupied_final)
