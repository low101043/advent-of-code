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
os.chdir("/home/low101043/Documents/adventOfCode/2020/day5")
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

list_of_rows = []

row_max = 0
for boarding_pass in numbers:
    row = convertBF(boarding_pass[:7])

    if row > row_max:
        row_max = row
    place = convertLR(boarding_pass[7:])
    seat_id = (row *8) + place


print(row)

for i in range(0,row_max):
    list_of_rows.append([])

print(list_of_rows)

for boarding_pass in numbers:
    row = convertBF(boarding_pass[:7])
    print(row)
    
    row_seats = list_of_rows[row-1]
    
    place = convertLR(boarding_pass[7:])
    seat_id = (row *8) + place
    row_seats.append(seat_id)
    list_of_rows[row-1] = row_seats

print(list_of_rows)

final_rows = []

for row_boarded in list_of_rows:
    if len(row_boarded) == 8:
        pass
    elif len(row_boarded) < 7:
        pass
    else:
        final_rows = row_boarded

final_rows.sort()
print(final_rows)