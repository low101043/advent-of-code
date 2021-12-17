def partOne(input_text):
    lantern_fish = solution_in_list(input_text)
    for i in range(80):
        new_lantern = []
        for num in lantern_fish:
            if num == 0:
                new_lantern.append(6)
                new_lantern.append(8)
            else:
                new_lantern.append(num-1)
        lantern_fish = new_lantern

    return len(lantern_fish)

def partTwo(input_text):
    lantern_fish = solution_in_list(input_text)
    for i in range(256):
        new_lantern = []
        for num in lantern_fish:
            if num == 0:
                new_lantern.append(6)
                new_lantern.append(8)
            else:
                new_lantern.append(num-1)
        lantern_fish = new_lantern



def solution_in_list(inputText):
    return [int(num) for num in inputText.split(",")]

with open("2021/day6/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
print(partTwo(file_to_read))
