import os
import string

def partone(input):
    
    i = 0
    data = list(input)
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
        


    
print(os.getcwd())
with open("2018/day5/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))

