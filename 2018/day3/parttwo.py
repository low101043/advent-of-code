import os
import string

def partone(input):
    
    input_split = input.split("\n")

    dict_items = {}

    for rectangle in input_split:

        index_at = rectangle.index("@")
        index_colon = rectangle.index(":")

        how_far = rectangle[index_at+2:index_colon]
        #print(rectangle, how_far)
        index_comma = how_far.index(",")
        from_left = int(how_far[:index_comma])
        from_top = int(how_far[index_comma+1:])

        width_height = rectangle[index_colon+2:]
        index_x = width_height.index("x")
        width = int(width_height[:index_x])
        height = int(width_height[index_x+1:])

        #print(rectangle, from_left, from_top, width, height)

        
        for i in range(from_left,from_left+width):
            for j in range(from_top,from_top+height):
                #print(i,j, (i, j) not in dict_items.keys())
                
                if (i, j) not in dict_items.keys():
                    dict_items[(i,j)] = 1
                else:
                    current = dict_items[(i,j)]
                    dict_items[(i,j)] = current + 1

                

        #print(size)

        #print(dict_items)

    total = 0
    for key, value in dict_items.items():
        #print(key, value)
        if value > 1:
            total += 1

    return total





print(os.getcwd())
with open("2018/day3/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
