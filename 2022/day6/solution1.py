from collections import Counter


def partOne(input):

    for i in range(4, len(input)):
        last_four = set(input[i-4:i])

        if len(last_four) == 4:
            return i




with open("2022/day6/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
