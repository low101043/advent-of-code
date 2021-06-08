import csv
import os

print(os.getcwd())
with open("2020/day13/day13Input1.txt") as data:
    file_to_read = data.read()

number_to_add = ""
numbers = []

for letter in file_to_read:
    if (letter == "\n" and number_to_add != ""):
        number_as_int = int(number_to_add)
        numbers.append(number_as_int)
        number_to_add = ""
    elif letter == "," and number_to_add != "x":
        number_as_int = int(number_to_add)
        numbers.append(number_as_int)
        number_to_add = ""
    elif letter == "," and number_to_add == "x":
        number_as_int = number_to_add
        numbers.append(number_as_int)
        number_to_add = ""
    else:
        number_to_add += letter

print(numbers)
earliest = numbers.pop(0)
print(earliest, numbers)

smallest_gap = 1000000000000
number_used = 0

for number in numbers:
    if number == "x":
        pass
    else:
        factor = earliest // number
        if (factor == 0):
            smallest_gap == 0
            number_used = number
        else:
            next_num = factor + 1
            next_bus = next_num * number
            diff = next_bus - earliest
            if diff < smallest_gap:
                smallest_gap = diff
                number_used = number

print(number_used * smallest_gap)
