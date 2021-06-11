import csv
import os
from collections import Counter

def parttwo(input):
    
    memory = setUp(input)

    finished = False
    seen_before = [memory.copy()]
    steps = 0
    while not finished:
        #print(memory)
        max_num = max(memory)
        index = memory.index(max_num)
        memory[index] = 0
        index +=1
        if (index == len(memory)):
                index = 0
        while max_num > 0:
            memory[index] = memory[index] + 1
            index += 1
            if (index == len(memory)):
                index = 0
            max_num -= 1
        steps += 1
        #print(memory)
        #print(seen_before)
        
        if memory in seen_before:
            return steps - seen_before.index(memory)
        else:
            seen_before.append(memory.copy())
            
def setUp(input):
    input_split = input.split("\t")
    

    return [int(x) for x in input_split]
    


print(os.getcwd())
with open("2017/day6/input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))
