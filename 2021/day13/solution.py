def partOne(input_text):
    instructions, coords = solution_in_list(input_text)
    print(instructions)
    set_instructions = set(coords)

    instruction_one = instructions[0]

    new_set = set([])
    number = int(instruction_one.split("=")[1])
    if "x" in instruction_one:
        for coord in set_instructions:
            gap_to_line = coord[0] - number
            if (gap_to_line < 0):
                new_set.add(coord)
                continue
            new_x = number - gap_to_line
            if new_x >= 0:
                new_set.add((new_x, coord[1]))
    else:
        for coord in set_instructions:
            print(coord)
            gap_to_line = coord[1] - number
            if (gap_to_line < 0):

                #print("Smaller")
                #print(coord)
                new_set.add(coord)
                continue
            new_y = number - gap_to_line
            if new_y >= 0:
           #     print((coord[0], new_y))
                new_set.add((coord[0], new_y))
            #print("")

    return len(new_set)
    
def folding(old_coords, instructions):

    for instruction in instructions:
        new_set = set([])
        number = int(instruction.split("=")[1])
        if "x" in instruction:
            for coord in old_coords:
                gap_to_line = coord[0] - number
                if (gap_to_line < 0):
                    new_set.add(coord)
                    continue
                new_x = number - gap_to_line
                if new_x >= 0:
                    new_set.add((new_x, coord[1]))
        else:
            for coord in old_coords:
                print(coord)
                gap_to_line = coord[1] - number
                if (gap_to_line < 0):

                    #print("Smaller")
                    #print(coord)
                    new_set.add(coord)
                    continue
                new_y = number - gap_to_line
                if new_y >= 0:
            #     print((coord[0], new_y))
                    new_set.add
        old_coords = new_set
    return new_set


def partTwo(input_text):
    instructions, coords = solution_in_list(input_text)
    print(instructions)
    set_instructions = set(coords)

    final_coords = folding(set_instructions, instructions)

    print(final_coords)
    


def solution_in_list(inputText):
    split = inputText.split("\n")

    coords = []
    instructions = []
    for line in split:
        if not line:
            pass
        elif line[0] == "f":
            instructions.append(line)
        elif "," in line:
            two_nums = line.split(",")
            coords.append((int(two_nums[0]), int(two_nums[1])))

    return instructions, coords
            


with open("2021/day13/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
print(partTwo(file_to_read))