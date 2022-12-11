from collections import Counter


def parttwo(input):

    for i in range(14, len(input)):
        last_four = set(input[i-14:i])

        if len(last_four) == 14:
            return i




with open("2022/day6/input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))
