import os
import hashlib

def parttwo(input):
    input_split = input.split("\n")
    input_in_col = [[] for i in range(len(input_split[0]))]
    input_in_col = setUp(input_split, input_in_col)
    #print(input_in_col)

    word = ""
    for column in input_in_col:
        word += mostFrequent(column)

    return word
    
def setUp(data, input_col):
    
    for line in data:
        
        for i in range(len(line)):
            data_to_append = input_col[i]
            data_to_append.append(line[i])
            input_col[i] = data_to_append
    
    return input_col

def mostFrequent(letters):
    frequency = {}

    for letter in letters:
        if letter not in frequency.keys():
            frequency[letter] = 1
        else:
            previous = frequency[letter]
            frequency[letter] = previous + 1

    most = 1000000000000000000
    most_frequent = ""
    for key, values in frequency.items():
        if values < most:
            most_frequent = key
            most = values

    return most_frequent

print(os.getcwd())
with open("2016/day6/input.txt") as data:
    file_to_read = data.read()


print(parttwo(file_to_read))