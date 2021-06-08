import os

def partone(input):
    frequency = 0

    for number in input.split("\n"):
        num = int(number)
        frequency += num
    
    return frequency


print(os.getcwd())
with open("2018/day1/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))