def partOne(input_text):
    input = solution_in_list(input_text)
    total = 0
    for row in input:
        outputs = row.split(" ")
        for output in outputs:
            length = len(output)
            if length in [2, 4, 3, 7]:
                total += 1

    return total


def partTwo(input_text):
    pass


def solution_in_list(inputText):
    each_row = inputText.split("\n")
    end = [second_half.split(" | ")[1] for second_half in each_row]
    return end


with open("2021/day8/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
print(partTwo(file_to_read))
