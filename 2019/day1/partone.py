import os

def partone(input):

    input_split = input.split("\n")
    total = 0
    for mass in input_split:
        fuel = (int(mass) // 3) - 2
        total += fuel
    
    return total


print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2019/day1")
with open("input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
