import os
import hashlib

def partone(input):
    input_split = input.split("\n")

    support_tls = 0
    for line in input_split:
        if checkTLS(line):
            support_tls += 1
    return(support_tls)

def checkTLS(line):

    bracket = ""
    in_bracket = False
    correct = False
    for i in range(len(line)):
        if in_bracket:
            if line[i] == "]":
                in_bracket = False
                if checkTLS(bracket):
                    return False
                bracket = ""
                continue
            else:
                bracket += line[i]
        else:   
            if line[i] == "[":
                in_bracket = True

            if (i + 3 < len(line)):
                to_check = ""
                if i+3 == len(line) -1:
                    to_check = line[i:]
                else:
                    to_check = line[i:i+4]

                if (to_check[0] == to_check[3] and to_check[1] == to_check[2] and to_check[0] != to_check[1]):
                    correct = True

    return correct

print(os.getcwd())
with open("2016/day7/input.txt") as data:
    file_to_read = data.read()


print(partone(file_to_read))