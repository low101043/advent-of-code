import csv
import os


def in_list(data, to_find):
    for key_value in data:
        if key_value[:3] == to_find:
            return True
    return False

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2020/day4")
with open("day4Input1.txt") as data:
    file_to_read = data.read()

number_to_add = []
numbers = []
to_add = ""

for letter in file_to_read:
    if (letter == " "):
        number_to_add.append(to_add)
        to_add = ""
    elif (letter == "\n"):
        number_to_add.append(to_add)
        to_add = ""
        numbers.append(number_to_add)
        number_to_add = []
    else:
        to_add += str(letter)

number_to_add.append(to_add)
numbers.append(number_to_add)
print(numbers)
print("\n\n")

final_input = []
previous = []
for data in numbers:
    #print(data)
    if (data == ['']):
        final_input.append(previous)
        previous = []
    else:
        for key_value in data:
            previous.append(key_value)

final_input.append(previous)
print(final_input)

valid = 0

for credentials in final_input:

    if (in_list(credentials, "byr") and in_list(credentials, "iyr") and in_list(credentials, "eyr") and in_list(credentials, "hgt") and in_list(credentials, "hcl") and in_list(credentials, "ecl") and in_list(credentials, "pid")):
        valid += 1

print(valid)
