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


print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2016/day1")
with open("input.txt") as data:
    file_to_read = data.read()


print(partone(file_to_read))