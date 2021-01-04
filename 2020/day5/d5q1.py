import csv
import os

def convertBF(array_input):
    input_reversed = array_input[::-1]
    print(input_reversed)

    row = 0
    for num in range(0, len(array_input)):
        if (input_reversed[num] == "B"):
            to_add = 2 ** num
            row += to_add
    return row

def convertLR(array_input):
    input_reversed = array_input[::-1]
    print(input_reversed)

    row = 0
    for num in range(0, len(array_input)):
        if (input_reversed[num] == "R"):
            to_add = 2 ** num
            row += to_add
    return row

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2020/day5")
with open("day5Input1.txt") as data:
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
print(numbers[0])

max = -1
for boarding_pass in numbers:
    row = convertBF(boarding_pass[:7])
    place = convertLR(boarding_pass[7:])
    seat_id = (row *8) + place

    if (seat_id > max):
        max = seat_id

print(max)