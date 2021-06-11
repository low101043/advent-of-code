import os
import string

def partone(data):
    
    i = 0
    
    while i < len(data) -1:

        letter = data[i]
        next_letter = data[i+1]
        if (letter.islower() and next_letter == letter.capitalize()):
            del data[i+1]
            del data[i]            
            i = 0
        elif letter.isupper() and next_letter == letter.lower():
            del data[i+1]
            del data[i]            
            i = 0
        else:
            i += 1

    return len(data)
        

def parttwo(input):
    smallest = 1000000000000
    for letter in string.ascii_lowercase:
        print(letter)
        data_list = [x for x in input if x != letter and x != letter.upper()]
        if len(input) == len(data_list):
            continue
        length = partone(data_list)
        if length < smallest:
            smallest = length

        

    return smallest


    
print(os.getcwd())
with open("2018/day5/input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))

