import os
import string

#BASE ASSUMPTION MIGHT BE WRONG

def partone(input):
    
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

    for node in tree.keys():
        if node not in children:
            queue.append(node)

    all_letters += queue 
    
    while len(queue) != 0:
        queue.sort()
        print(all_letters)

        letter = queue.pop(0)

        first = all_letters.index(letter)

        print(len(all_letters))
        last = len(all_letters) - 1 - all_letters[::-1].index(letter)

        all_letters.remove(letter)
        print(letter, last, first)
        if (last == first):
            solution += letter


            next_children = []
            if letter in tree.keys():
                next_children = tree[letter]

            queue = queue + next_children        

    print(tree)

    return solution
    
    
print(os.getcwd())
with open("2018/day7/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))

