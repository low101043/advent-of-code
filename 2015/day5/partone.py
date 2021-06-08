import csv
import os

def partone(input):
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
    vowels = 0
    double = False

    for i in range(len(string)):
        letter = string[i]
        if letter in ["a", "e", "i", "o", "u"]:
            vowels += 1
        if i != len(string) -1:
            if letter == string[i+1]:
                double = True
            if i + 2 < len(string):
                if string[i:i+2] in ["ab", "cd", "pq", "xy"]:
                    return False
            else:
                if string[i:] in ["ab", "cd", "pq", "xy"]:
                    return False
    if (vowels >= 3) and double:
        return True
    return False

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2015/day5")
with open("input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
