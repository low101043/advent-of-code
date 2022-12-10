
def partOne(input):
    input_format = input_split(input)

    total = 0
    conv = {'Y': 'B', 'X':'A', 'Z':'C'}
    move_score = {'X': 1, 'Y': 2, 'Z': 3}
    for round in input_format:
        split = round.split(" ")
        opponent = split[0]
        agent = conv[split[1]]

        if opponent == agent:
            total += (move_score[split[1]]+3)
        elif opponent == 'A' and agent == 'B':
            total += (move_score[split[1]]+6)
        elif opponent == 'B' and agent == 'C':
            total += (move_score[split[1]]+6)
        elif opponent == 'C' and agent == 'A':
            total += (move_score[split[1]]+6)
        else:
            total += (move_score[split[1]])

    return total

        
    

def input_split(input):
    split_input = input.split("\n")

    return split_input


with open("2022/day2/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
