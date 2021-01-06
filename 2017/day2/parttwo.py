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

def parttwo(input):
    input_split = input.split("\n")
    print(input_split)
    total = 0
    for row in input_split:


        found = False
        final_one = 0
        final_two = 0

        i = 0
        j = 0
        

        split_num = row.split("\t")
        print(split_num)

        while not found:
            num_one = int(split_num[i])
            print(i, num_one)
            for number in split_num:
                num_two = int(number)

                if (num_one % num_two == 0 and num_one != num_two):
                    found = True
                    print(num_one, num_two)
                    final_one = num_one
                    final_two = num_two
                    print("Found")
            i += 1

        total += int(final_one /final_two)
        

    return total

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2017/day2")
with open("input.txt") as data:
    file_to_read = data.read()

print(file_to_read)

print(partone(file_to_read))
print("\n")
print(parttwo(file_to_read))
