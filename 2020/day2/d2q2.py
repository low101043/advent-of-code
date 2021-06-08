import csv
import os

print(os.getcwd())
with open("2020/day2/day2Input1.txt") as data:
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

number_of_valid = 0
for input in numbers:
    print(input)
    low = 1000000000000
    high = -1
    number = ""
    start_of_word = False
    i = 0
    letter_to_check = ""
    while not start_of_word:
        letter = input[i]
        if (letter == '-'):
            low = int(number)
            number = ""
            i += 1
        elif (letter == " "):
            high = int(number)
            letter_to_check = input[i+1]
            i = i +4
            start_of_word = True
        else:
            number += letter
            i += 1

    print(low, high, letter_to_check)

    password = input[i:]
    print(password)
    letter_found = 0
    
    letter_1 = password[low-1]
    letter_2 = password[high-1]
    print(letter_1, letter_2)

    letter_1_truth = letter_1 == letter_to_check
    letter_2_truth = letter_2 == letter_to_check

    if letter_1_truth ^ letter_2_truth:
        number_of_valid += 1

print(number_of_valid)
        
