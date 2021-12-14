def partOne(input_text):
    coords = solution_in_list_part_one(input_text)
    set_of_coords = set([])
    set_already_overlapping = set([])
    overlap = 0
    for pairwise in coords:
        if pairwise[0][0] == pairwise[1][0]:        # x Coords same
            if pairwise[0][1] > pairwise[1][1]:
                for num in range(pairwise[1][1], pairwise[0][1]+1):
                    new_num = (pairwise[0][0], num)
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
            
            else:
                for num in range(pairwise[0][1], pairwise[1][1] + 1):
                    new_num = (pairwise[0][0], num)
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
                        
        else:           # y coords same
            if pairwise[0][0] > pairwise[1][0]:
                for num in range(pairwise[1][0], pairwise[0][0] + 1):
                    new_num = (num, pairwise[0][1])
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
            
            else:
                for num in range(pairwise[0][0], pairwise[1][0]+1):
                    new_num = (num, pairwise[0][1])
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)

        # print(set_of_coords, set_already_overlapping)

    return overlap


def partTwo(input_text):
    coords = solution_in_list_part_two(input_text)

    debug = [[0 for i in range(10)] for j in range(10)]
    set_of_coords = set([])
    set_already_overlapping = set([])
    overlap = 0
    for pairwise in coords:
        if pairwise[0][0] == pairwise[1][0]:        # x Coords same
            if pairwise[0][1] > pairwise[1][1]:
                for num in range(pairwise[1][1], pairwise[0][1]+1):
                    new_num = (pairwise[0][0], num)
                    # print(new_num)
                    # num = debug[new_num[1]][new_num[0]]
                    # debug[new_num[1]][new_num[0]] = num + 1
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
            
            else:
                for num in range(pairwise[0][1], pairwise[1][1] + 1):
                    new_num = (pairwise[0][0], num)
                    # print(new_num)
                    # num = debug[new_num[1]][new_num[0]]
                    # debug[new_num[1]][new_num[0]] = num + 1
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
                        
        elif pairwise[0][1] == pairwise[1][1]:           # y coords same
            if pairwise[0][0] > pairwise[1][0]:
                for num in range(pairwise[1][0], pairwise[0][0] + 1):
                    new_num = (num, pairwise[0][1])
                    # print(new_num)
                    # num = debug[new_num[1]][new_num[0]]
                    # debug[new_num[1]][new_num[0]] = num + 1
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
            
            else:
                for num in range(pairwise[0][0], pairwise[1][0]+1):
                    new_num = (num, pairwise[0][1])
                    # print(new_num)
                    # num = debug[new_num[1]][new_num[0]]
                    # debug[new_num[1]][new_num[0]] = num + 1
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
        
        else:
            if pairwise[0][0] > pairwise[1][0] and pairwise[0][1] > pairwise[1][1]: #x1 > x2 , y1>y2
                for num in range(pairwise[0][0] - pairwise[1][0]+1):
                    new_num = (pairwise[1][0] + num, pairwise[1][1] + num)
                    # print(new_num)
                    # num = debug[new_num[1]][new_num[0]]
                    # debug[new_num[1]][new_num[0]] = num + 1
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
            elif pairwise[0][0] > pairwise[1][0] and pairwise[0][1] < pairwise[1][1]: #x1 > x2 , y1<y2
                for num in range(pairwise[0][0] - pairwise[1][0]+1):
                    new_num = (pairwise[1][0] + num, pairwise[1][1] - num)
                    # print(new_num)
                    # num = debug[new_num[1]][new_num[0]]
                    # debug[new_num[1]][new_num[0]] = num + 1
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
            elif pairwise[0][0] < pairwise[1][0] and pairwise[0][1] > pairwise[1][1]: #x1 < x2 , y1>y2
                for num in range(pairwise[1][0] - pairwise[0][0]+1):
                    new_num = (pairwise[1][0] - num, pairwise[1][1] + num)
                    # print(new_num)
                    # num = debug[new_num[1]][new_num[0]]
                    # debug[new_num[1]][new_num[0]] = num + 1
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
            elif pairwise[0][0] < pairwise[1][0] and pairwise[0][1] < pairwise[1][1]:   # x1 < x2, y1<y2
                for num in range(pairwise[1][0] - pairwise[0][0]+1):
                    new_num = (pairwise[1][0] - num, pairwise[1][1] - num)
                    # print(new_num)
                    # num = debug[new_num[1]][new_num[0]]
                    # debug[new_num[1]][new_num[0]] = num + 1
                    if new_num not in set_of_coords and new_num not in set_already_overlapping:
                        set_of_coords.add(new_num)
                    elif new_num in set_of_coords and new_num not in set_already_overlapping:
                        overlap += 1
                        set_already_overlapping.add(new_num)
                        set_of_coords.remove(new_num)
            else:
                print("Idiot how did you get here")
            #x1 > x2, y1> y2
            #x1 > x2, y2> y1

       # print(set_of_coords, set_already_overlapping)
    #print(debug)
    return overlap


def solution_in_list_part_two(input_text):
    needed_coords = []

    split_input = input_text.split("\n")

    for vent in split_input:
        two_sided = vent.split(" -> ")
        coords = []
        for posisition in two_sided:
            x,y = posisition.split(",")
            coords.append((int(x), int(y)))

        needed_coords.append(coords)
        

    return needed_coords

def solution_in_list_part_one(inputText):
    needed_coords = []

    split_input = inputText.split("\n")

    for vent in split_input:
        two_sided = vent.split(" -> ")
        coords = []
        for posisition in two_sided:
            x,y = posisition.split(",")
            coords.append((int(x), int(y)))
        
        if coords[0][0] == coords[1][0] or coords[0][1] == coords[1][1]:
            needed_coords.append(coords)

    return needed_coords

with open("2021/day5/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
print(partTwo(file_to_read))
