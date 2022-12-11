from collections import defaultdict


def parttwo(input):
    forest = input_split(input)

    visible = 0
    for i in range(len(forest)):    # Height
        for j in range(len(forest[i])): #Width
            
            height = forest[i][j]
            i_left = i
            j_left = j
            i_right = i
            j_right = j
            seen_i_left = 0
            seen_j_left = 0
            seen_i_right = 0
            seen_j_right = 0
            #print('\n')
            #print(height)
            while i_left >= 1:
                i_left -= 1
                if forest[i_left][j] < height:
                    seen_i_left += 1
                else: 
                    seen_i_left += 1
                    i_left = 0


            while j_left >= 1:
                j_left -= 1
                if forest[i][j_left] < height:
                    seen_j_left += 1
                else:
                    seen_j_left += 1
                    j_left = 0

            while i_right <= len(forest)-2:
                i_right += 1
                if forest[i_right][j] < height:
                    seen_i_right += 1

                else:
                    seen_i_right += 1
                    i_right = len(forest)

            while j_right <= len(forest[i])-2:
                j_right += 1
                if forest[i][j_right] < height:
                    seen_j_right += 1
                else:
                    seen_j_right += 1
                    j_right = len(forest[i])

            scene = seen_i_left*seen_i_right*seen_j_left*seen_j_right
            if scene > visible:
                visible = scene

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

print(parttwo(file_to_read))
