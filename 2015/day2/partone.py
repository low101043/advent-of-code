import csv
import os

def partone(input):
    
    input_split = input.split("\n")
    total = 0
    for dimensions in input_split:

        numbers = dimensions.split("x")
        length = int(numbers[0])
        width = int(numbers[1])
        height = int(numbers[2])
        surface_area = (2 * length * width) + (2 * width * height) + (2 * height * length)

        min_one = min([length, width, height])

        if length == min_one:
            min_two = min([width, height])
        elif width == min_one:
            min_two = min([length, height])
        else:
            min_two = min([length, width])

        smallest_area = min_one * min_two
        total += (smallest_area + surface_area)

    return total
        

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2015/day2")
with open("input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))