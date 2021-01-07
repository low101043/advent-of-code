import os

def partone(input):

    input_split = input.split("\n")
    total_possible = 0

    for triangle in input_split:
        triangle_split = triangle.split(" ")
        print(triangle_split)
        triangle_to_use = []

        for possible_input in triangle_split:
            if possible_input == "":
                pass
            else:
                triangle_to_use.append(int(possible_input))

        print(triangle_to_use)

        max_num = max(triangle_to_use)

        num_to_add = [number for number in triangle_to_use if number != max_num]

        print(max_num, num_to_add)
        if len(num_to_add) < 2:
            total_possible += 1

        elif (num_to_add[0] + num_to_add[1]) > max_num:
            total_possible += 1

    return total_possible



print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2016/day3")
with open("input.txt") as data:
    file_to_read = data.read()


print(partone(file_to_read))