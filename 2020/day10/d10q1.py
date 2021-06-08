import csv
import os

print(os.getcwd())
with open("2020/day10/day10Input1.txt") as data:
    file_to_read = data.read()

number_to_add = ""
numbers = []

for letter in file_to_read:
    if (letter == "\n" and number_to_add != ""):
        number_as_int = int(number_to_add)
        numbers.append(number_as_int)
        number_to_add = ""
    else:
        number_to_add += letter

print(numbers)
numbers.sort()
print(numbers)

last_value = numbers[-1] + 3
numbers.append(last_value)

difference_1 = 0
difference_2 = 0
difference_3 = 0
previous = 0

for number in numbers:
    print(previous, number)
    previous_diff = number - previous
    previous = number
    print(previous)
    if previous_diff == 1:
        difference_1 += 1
    elif previous_diff == 2:
        difference_2 += 1
    elif previous_diff == 3:
        difference_3 += 1
    else:
        print("Error")
print(difference_1, difference_2, difference_3)

print(difference_1 * difference_3)