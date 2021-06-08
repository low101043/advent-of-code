import csv
import os

def partone(input):

    total = 0
    previous = input[-1]
    for letter in input:
        if letter == previous:
            total += int(letter)
        
        previous = letter

    return total

print(os.getcwd())
with open("2017/day1/input.txt") as data:
    file_to_read = data.read()

print(type(file_to_read))

print(partone(file_to_read))
