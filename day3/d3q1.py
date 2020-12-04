import csv
import os

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/2020/day3")
with open("day3Input1.txt") as data:
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
pos = 0
gone_thru = False
encounters = 0
for row in numbers:
    if not gone_thru:
        gone_thru = True
    else:
        pos = pos + 3
        if (pos >= len(row)):
            pos = pos % len(row)
        if (row[pos] == '#'):
            encounters += 1

print(encounters)
        
