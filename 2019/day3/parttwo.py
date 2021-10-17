import os
from collections import Counter


def partone(input):

    input_split = input.split("\n")
    
    list_one = go_thru_wires(input_split[0])
    list_two = go_thru_wires(input_split[1])

    data_one = [i[0] for i in list_one ]
    data_two = [i[0] for i in list_two]

    set_of_all = list((Counter(data_one) & Counter(data_two)).elements())
    
    print(set_of_all)

    smallest = None
    smallest_dis = 10000000000000
    
    for i in set_of_all:
        index_data_one = data_one.index(i)
        index_data_two = data_two.index(i)
        if list_one[index_data_one][1] + list_two[index_data_two][1] < smallest_dis:
            smallest = i
            smallest_dis = list_one[index_data_one][1] + list_two[index_data_two][1]

    return smallest_dis
        

def go_thru_wires(directions):
    start = [0,0]
    distance = 0
    places = []

    for direction in directions.split(','):

        if direction[0] == 'D':
            start, places_new, distance = add_in_between(start, direction, 0, False, distance)
            places += places_new
        elif direction[0] == 'U':
            start, places_new, distance = add_in_between(start, direction, 0, True, distance)
            places += places_new
        elif direction[0] == 'L':
            start, places_new, distance = add_in_between(start, direction, 1, False, distance)
            places += places_new
        else:
            start, places_new, distance = add_in_between(start, direction, 1, True, distance)
            places += places_new
        
    

    return places

def add_in_between(start, direction, place, add, distance):
    places = []
    for i in range(int(direction[1:])):
        if add:
            start[place] += 1
        else:
            start[place] -= 1

        distance += 1
        
        places.append([tuple(start), distance])

    return start, places, distance

print(os.getcwd())
with open("2019/day3/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))