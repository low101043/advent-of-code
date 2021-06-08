import csv
import os

print(os.getcwd())
with open("2020/day3/day3Input1.txt") as data:
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
pos_3 = 0
pos_1 = 0
pos_5 = 0
pos_7 = 0
pos_12 = 0
gone_thru = False
encounters_3 = 0
encounters_1 = 0
encounters_5 = 0
encounters_7 = 0
encounters_12 = 0

for row in numbers:
    if not gone_thru:
        gone_thru = True
    else:
        pos_3 = pos_3 + 3
        pos_1 = pos_1 + 1
        pos_5 = pos_5 + 5
        pos_7 = pos_7 + 7
        if (pos_3 >= len(row)):
            pos_3 = pos_3 % len(row)
        if (row[pos_3] == '#'):
            encounters_3 += 1

        if (pos_1 >= len(row)):
            pos_1 = pos_1 % len(row)
        if (row[pos_1] == '#'):
            encounters_1 += 1
        
        if (pos_5 >= len(row)):
            pos_5 = pos_5 % len(row)
        if (row[pos_5] == '#'):
            encounters_5 += 1

        if (pos_7 >= len(row)):
            pos_7 = pos_7 % len(row)
        if (row[pos_7] == '#'):
            encounters_7 += 1

row_to_check = 2
while (row_to_check < len(numbers)):
    row_here = numbers[row_to_check]
    pos_12 += 1
    print(pos_12, len(row_here))
    print(pos_12 >= len(row_here))
    if (pos_12 >= len(row_here)):
        pos_12 = pos_12 % len(row_here)
        
    if (row_here[pos_12] == '#'):
        encounters_12 += 1
    row_to_check += 2

print(encounters_1, encounters_3, encounters_5, encounters_7,  encounters_12)    
print(encounters_3 * encounters_1 * encounters_12 * encounters_5 * encounters_7)
        
