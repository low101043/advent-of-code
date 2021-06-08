import os

def partone(input):

    input_split = input.split("\n")
    total_possible = 0

    for triangle in input_split:
        triangle_split = triangle.split(" ")
        print(triangle_split)
        triangle_to_use = []

        for possible_input in triangle_split:
            if possible_input == "":
                pass
            else:
                triangle_to_use.append(int(possible_input))

        print(triangle_to_use)

        max_num = max(triangle_to_use)

        num_to_add = [number for number in triangle_to_use if number != max_num]

        print(max_num, num_to_add)
        if len(num_to_add) < 2:
            total_possible += 1

        elif (num_to_add[0] + num_to_add[1]) > max_num:
            total_possible += 1

    return total_possible


def check(triangle_to_use):
    max_num = max(triangle_to_use)

    num_to_add = [number for number in triangle_to_use if number != max_num]

    print(max_num, num_to_add)
    if len(num_to_add) < 2:
        return 1

    elif (num_to_add[0] + num_to_add[1]) > max_num:
        return 1
    
    else:
        return 0

def parttwo(input):

    input_split = input.split("\n")
    total_possible = 0

    print(input_split)

    triangles = []

    for triangle in input_split:
        triangle_split = triangle.split(" ")
        print(triangle_split)
        triangle_to_use = []

        for possible_input in triangle_split:
            if possible_input == "":
                pass
            else:
                triangle_to_use.append(int(possible_input))

        triangles.append(triangle_to_use)

    print(triangles)

    for i in range(len(triangles) // 3):
        
        for j in range(3):
            triangle_to_check = [triangles[i*3][j], triangles[(i*3)+1][j], triangles[(i*3)+2][j]]

            print(triangle_to_check)

            total_possible += check(triangle_to_check)


    return total_possible

print(os.getcwd())
with open("2016/day3/input.txt") as data:
    file_to_read = data.read()


#print(partone(file_to_read))
print(parttwo(file_to_read))
