
def partOne(input):
    input_format = input_split(input)

    max = 0
    total = 0
    for num in input_format+[""]:
        if num == "":
            if total > max:
                max = total
            total = 0

        else:
            num_int = int(num)
            total += num_int

    return max
    

def input_split(input):
    split_input = input.split("\n")

    return split_input


with open("2022/day1/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
