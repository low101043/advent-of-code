import csv
import os
from collections import Counter

def partone(input):
    
    split = input.split("\n")

    child = []
    root_maybe = []

    for line in split:
        if line.find("->") == -1:
            pass
        else:
            start_index = line.find("->") + 3
            
            root = line[:line.find(" ")]
            children = line[start_index:]

            if root in child:
                pass
            else:
                root_maybe.append(root)

            children_list = children.split(", ")

            for child_of_root in children_list:
                child.append(child_of_root)


    print(child)
    print(root_maybe)
    for maybe_root in root_maybe:
        if maybe_root not in child:
            return maybe_root
           


print(os.getcwd())
with open("2017/day7/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
