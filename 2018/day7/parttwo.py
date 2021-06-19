import os
import string

#BASE ASSUMPTION MIGHT BE WRONG

def parttwo(input):
    
    input_split = input.split("\n")

    tree = {}
    children = []
    all_letters = []
    for line in input_split:
        node = line[5]
        child = line[-12]
        children.append(child)
        all_letters.append(child)
        
        if node not in tree.keys():
            tree[node] = [child]
        else:
            data = tree[node]
            data.append(child)
            tree[node] = data



    solution = ""
    queue = []

    elf_working = [False for i in range(5)]
    time_working = [0 for i in range(5)]
    letter_on = ["" for i in range(5)]


    for node in tree.keys():
        if node not in children:
            queue.append(node)

    all_letters += queue 
    time = -1
    
    while len(all_letters) > 0 or any(elf_working):
        queue.sort()
        print(time)
        print(elf_working)
        print(letter_on)
        print(time_working)
        print(all_letters)
        print(queue)

        for i, elf in enumerate(elf_working):
            if (elf) == True:
                time_working[i] = time_working[i] -1
                if (time_working[i] <= 0):
                    elf_working[i] = False
                    next_children = []
                    letter = letter_on[i]
                    letter_on[i] = ""
                    if letter in tree.keys():
                        next_children = tree[letter]

                    queue = queue + next_children 
        
        time += 1
        
        queue.sort()
        check = len(queue) > 0 and not all(elf_working)
        while check: # REWRITE
            letter = queue.pop(0)

            first = all_letters.index(letter)

            last = len(all_letters) - 1 - all_letters[::-1].index(letter)

            all_letters.remove(letter)
            print(letter, last, first)
            if (last == first):
                elf_work = elf_working.index(False)
                time_working[elf_work] = ord(letter) - 64 + 60
                elf_working[elf_work] = True
                letter_on[elf_work] = letter

            check = len(queue) > 0 and not all(elf_working)


                          

    print(tree)

    return time
    
    
print(os.getcwd())
with open("2018/day7/input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))

