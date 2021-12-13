def partOne(input_text):
    input_split = solution_in_list(input_text)
    bingo_num = input_split[0].split(",")
    bingo_cards = input_split[1:]
    bingo_called = []
    for num in bingo_num:
        bingo_called.append(int(num))
        for i, card in enumerate(bingo_cards):
            #print(card, bingo_called)
            done = check_bingo(card, bingo_called)
            #print("\n\n\n")
            if done:
                print(bingo_called)
                print(done)
                print(int(num))
                print(card)
                return done * int(num)



def check_bingo(card, nums):
    vertical = [0,1,2,3,4]
    horizontal = [0,1,2,3,4]
    
    total = 0
    for i, data in enumerate(card):
        #print(horizontal_split)
        for j, num in enumerate(data):

            #print(i, j, num)
            if num not in nums:
                total += num
                if j in vertical:
                    vertical.remove(j)
                if i in horizontal:
                    horizontal.remove(i)
            
            if vertical == [] and horizontal == []:
                return 0

    return total

def partTwo(input_text):
    input_split = solution_in_list(input_text)
    bingo_num = input_split[0].split(",")
    bingo_cards = input_split[1:]
    bingo_called = []
    for num in bingo_num:
        bingo_called.append(int(num))
        to_remove = []
        for i, card in enumerate(bingo_cards):
            #print(card, bingo_called)
            done = check_bingo(card, bingo_called)
            #print("\n\n\n")
            if done:
                if len(bingo_cards) == 1:
                    return done * int(num)
                else:
                    to_remove.append(i)
        
        for j, index in enumerate(to_remove):
            bingo_cards.pop(index - j)

def solution_in_list(inputText):
    input_split = inputText.split("\n\n")
    output = [input_split[0]]
    for card in input_split[1:]:
        rows = card.split("\n")
        final_card = []
        for row in rows:
            row_split = row.split(" ")
            final_row = [int(data) for data in row_split if data != ""]
            final_card.append(final_row)

        output.append(final_card)
    return output


with open("2021/day4/input.txt") as data:
    file_to_read = data.read()

# print(partOne(file_to_read))
print(partTwo(file_to_read))
