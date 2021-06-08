import csv
import os

print(os.getcwd())
with open("2020/day14/day14Input1.txt") as data:
    file_to_read = data.read()

number_to_add = ""
numbers = []

for letter in file_to_read:
    if (letter == "\n" and number_to_add != ""):
        number_as_int = str(number_to_add)
        numbers.append(number_as_int)
        number_to_add = ""
    else:
        number_to_add += letter

print(numbers)
mem = {}
print(mem)
mask = ""
for input in numbers:
    if input[0:3] == "mem":
        start_num = input.index("[") + 1
        end_num = input.index("]")
        index = input[start_num:end_num]
        equal_sign = input.index("=")
        number = str(bin(int(input[equal_sign+2:])))[2:]
        print(index, number)

        length = len(number)
        while length != len(mask):
            number = "0" + number
            length = len(number)
        
        print(index, number)

        new_number = ""
        for i, digit in enumerate(number):
            mask_digit = mask[i]
            if mask_digit == "X":
                new_number += digit
            else:
                new_number += mask_digit
        
        mem[index] = new_number
    else:
        mask = input[7:]
        print(mask)

total = 0
for value in mem.values():
    print(value)
    for i in range(len(value)):
        if value[i] == "1":
            to_add = 2 ** (36 - 1-i)
            total += to_add
print(total)
        