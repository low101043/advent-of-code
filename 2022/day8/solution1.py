from collections import defaultdict


def partOne(input):
    forest = input_split(input)

    visible = 0
    for i in range(len(forest)):    # Height
        for j in range(len(forest[i])): #Width
            if i == 0 or j == 0 or i == len(forest)-1 or j == len(forest[i])-1: 
                visible += 1

            else:
                height = forest[i][j]
                i_left = i
                j_left = j
                i_right = i
                j_right = j
                seen_i_left = True
                seen_j_left = True
                seen_i_right = True
                seen_j_right = True
                #print('\n')
                #print(height)
                while i_left >= 1:
                    i_left -= 1
                    if forest[i_left][j] >= height:
                        seen_i_left = False

                while j_left >= 1:
                    j_left -= 1
                    if forest[i][j_left] >= height:
                        seen_j_left = False

                while i_right <= len(forest)-2:
                    i_right += 1
                    if forest[i_right][j] >= height:
                        seen_i_right = False

                while j_right <= len(forest[i])-2:
                    j_right += 1
                    if forest[i][j_right] >= height:
                        seen_j_right = False

                if seen_i_left or seen_j_left or seen_i_right or seen_j_right:
                    visible += 1
#                    print(height)

    return visible

    
        
def input_split(input):
    forest = []
    split_input = input.split("\n")
    for line in split_input:
        line_to_add = []
        for num in list(line):
            line_to_add.append(int(num))
        forest.append(line_to_add)

    return forest


with open("2022/day8/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
