import os

def partone(input):
    frequency = 0

    for number in input.split("\n"):
        num = int(number)
        frequency += num
    
    return frequency

def parttwo(input):


    input_split = input.split("\n")
    frequency = 0
    frequencies_seen = set([])

    i = 0 
    found = False

    while (not found):
        change = int(input_split[i])
        frequency += change

        if frequency in frequencies_seen:
            return frequency
        else:
            frequencies_seen.add(frequency)

        i = (i + 1) % len(input_split)

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2018/day1")
with open("input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
print(parttwo(file_to_read))