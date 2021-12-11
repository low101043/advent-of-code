
def partOne(input_text):
    input_in_list = solution_in_list(input_text)

    coords = [0,0]

    for direction in input_in_list:
        if direction[0] == 'f':
            coords[0] = coords[0] + int(direction[-1])
        elif direction[0] == 'u':
            coords[1] = coords[1] - int(direction[-1])
        else:
            coords[1] = coords[1] + int(direction[-1])
    return coords[0] * coords[1]

def partTwo(input_text):
    input_in_list = solution_in_list(input_text)

    coords = [0,0,0]

    for direction in input_in_list:
        if direction[0] == 'f':
            coords[0] = coords[0] + int(direction[-1])
            coords[1] = coords[1] + (coords[2] * int(direction[-1]))
        elif direction[0] == 'u':
            coords[2] = coords[2] - int(direction[-1])
        else:
            coords[2] = coords[2] + int(direction[-1])
    return coords[0] * coords[1]



def solution_in_list(inputText):
    input_split = inputText.split("\n")
    return input_split


with open("2021/day2/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
print(partTwo(file_to_read))
