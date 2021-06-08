import os
import string

def partone(input):
    
    input_split = input.split("\n")

    two_letters = 0
    three_letters = 0

    for box_id in input_split:

        found_two = False
        found_three = False

        for letter in string.ascii_lowercase:

            letter_in = 0

            for letter_id in box_id:
                if letter_id == letter:
                    letter_in += 1

            if (letter_in == 2 and not found_two):
                two_letters += 1
                found_two = True
            if letter_in == 3 and not found_three:
                three_letters += 1
                found_three = True

    print(two_letters, three_letters)

    return two_letters * three_letters
            

print(os.getcwd())
with open("2018/day2/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
