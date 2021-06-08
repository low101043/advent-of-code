import os

def partone(input):
    input_split = input.split(", ")
    print(len(input_split))
    print(input_split)
    
    angle = 0
    xLeft = 0
    yUp = 0
    xRight = 0
    yDown = 0

    for instruction in input_split:
        turn = instruction[0]
        if turn == "R":
            angle = (angle + 90) % 360
        else:
            print(turn)
            angle = ((angle - 90) + 360) % 360

        distance = int(instruction[1:])
        print(angle)
        if angle == 0:
            yUp += distance
        elif angle == 90:
            xRight += distance
        elif angle == 180:
            yDown += distance
        else:
            print("Here")
            xLeft += distance
        


    print(xRight, xLeft, yDown, yUp)
    print(xRight - xLeft)
    print(yUp - yDown)
    print("\n")
    return abs(abs(xRight-xLeft) + abs(yUp - yDown))


def parttwo(input):
    input_split = input.split(", ")
    #print(len(input_split))
    print(input_split)
    
    angle = 0
    xLeft = 0
    yUp = 0
    xRight = 0
    yDown = 0
    visited = []
    found = False
    j = 0

    while not found:
        instruction = input_split[j]
        print(j, instruction)
        turn = instruction[0]
        if turn == "R":
            angle = (angle + 90) % 360
        else:
            #print(turn)
            angle = ((angle - 90) + 360) % 360

        distance = int(instruction[1:])
        #print(angle)
        print(distance)
        if angle == 0:
            for i in range(distance):
                
                yUp += 1
                print(((xRight-xLeft),(yUp-yDown)))
                if ((xRight-xLeft),(yUp-yDown)) in visited:
                    found = True
                    print(((xRight-xLeft),(yUp-yDown)))
                    return (abs(xRight-xLeft) + abs(yUp - yDown))
                else:
                    visited.append(((xRight-xLeft),(yUp-yDown)))

        elif angle == 90:
            for i in range(distance):
                xRight += 1
                print(((xRight-xLeft),(yUp-yDown)))
                if ((xRight-xLeft),(yUp-yDown)) in visited:
                    found = True
                    print(((xRight-xLeft),(yUp-yDown)))
                    return (abs(xRight-xLeft) + abs(yUp - yDown))
                else:
                    visited.append(((xRight-xLeft),(yUp-yDown)))
        elif angle == 180:
            for i in range(distance):
                yDown += 1
                print(((xRight-xLeft),(yUp-yDown)))
                if ((xRight-xLeft),(yUp-yDown)) in visited:
                    found = True
                    print(((xRight-xLeft),(yUp-yDown)))
                    return (abs(xRight-xLeft) + abs(yUp - yDown))
                else:
                    visited.append(((xRight-xLeft),(yUp-yDown)))
        else:
            for i in range(distance):
                xLeft += 1
                print(((xRight-xLeft),(yUp-yDown)))
                if ((xRight-xLeft),(yUp-yDown)) in visited:
                    found = True
                    print(((xRight-xLeft),(yUp-yDown)))
                    return (abs(xRight-xLeft) + abs(yUp - yDown))
                else:
                    visited.append(((xRight-xLeft),(yUp-yDown)))
        

        print(visited)
        print("\n")

        j = (j + 1) % len(input_split)


    
    print(xRight - xLeft)
    print(yUp - yDown)
    print("\n")
    print("ENDS")


print(os.getcwd())
with open("2016/day3/input.txt") as data:
    file_to_read = data.read()


#print(partone(file_to_read))
print(parttwo(file_to_read))