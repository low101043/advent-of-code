import csv
import os

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2020/day15")
with open("day15Input1.txt") as data:
    file_to_read = data.read()


numbers = file_to_read.split(",")
print(numbers)

int_numbers = []
for number in numbers:
    actual_number = number
    if number.__contains__("\n"):
        print("Found")
        actual_number = ""
        for element in number:
            if element.isnumeric():
                actual_number += element
    int_numbers.append(int(actual_number))

print(int_numbers)

ones_used = {}

num_got_to = 1
old_number = int_numbers[num_got_to-1]

while num_got_to <= 2020:
    print("Number said at", num_got_to, "is ",old_number)
    if old_number not in ones_used.keys():
        ones_used[old_number] = num_got_to
        num_got_to += 1
        if num_got_to <= len(int_numbers):
            old_number = int_numbers[num_got_to-1]
        else:
            old_number = 0
    else:
        last_used = ones_used[old_number]
        print(last_used)
        ones_used[old_number] = num_got_to
        num_got_to += 1
        if num_got_to <= len(int_numbers):
            old_number = int_numbers[num_got_to-1]
        else:
            old_number = num_got_to - last_used -1 
print(old_number)