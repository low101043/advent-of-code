import csv
import os

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2020/day14")
with open("day14Input1.txt") as data:
    file_to_read = data.read()

number_to_add = ""
numbers = []

for letter in file_to_read:
    if (letter == "\n" and number_to_add != ""):
        number_as_int = str(number_to_add)
        numbers.append(number_as_int)
        number_to_add = ""
    else:
        number_to_add += letter

print(numbers)
mem = {}
print(mem)
mask = ""
for input in numbers:
    if input[0:3] == "mem":
        start_num = input.index("[") + 1
        end_num = input.index("]")
        index = str(bin(int(input[start_num:end_num])))[2:]
        equal_sign = input.index("=")
        number = int(input[equal_sign+2:])
        print(index, number)

        length = len(index)
        while length != len(mask):
            index = "0" + index
            length = len(index)
        
        print(index, number)

        new_number = ""
        number_of_xs = 0
        for i, digit in enumerate(index):
            mask_digit = mask[i]
            if mask_digit == "X":
                number_of_xs += 1
                new_number += mask_digit
            elif mask_digit == "1":
                new_number += "1"
            else:
                new_number += digit
            
        
        #print(new_number, number, number_of_xs)
        for i in range(2**number_of_xs):
            digits_could_be = []
            for j in range(number_of_xs):
                below_to_reach = i - (i%(2**j))
                even_or_odd = below_to_reach // (2**j)
                if even_or_odd % 2 == 0:
                    digits_could_be.append("1")
                else:
                    digits_could_be.append("0")
            #print("Digits could be", digits_could_be)
            index_to_use = 0
            new_index = ""
            for old_index in new_number:
                if old_index != "X":
                    new_index += old_index
                else:
                    new_index += digits_could_be[index_to_use]
                    index_to_use +=1
            #print(new_index, new_number)
            mem[new_index] = number
        #print(mem)
                 
        
    else:
        mask = input[7:]
        print(mask)

total = 0
for value in mem.values():
    total += value
print(total)
        