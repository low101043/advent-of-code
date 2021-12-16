def partOne(input_text):
    positions = solution_in_list(input_text)
    max_pos = max(positions)

    max_dis = 1000000000000000
    pos = -1
    for i in range(max_pos+1):
        total_move = 0
        for crab in positions:
            total_move += abs(crab - i)

        if total_move < max_dis:
            max_dis = total_move
            pos = i

    return max_dis

def partTwo(input_text):
    positions = solution_in_list(input_text)
    max_pos = max(positions)

    max_dis = 10000000000000000
    pos = -1
    for i in range(max_pos+1):
        total_move = 0
        for crab in positions:
            amount_to_move = abs(crab - i)
            total_move += count_up(amount_to_move)

        if total_move < max_dis:
            max_dis = total_move
            pos = i

    return max_dis

def count_up(to_end):
    total = 0
    for i in range(to_end+1):
        total+=i

    return total

def solution_in_list(inputText):
    return [int(num) for num in inputText.split(",")]

with open("2021/day7/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
print(partTwo(file_to_read))
