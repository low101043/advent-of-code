from collections import defaultdict


def partOne(input):
    instructions = input_split(input)

    counter = 0
    total = 0
    x = 1
    instruction_play = False
    left = 0
    to_add = 0
    prev = 'no_op'
    for num in range(1, 221):
        if left == 0:
            instruction_play = False
            if prev == 'addx':
                x += to_add
        if num in (20, 60, 100, 140, 180, 220):
            print(num, x)
            print(x*num)
            print('\n')
            total += (x*num)
        if not instruction_play:
            instruction = instructions[counter]
            counter += 1
            if instruction[0] == 'n':
                prev = 'no_op'

                continue
            else:
                prev = 'addx'
                instruction_play = True
                left = 2
                to_add = int(instruction[5:]) 

        if instruction_play and left > 0:
            left -= 1
    
    return total

    
        
def input_split(input):
    split_input = input.split("\n")

    return split_input


with open("2022/day10/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))

#