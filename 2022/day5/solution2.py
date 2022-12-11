from collections import Counter


def parttwo(input):
    input_format = input_split(input)
    stacks = input_format[0]
    instructions = input_format[1]

    stack = stack_format(stacks)
    instructions_formatted = convert_instructions(instructions)

    for instruction in instructions_formatted:
        stack_from = instruction[1]-1
        stack_to = instruction[2]-1
        num = instruction[0]

        to_add = []
        for i in range(num):
            old_stack = stack[stack_from]
            num_to_add = old_stack.pop()
            stack[stack_from] = old_stack
            to_add.append(num_to_add)
       # print(to_add)

        reversed = to_add[::-1]
       # print(reversed)
        for num_to_add in reversed:
            old_to_stack = stack[stack_to]
            old_to_stack.append(num_to_add)
            stack[stack_to] = old_to_stack

    final_output = ''
    for s in stack:
        final_output += s.pop()

    return final_output
        
def convert_instructions(instructions):
    final_instruct = []

    for instruction in instructions.split('\n'):
        instruct_split = instruction.split(' ')
        list_to_use = [int(instruct_split[1]), int(instruct_split[3]), int(instruct_split[5])]
        final_instruct.append(list_to_use)

    return final_instruct


def stack_format(stack):
    split_into_lines = stack.split('\n')
    stack_num_line = split_into_lines[-1]
    split_on_space = list(stack_num_line)
    num_of_stacks = split_on_space[-2]

    stacks = [[] for i in range(int(num_of_stacks))]

    for i in range(len(split_into_lines)-1):
        index = -(2 + (i))
        split_line = list(split_into_lines[index])
        for i in range(0, len(split_line), 4):
            data = split_line[i:i+3]
            index_in_stacks = int(i/4)
            if data[0] == '[':
                current_stack = stacks[index_in_stacks]
                current_stack.append(data[1])
                stacks[index_in_stacks] = current_stack
            

    return stacks
        
def input_split(input):
    split_input = input.split("\n\n")

    return split_input


with open("2022/day5/input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))
