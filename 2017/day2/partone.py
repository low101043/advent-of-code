import csv
import os

def partone(input):

    input_split = input.split("\n")
    print(input_split)
    total = 0

    for row in input_split:
        min = 10000000000000000000000000
        max = -1
        split_num = row.split("\t")

        for number_str in split_num:
            num = int(number_str)

            if num < min:
                min = num
            if num > max:
                max = num

        print(max-min)
        total += (max - min)

    return total

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2017/day2")
with open("input.txt") as data:
    file_to_read = data.read()

print(file_to_read)

print(partone(file_to_read))
