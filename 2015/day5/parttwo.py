import csv
import os

def parttwo(input):
    input_split = input.split("\n")
    num_nice = 0
    for string in input_split:
        if string == "":
            pass
        else:
            print(string)
            nice = checkNiceness(string)
            print(nice)
            if nice:
                num_nice += 1

    return num_nice
    
def checkNiceness(string):
    repeat = False
    overlapping = {}
    overlapping_final = False

    for i in range(len(string)):
        letter = string[i]
        if i + 1 >= len(string):
            pass
        else:
            keyLetters = letter + string[i+1]
            key = (keyLetters, i, i + 1)
            if keyLetters not in overlapping.keys():
                overlapping[keyLetters] = key
            else:
                old_info = overlapping[keyLetters]
                if (old_info[2] != key[1]):
                    overlapping_final = True


        if i + 1 >= len(string) or i + 2 >= len(string):
            pass
        else:
            if letter == string[i+2]:
                repeat = True

    return repeat and overlapping_final
                

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2015/day5")
with open("input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))
