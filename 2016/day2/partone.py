import os

def partone(input):

    input_split = input.split("\n")

    for set_to_use in input_split:
        num = number_here(set_to_use)

        print(num)


def number_here(input):
    KEY_TABLE = [[1,2,3],[3,5,6],[7,8,9]]
    pos = [1,1]
    for letter in input:

        if letter == "R":
            if pos[1] < 2:
                pos[1] = pos[1] + 1
        elif letter == "L":
            if pos[1] > 0:
                pos[1] = pos[1] - 1
        elif letter == "U":
            if pos[0] > 0:
                pos[0] = pos[0] - 1
        else:
            if pos[0] < 2:
                pos[0] = pos[0] + 1

    return KEY_TABLE[pos[0]][pos[1]]



print(os.getcwd())
with open("2016/day2/input.txt") as data:
    file_to_read = data.read()


print(partone(file_to_read))