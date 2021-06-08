import csv
import os

print(os.getcwd())
with open("2020/day6/day6Input1.txt") as data:
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

    for i, person in enumerate(group):
        print(yes_group)
        person_yes = []
        for letter in person:
            person_yes.append(letter)
        if (i == 0):
            yes_group = person_yes
        else:
            to_remove = []
            intermediate_yes = []
            for element in yes_group:
                if (element not in person_yes):
                    to_remove.append(element)
                else:
                    intermediate_yes.append(element)
            
            yes_group = intermediate_yes
                
            
            
    
    yes += len(yes_group)

print(yes)