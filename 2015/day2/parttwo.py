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
        
def parttwo(input):

    input_split = input.split("\n")
    total = 0
    for dimensions in input_split:

        numbers = dimensions.split("x")
        length = int(numbers[0])
        width = int(numbers[1])
        height = int(numbers[2])

        side_one = (2 * length) + (2 * width)
        side_two = (2 * height) + (2 * width)
        side_three = (2 * height) + (2 * length)

        min_ribbon = min([side_one,side_two,side_three])
        cubic_ribbon = height * length * width

        total += (min_ribbon + cubic_ribbon)

    return total
    
print(os.getcwd())
with open("2015/day2/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
print(parttwo(file_to_read))