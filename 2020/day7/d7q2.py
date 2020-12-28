import csv
import os
import copy

def partone(clean_file):
    to_hold_shiny = set(["shinygold"])
    add_new = False
    while not add_new:
        add_new = True
        for element in clean_file:
            for item in element:
                #print(item)
                if item in to_hold_shiny and element[0] not in to_hold_shiny:
                    print("Hi")
                
                    to_hold_shiny.add(element[0])
                    add_new = False
        #print(to_hold_shiny)

    print(to_hold_shiny)
    to_hold_shiny.remove("shinygold")

    total = 0
    for element in clean_file:
        added = False
        i = 0
        while not added and i < len(element):
            if element[i] in to_hold_shiny:
                added = True
                total += 1
            i += 1

    print(total)

def parttwo(clean_file, to_find):

    total = 0

    for element in clean_file:
        if element[0] == to_find:
            total += len(element) - 1
            for i in range(1,len(element)):
                total += parttwo(clean_file,element[i])
    return total

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/2020/day7")
with open("day7Input1.txt") as data:
    file_to_read = data.read()

bags_split = file_to_read.split("\n")
final_split = []

for item in bags_split:
    if item == "":
        pass
    else:
        item_split = item.split(" ")
        final_split.append(item_split)

clean_file = []
for bags in final_split:
    i = 0
    cleaned_file = []
    to_add = ""
    num_to_add = 1
    while i < len(bags):
        if bags[i] == "bags":
            cleaned_file.append(to_add)
            to_add = ""
            i += 1
        elif bags[i] == "no":
            i = len(bags)
        elif bags[i][-1] == "," or bags[i][-1] == ".":
            for j in range(num_to_add):
                cleaned_file.append(to_add)
            to_add = ""
            num_to_add = 1
        elif bags[i].isnumeric():
            num_to_add = int(bags[i])
        else:
            to_add += bags[i]
        i+=1
    clean_file.append(cleaned_file)

print(clean_file)

#partone(clean_file)
total = parttwo(clean_file, "shinygold")
print(total)