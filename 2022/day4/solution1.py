from collections import Counter


def partOne(input):
    input_format = input_split(input)

    total = 0

    for pairs in input_format:
        split_tasks = pairs.split(',')
        elf_one_lower = int(split_tasks[0].split('-')[0])
        elf_one_upper = int(split_tasks[0].split('-')[1])
        elf_two_lower = int(split_tasks[1].split('-')[0])
        elf_two_upper = int(split_tasks[1].split('-')[1])

        if elf_one_lower >= elf_two_lower and elf_one_upper <= elf_two_upper:
            print(elf_one_lower, elf_one_upper)
            print(elf_two_lower, elf_two_upper)
            print('\n')
            total += 1
        elif elf_two_lower >= elf_one_lower and elf_two_upper <= elf_one_upper:
            print(elf_one_lower, elf_one_upper)
            print(elf_two_lower, elf_two_upper)
            print('\n')
            total += 1
#

    return total
        
    

def input_split(input):
    split_input = input.split("\n")

    return split_input


with open("2022/day4/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
