import os

def parttwo(input):

    input_split = input.split("\n")
    total = 0
    for line in input_split:
        room_name = line[:line.rfind("-")]
        str_room_num = line[line.rfind("-") +1: line.find("[")]
        room_num = int(str_room_num)
        #print(room_num)
        #print(room_name)
        increase_by = room_num % 26
        #print(increase_by)

        final_word = ""
        for letter in room_name:
            if letter == "-":
                final_word += " "
            else:
                #print(letter)
                num = ord(letter) + increase_by
                #print(num)
                if num > 122:
                    num -= 26

                letter_add = chr(num)
                #print(letter_add)

                final_word += letter_add

        print(final_word, str_room_num)
        

    return total



print(os.getcwd())
with open("2016/day4/input.txt") as data:
    file_to_read = data.read()


print(parttwo(file_to_read))