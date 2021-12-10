import os


def partone(input):

    input_split = input.split("-")
    print(input_split)

    total = 0
    for i in range(int(input_split[0]), int(input_split[1]) +1):
        total += check_legal(str(i))

    print(total)


def check_legal(num):
    prev = None

    double = False
    for letter in num:
        if prev is None:
            prev = letter
            continue
        if letter == prev:
            double = True
        if int(prev) > int(letter):
            return 0

        prev = letter
    
    if double:
        return 1
    else:
        return 0
   

print(os.getcwd())
with open("2019/day4/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))