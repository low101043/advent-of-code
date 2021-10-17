import os
from collections import Counter


def partone(input):

    input_split = input.split("\n")
    
    list_one = go_thru_wires(input_split[0])
    list_two = go_thru_wires(input_split[1])
    

    set_data = set(list_one+list_two)
    print(set_data)
    set_of_all = list((Counter(list_one) & Counter(list_two)).elements())
    
    print(set_of_all)

    smallest = None
    smallest_dis = 10000000000000
    
    for i in set_of_all:
        if abs(i[0]) + abs(i[1]) < smallest_dis:
            smallest = i
            smallest_dis = abs(i[0]) + abs(i[1])

    return smallest_dis
        

def go_thru_wires(directions):
    start = [0,0]
    places = []

    for direction in directions.split(','):

        if direction[0] == 'D':
            start, places_new = add_in_between(start, direction, 0, False)
            places += places_new
        elif direction[0] == 'U':
            start, places_new = add_in_between(start, direction, 0, True)
            places += places_new
        elif direction[0] == 'L':
            start, places_new = add_in_between(start, direction, 1, False)
            places += places_new
        else:
            start, places_new = add_in_between(start, direction, 1, True)
            places += places_new
        
    

    return places

def add_in_between(start, direction, place, add):
    places = []
    for i in range(int(direction[1:])):
        if add:
            start[place] += 1
        else:
            start[place] -= 1
        
        places.append(tuple(start))

    return start, places

print(os.getcwd())
with open("2019/day3/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))