import csv
import os
import re 

def partOne(classes, other_ticket):
    legal_numbers = set([])
    for data in classes:
        start_end = []
        int_to_add = ""
        for letter in data:
            if letter == "-":
                start_end.append(int(int_to_add))
                int_to_add = ""
            elif letter == " " and int_to_add != "":
                start_end.append(int(int_to_add))
                int_to_add = ""
            elif letter.isnumeric():
                int_to_add += letter
        start_end.append(int(int_to_add))
        print(start_end)

        start_one = start_end[0]
        end_one = start_end[1]

        for i in range(start_one, end_one+1):
            legal_numbers.add(i)
        
        for i in range(start_end[2], start_end[3] + 1):
            legal_numbers.add(i)
        
    print(legal_numbers)

    total_end = 0
    for ticket in other_ticket:
        for number in ticket:
            if number not in legal_numbers:
                total_end += number
    return total_end

print(os.getcwd())
with open("2020/day16/day16Input1.txt") as data:
    file_to_read = data.read()

bags_split = file_to_read.split("\n")
#print(bags_split)
classes = []
my_ticket = []
other_ticket = []

i = 0
while i < len(bags_split):
    if bags_split[i] == "":
        pass
    elif bags_split[i] == "nearby tickets:":
        for i in range(i+1, len(bags_split)):
            data_split = bags_split[i].split(",")
            to_add = []
            for k in range(len(data_split)):
                if (data_split[k] == ""):
                    pass
                else:
                    to_add.append(int(data_split[k]))

            other_ticket.append(to_add)
            
    elif bags_split[i] == "your ticket:":
        i += 1
        print("here")
        data_split = bags_split[i].split(",")
        for k in range(len(data_split)):
            print(data_split[k])
            if (data_split[k] == ""):
                pass
            else:
                my_ticket.append(int(data_split[k]))
    else:
        classes.append(bags_split[i])
    
    i+= 1

print(classes)
print("\n")
print(my_ticket)
print("\n")
print(other_ticket)
        
part_one_answer = partOne(classes,other_ticket)
print(part_one_answer)
            