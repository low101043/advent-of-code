import csv
import os
import itertools

# Have to implement Branch and Bound as TSP.  Thanks Wikipedia

def partone(input):
    final_num = 0
    for i in range(40):
        output = ""
        length = 1
        for j in range(len(input)):
            num1 = input[j]
            if (j +1 >= len(input)):
                output += str(length)
                output += num1
                length = 1
            else:
                num2 = input[j+1]
                if (num1 == num2):
                    length += 1
                else:
                    output += str(length)
                    output += num1
                    length = 1
        #print(input)
        input = output
    return len(input)

print(os.getcwd())
with open("2015/day10/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
