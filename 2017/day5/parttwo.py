import csv
import os
from collections import Counter

def parttwo(input):
    input_split = input.split("\n")

    in_line = setUp(input_split)
    print(in_line)

    i = 0
    steps = 0
    while i < len(in_line):
        to_jump = in_line[i]
        if (to_jump < 3):
            in_line[i] = to_jump + 1
        else:
            in_line[i] = to_jump - 1
        i += to_jump
        steps += 1

    return(steps)

    

def setUp(data):

    to_return = []
    for number in data:
        to_return.append(int(number))

    return to_return
    
    



print(os.getcwd())
with open("2017/day5/input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))
