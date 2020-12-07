import csv
import os

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/2020/day6")
with open("day6Input1.txt") as data:
    file_to_read = data.read()

number_to_add = []
answer = ""
numbers = []

for letter in file_to_read:
    if (letter == "\n" and answer != ""):
        number_as_int = answer
        number_to_add.append(number_as_int)
        answer = ""
    elif (letter == "\n" and answer == ""):
        numbers.append(number_to_add)
        number_to_add = []
    else:
        answer += str(letter)

print(numbers)
yes = 0
for group in numbers:

    yes_group = []

    for person in group:
        for letter in person:
            if (letter not in yes_group):
                yes_group.append(letter)
    
    yes += len(yes_group)

print(yes)