import os
KEY_TABLE = [[1,2,3],[3,5,6],[7,8,9]]
KEY_TABLE_TWO = [[None,None,1,None,None],
                [None, 2, 3, 4, None],
                [5,6,7,8,9],
                [None, "A", "B", "C", None],
                [None, None, "D", None, None]]


def partone(input):

    input_split = input.split("\n")
    pos = [1,1]

    for set_to_use in input_split:
        num = number_here(set_to_use,pos)

        print(num)

        for i in range(len(KEY_TABLE)):
            for j in range(len(KEY_TABLE[i])):
                if KEY_TABLE[i][j] == num:
                    pos = [i,j]


def number_here(input,pos):
    
    print(pos)
    for letter in input:

        if letter == "R":
            if pos[1] < 2:
                pos[1] = pos[1] + 1
        elif letter == "L":
            if pos[1] > 0:
                pos[1] = pos[1] - 1
        elif letter == "U":
            if pos[0] > 0:
                pos[0] = pos[0] - 1
        else:
            if pos[0] < 2:
                pos[0] = pos[0] + 1

    return KEY_TABLE[pos[0]][pos[1]]

def parttwo(input):
    input_split = input.split("\n")
    pos = [2,0]
    #print(KEY_TABLE_TWO[pos[0]][pos[1]])

    for set_to_use in input_split:
        num = number_here_two(set_to_use,pos)

        print(num)

        for i in range(len(KEY_TABLE_TWO)):
            for j in range(len(KEY_TABLE_TWO[i])):
                if KEY_TABLE_TWO[i][j] == num:
                    pos = [i,j]

def number_here_two(input, pos):

    #print(input,pos)

    for letter in input:
        #print(letter)
        if letter == "R":
            old_value = pos[1]
            new_value = old_value + 1
            if new_value < len(KEY_TABLE_TWO[0]) and KEY_TABLE_TWO[pos[0]][new_value] != None:
                pos[1] = new_value

        elif letter == "L":
            old_value = pos[1]
            new_value = old_value - 1
            if new_value >= 0 and KEY_TABLE_TWO[pos[0]][new_value] != None:
                pos[1] = new_value

        elif letter == "D":
            old_value = pos[0]
            new_value = old_value + 1
            if new_value < len(KEY_TABLE_TWO[0]) and KEY_TABLE_TWO[new_value][pos[1]] != None:
                pos[0] = new_value

        else:

            old_value = pos[0]
            new_value = old_value - 1
            #print(new_value)
            if new_value >= 0 and KEY_TABLE_TWO[new_value][pos[1]] != None:
                pos[0] = new_value

        #print(letter, KEY_TABLE_TWO[pos[0]][pos[1]])
    #print(pos)
    return KEY_TABLE_TWO[pos[0]][pos[1]]
                

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2016/day2")
with open("input.txt") as data:
    file_to_read = data.read()


#print(partone(file_to_read))
print(parttwo(file_to_read))