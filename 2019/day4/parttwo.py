import os


def parttwo(input):

    input_split = input.split("-")
    print(input_split)

    total = 0
    for i in range(int(input_split[0]), int(input_split[1]) +1):
        total += check_legal(str(i))

    print(total)


def check_legal(num):
    prev = None

    for letter in num:
        if prev is None:
            prev = letter
            continue
        if int(prev) > int(letter):
            return 0

        prev = letter
    
    data = [(num[0] == num[1]),
            (num[1] == num[2]),
            (num[2] == num[3]),
            (num[3] == num[4]),
            (num[4] == num[5]),
            ]

    total_true = 0
    for truth in data:
        if truth:
            total_true += 1

    if total_true == 1:
        return 1
    else:
        return 0
   

print(os.getcwd())
with open("2019/day4/input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))