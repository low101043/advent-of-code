import csv
import os

print(os.getcwd())
with open("2020/day8/day8Input1.txt") as data:
    file_to_read = data.read()

number_to_add = ""
instruction = []
numbers = []

for letter in file_to_read:
    if (letter == " " and number_to_add != ""):
        instruction.append(number_to_add)
        number_to_add = ""
    elif (letter == " " and number_to_add == ""):
        pass
    elif (letter == "\n"):
        number_as_int = int(number_to_add)
        instruction.append(number_as_int)
        numbers.append(instruction)
        number_to_add = ""
        instruction = []
    else:
        number_to_add += letter

print(numbers)

acc = 0
done_command = [False for i in range(len(numbers))]
command_to_execute = 0
print(command_to_execute)
while not done_command[command_to_execute]:
    command = numbers[command_to_execute]
    if command[0] == "acc":
        acc += command[1]
        done_command[command_to_execute] = True
        command_to_execute += 1
    elif command[0] == "jmp":
        done_command[command_to_execute] = True
        command_to_execute += command[1]
    else:
        done_command[command_to_execute] = True
        command_to_execute += 1
    print(command_to_execute, acc)

print(acc)