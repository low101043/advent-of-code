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
            
def parttwo(input):

    input_split = input.split("\n")

    found_diff = False
    i = 0
    j = 0

    while not found_diff:
        
        check_against = input_split[i]

        for box_id in input_split:
            #print(check_against, box_id)
            if box_id == check_against:
                pass

            else:
                how_many_different = 0

                for j, letter in enumerate(box_id):
                    if letter != check_against[j]:
                        how_many_different += 1

                #print(how_many_different)

                if how_many_different == 1:
                    found_diff = True

                    output = ""
                    for j in range(len(check_against)):
                        letter_one = check_against[j]
                        letter_two = box_id[j]
                        if letter_one == letter_two:
                            output+= letter_one

                    print( output)
                    
                                    

        i += 1

print(os.getcwd())
with open("2018/day2/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))

print(parttwo(file_to_read))