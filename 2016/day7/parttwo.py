import os
import hashlib

def parttwo(input):
    input_split = input.split("\n")

    support_ssl = 0
    for line in input_split:
        supernet, hypernet = createParts(line)
        print(supernet, hypernet)
        if checkSSL(supernet, hypernet):
            support_ssl += 1
    return(support_ssl)


def createParts(line):

    hypernet = []
    supernet = []
    hypernetNext = ""
    supernetNext = ""
    in_bracket = ""
    for letter in line:
        print(letter)
        if in_bracket:
            if letter == "]":
                in_bracket = False
                hypernet.append(hypernetNext)
                hypernetNext = ""
                continue
            else:
                hypernetNext += letter
        else:
            if letter == "[":
                in_bracket = True
                supernet.append(supernetNext)
                supernetNext = ""
            else:
                supernetNext += letter

    if not in_bracket:
        supernet.append(supernetNext)
    return supernet, hypernet

def createABA(supernet):
    aba_list = []
    for part in supernet:
        for i in range(len(part)):
            
            if (i + 2 < len(part)):
                to_check = ""           
                if i+2 == len(part) -1:
                    to_check = part[i:]
                else:
                    to_check = part[i:i+3]

                if (to_check[0] == to_check[2] and to_check[0] != to_check[1]):
                    aba_list.append(to_check)

    return aba_list

def check_bab(hypernet, aba_list):
    for part in hypernet:
        for i in range(len(part)):
            
            if (i + 2 < len(part)):
                to_check = ""
                if i+2 == len(part) -1:
                    to_check = part[i:]
                else:
                    to_check = part[i:i+3]

                if (to_check[0] == to_check[2] and to_check[0] != to_check[1]):
                    
                    for aba in aba_list:
                        if to_check[0] == aba[1] and to_check[1] == aba[0]:
                            return True

def checkSSL(supernet, hypernet):
    aba_list = createABA(supernet)
    return check_bab(hypernet, aba_list)



print(os.getcwd())
with open("2016/day7/input.txt") as data:
    file_to_read = data.read()


print(parttwo(file_to_read))