import csv
import os
from collections import Counter

def partone(input):
    
    split = input.split("\n")

    child = []
    root_maybe = []

    for line in split:
        if line.find("->") == -1:
            pass
        else:
            start_index = line.find("->") + 3
            
            root = line[:line.find(" ")]
            children = line[start_index:]

            if root in child:
                pass
            else:
                root_maybe.append(root)

            children_list = children.split(", ")

            for child_of_root in children_list:
                child.append(child_of_root)


    print(child)
    print(root_maybe)
    for maybe_root in root_maybe:
        if maybe_root not in child:
            return maybe_root
           
def parttwo(input):

    root = partone(input)

    tree = makeTree(input.split("\n"))
    unbalancedNum(tree, root)

    


def unbalancedNum(tree, root):

    node_num = -1
    for node in tree:
        if node[0] == root:
            node_num = node[1]
            

            child_scores = []
            for child in node[2]:
                child_score = unbalancedNum(tree, child)

                child_scores.append((child, child_score))

            if len(child_scores) >= 2:
                for i in range(len(child_scores)-1):
                    if child_scores[i][1] != child_scores[i+1][1]:
                        print(node)
                        print(child_scores)
                        print(child_scores[i][1], child_scores[i][0])
                        print(child_scores[i+1][1], child_scores[i+1][0])
                        print("ERROR")

            for child in child_scores:
                node_num += child[1]

            return node_num

    




def makeTree(split):

    tree = []

    for data in split:
        open_bracket = data.find("(") 
        close_bracket = data.find(")")

        num = int(data[open_bracket+1:close_bracket])

        node_name = data[:open_bracket-1]

        if data.find("->") == -1:
            tree.append((node_name, num, []))
        else:
            start_index = data.find("->") + 3
            
            root = data[:data.find(" ")]
            children = data[start_index:]

            children_list = children.split(", ")

            tree.append((node_name, num, children_list))

    return tree


print(os.getcwd())
with open("2017/day7/input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))
