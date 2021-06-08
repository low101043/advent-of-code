import csv
import os
import itertools

# Have to implement Branch and Bound as TSP.  Thanks Wikipedia

def partone(input):
    split_input = input.split("\n")
    data_in_dict, current_best = sortInput(split_input) 
    print(data_in_dict, current_best) 
    # Will brute force (Starts crying)  

    cities = list(data_in_dict.keys())
    print(cities)

    all_permuations = list(itertools.permutations(cities))
    #print(all_permuations)

    for permuation in all_permuations:
        distance = 0
        
        for i in range(0, len(permuation) - 1):
            first_city = permuation[i]
            destination = permuation[i+1]

            distance += data_in_dict[first_city][destination]
            
    
        if (distance < current_best):
            current_best = distance
        
    return current_best
def sortInput(data):
    to_return = {}
    current_dist = 0
    previous = ""
    for line in data:
        cities = line.split(" to ")
        city1 = cities[0]
        data_split_further = cities[1].split(" = ")
        city2 = data_split_further[0]
        distance = int(data_split_further[1])

        if previous != city1:
            previous = city1
            current_dist += distance
        
        if city1 not in to_return.keys():
            to_return[city1] = {city2:distance}
        else:
            old_dict = to_return[city1]
            old_dict[city2] = distance
            to_return[city1] = old_dict
    
        if city2 not in to_return.keys():
            to_return[city2] = {city1:distance}
        else:
            old_dict = to_return[city2]
            old_dict[city1] = distance
            to_return[city2] = old_dict

    
    return to_return, current_dist
        


print(os.getcwd())
with open("2015/day9/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
