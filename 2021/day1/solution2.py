
def partOne(input_text):
    input_in_list = solution_in_list(input_text)

    before = int(input_in_list[0])
    down = 0
    for num in input_in_list:
        if num != '' and int(num) > before:
            down+=1
        if num != '':
            before = int(num)

    return down

def partTwo(input_text):
    input_in_list = solution_in_list(input_text)

    three_split = input_in_list[:3]
    before = sum(three_split)
    down = 0
    for i, num in enumerate(input_in_list[0:]):
        three_split[i%3] = num
        new_num = sum(three_split)
        # print(three_split)
        # print(before)
        # print(new_num)
        # print("")
        if new_num > before:
            down += 1
        before = new_num
    
    return down


def solution_in_list(inputText):
    input_split = inputText.split("\n")
    input_split = [int(num) for num in input_split if num != '']
    return input_split


with open("2021/day1/input.txt") as data:
    file_to_read = data.read()

print(partTwo(file_to_read))
