import os

def partone(input):

    input_split = input.split(",")
    memory = []

    for i, number in enumerate(input_split):
        if i == 1:
            memory.append(12)
        elif i == 2:
            memory.append(2)
        else:
            memory.append(int(number))

    memory = intcode_run(memory)

    return memory[0]
        

def intcode_run(memory):

    opcode_pos = 0
    opcode = memory[opcode_pos]

    while opcode != 99:
        

        if opcode == 1:

            add_one_pos = memory[opcode_pos + 1]
            add_two_pos = memory[opcode_pos + 2]

            add_one = memory[add_one_pos]
            add_two = memory[add_two_pos]

            store = memory[opcode_pos + 3]
            
            added = add_one + add_two

            #print(add_one,add_two,store,added)

            memory[store] = added
        
        elif opcode == 2:
            mult_one_pos = memory[opcode_pos + 1]
            mult_two_pos = memory[opcode_pos + 2]

            mult_one = memory[mult_one_pos]
            mult_two = memory[mult_two_pos]

            store = memory[opcode_pos + 3]

            multiplied = mult_one * mult_two

            memory[store] = multiplied


        elif opcode== 99:
            print("Finished")
        else:
            print("Illegal Opcode")

        opcode_pos += 4
        opcode = memory[opcode_pos]

    return memory

    


print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2019/day2")
with open("input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
print(intcode_run([1,0,0,0,99]))