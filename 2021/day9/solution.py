def partOne(input_text):
    input_lava = solution_in_list(input_text)

    risk_total = 0
    for i in range(len(input_lava)):
        row = input_lava[i]
        for j in range(len(row)):
            if check(i, j, input_lava):
                height = input_lava[i][j]
                risk_total += (height+1)

    return risk_total

def check(i, j, input_lava):
    if i == 0 and j == 0:
        return input_lava[i][j] < input_lava[i+1][j] and input_lava[i][j] < input_lava[i][j+1]

    if i == 0 and j == len(input_lava[0])-1:
        return input_lava[i][j] < input_lava[i+1][j] and input_lava[i][j] < input_lava[i][j-1]

    if i == len(input_lava)-1 and j == 0:
        return input_lava[i][j] < input_lava[i-1][j] and input_lava[i][j] < input_lava[i][j+1]

    if i == len(input_lava)-1 and j == len(input_lava[0])-1:
        return input_lava[i][j] < input_lava[i-1][j] and input_lava[i][j] < input_lava[i][j-1]

    if i == 0:
        return input_lava[i][j] < input_lava[i+1][j] and input_lava[i][j] < input_lava[i][j-1] and input_lava[i][j] < input_lava[i][j+1]

    if j == 0:
        return input_lava[i][j] < input_lava[i-1][j] and input_lava[i][j] < input_lava[i+1][j] and input_lava[i][j] < input_lava[i][j+1]

    if i == len(input_lava)-1:
        return input_lava[i][j] < input_lava[i-1][j] and input_lava[i][j] < input_lava[i][j-1] and input_lava[i][j] < input_lava[i][j+1]

    if j == len(input_lava[0]) - 1:
        return input_lava[i][j] < input_lava[i-1][j] and input_lava[i][j] < input_lava[i+1][j] and input_lava[i][j] < input_lava[i][j-1]

    return input_lava[i][j] < input_lava[i-1][j] and input_lava[i][j] < input_lava[i+1][j] and input_lava[i][j] < input_lava[i][j-1] and input_lava[i][j] < input_lava[i][j+1]


def partTwo(input_text):
    input_lava = solution_in_list(input_text)

    sizes = []
    for i in range(len(input_lava)):
        row = input_lava[i]
        for j in range(len(row)):
            if check(i, j, input_lava):
                sizes.append(basin_size(i, j, input_lava))
    sizes.sort(reverse=True)
    print(sizes)
    return sizes[0] * sizes[1] * sizes[2]

def basin_size(i, j, input_lava):
    to_check = [(i, j)]
    basin = set([])
    while to_check:
        num_to_check = to_check.pop()
        if num_to_check in basin:
            continue
        basin.add(num_to_check)
        basin_around = check_if_basin(num_to_check, input_lava)
        to_check = to_check + basin_around
    #    print(to_check)
   # print(i,j, basin, len(basin), input_lava[i][j])
    return len(basin)


def check_if_basin(coords, input_lava):
    i = coords[0]
    j = coords[1]
    coords_fig = input_lava[i][j]
    to_return = []

    if i != 0 and input_lava[i-1][j] > coords_fig and input_lava[i-1][j] != 9:
        to_return.append((i-1, j))
    if i != len(input_lava)-1 and input_lava[i+1][j] > coords_fig and input_lava[i+1][j] != 9:
        to_return.append((i+1, j))
    if j != 0 and input_lava[i][j-1] > coords_fig and input_lava[i][j-1] != 9:
        to_return.append((i, j-1))
    if j != len(input_lava[0])-1 and input_lava[i][j+1] > coords_fig and input_lava[i][j+1] != 9:
        to_return.append((i, j+1))

    #print(coords, to_return)
    return to_return


def solution_in_list(inputText):

    end = [[int(num) for num in second_half] for second_half in inputText.split("\n")]
    return end


with open("2021/day9/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
print(partTwo(file_to_read))
