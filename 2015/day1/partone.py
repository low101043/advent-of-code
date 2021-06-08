import csv
import os

def partone(input):
    floor = 0

    for bracket in input:
        if bracket == "(":
            floor += 1
        elif bracket == ")":
            floor -= 1

    return floor

print(os.getcwd())
with open("2015/day1/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))