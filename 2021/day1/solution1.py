
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


def solution_in_list(inputText):
    input_split = inputText.split("\n")
    return input_split


with open("2021/day1/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
