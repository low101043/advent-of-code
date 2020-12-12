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
iteration = 0

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

                row = previous_value[i]
                col = [element[j] for element in previous_value]
                leftmost = j - 1
                upmost = i -1
                #print(leftmost,upmost)

                seats_occupied = []
                found = False
                while (leftmost >= 0 and upmost >= 0 and not found):
                    if (previous_value[upmost][leftmost] == "#"):
                        seats_occupied.append(True)
                        found = True
                    elif (previous_value[upmost][leftmost] == "L"):
                        found = True
                    leftmost -= 1
                    upmost -= 1
            
                #print("Diag Left", len(seats_occupied))

                leftmost = j + 1
                upmost = i + 1
                found = False
                while (leftmost < len(previous_value[i]) and upmost < len(numbers) and not found):
                    if (previous_value[upmost][leftmost] == "#"):
                        seats_occupied.append(True)
                        found = True
                    elif (previous_value[upmost][leftmost] == "L"):
                        found = True
                    leftmost += 1
                    upmost += 1

                #print("Diag Left 2", len(seats_occupied))

                
                leftmost = j + 1
                upmost = i -1
                found = False
                while (leftmost < len(previous_value[i]) and upmost >= 0 and not found):
                    if (previous_value[upmost][leftmost] == "#"):
                        seats_occupied.append(True)
                        found = True
                    elif (previous_value[upmost][leftmost] == "L"):
                        found = True
                    leftmost += 1
                    upmost -= 1

                #print("Diag Right 1", len(seats_occupied))
                leftmost = j -1
                upmost = i + 1
                
                found = False
                while(leftmost >= 0 and upmost < len(numbers)and not found):
                    
                    if (previous_value[upmost][leftmost] == "#"):
                        seats_occupied.append(True)
                        found = True
                    elif (previous_value[upmost][leftmost] == "L"):
                        found = True
                    leftmost -= 1
                    upmost += 1
                #print("Diag Right 2", len(seats_occupied))

                num_row = 1
                found = False
                
                while not found and j - num_row >= 0:
                    if (row[j - num_row] == "#"):
                        seats_occupied.append(True)
                        found = True
                    elif (row[j - num_row] == "L"):
                        found = True
                    
                    num_row += 1

                #print("Left", len(seats_occupied))
                num_row = 1
                found = False
                while not found and num_row + j < len(row):
                    if (row[num_row + j] == "#"):
                        seats_occupied.append(True)
                        found = True
                    elif (row[num_row + j] == "L"):
                        found = True
                    
                    num_row += 1
                #print("Right", len(seats_occupied))

                num_row = 1
                found = False
                while not found and num_row + i < len(col):
                    if (col[num_row + i] == "#"):
                        seats_occupied.append(True)
                        found = True
                    elif (col[num_row + i] == "L"):
                        found = True
                    
                    num_row += 1

                #print("Down", len(seats_occupied))
                num_row = 1
                found = False
                while not found and i - num_row >= 0:
                    if (col[i - num_row] == "#"):
                        seats_occupied.append(True)
                        found = True
                    elif (col[i - num_row] == "L"):
                        found = True
                    
                    num_row += 1
                print("Final")
                print(i, j, len(seats_occupied))
                if (len(seats_occupied) >= 5 and previous_value[i][j] == "#"):
                    
                    new_value[i][j] = "L"
                elif (len(seats_occupied) == 0 and previous_value[i][j] == "L"):
                    new_value[i][j] = "#"
                else:
                    new_value[i][j] = deepcopy(previous_value[i][j])
    print(new_value)
    iteration += 1
        

print(new_value)
seats_occupied_final = 0
for i in new_value:
    for j in i:
        if j == "#":
            seats_occupied_final += 1

print(seats_occupied_final)
