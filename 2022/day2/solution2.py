
def partTwo(input):
    input_format = input_split(input)

    total = 0
    move_score = {'A': 1, 'B': 2, 'C': 3}
    for round in input_format:
        split = round.split(" ")
        opponent = split[0]
        result = split[1]


        if result == 'X':
            if opponent == 'A':
                total += 3
            elif opponent == 'B':
                total += 1
            else:
                total += 2

        elif result == 'Y':
            total += (3 + move_score[opponent])

        else:
            if opponent == 'A':
                total += (6+2)
            elif opponent == 'B':
                total += (6+3)
            else:
                total += (6+1)

    return total

        
    

def input_split(input):
    split_input = input.split("\n")

    return split_input


with open("2022/day2/input.txt") as data:
    file_to_read = data.read()

print(partTwo(file_to_read))
