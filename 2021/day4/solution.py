def partOne(input_text):
    input_split = solution_in_list(input_text)
    bingo_num = input_split[0].split(",")
    bingo_cards = input_split[1:]
    bingo_called = []
    for num in bingo_num:
        bingo_called.append(int(num))
        for i, card in enumerate(bingo_cards):
            done = check_bingo(card, bingo_called)
            print("\n\n\n")
            if done:
                print(bingo_called)
                print(done)
                print(int(num))
                print(card)
                return done * int(num)



def check_bingo(card, nums):
    vertical = [0,1,2,3,4]
    horizontal = [0,1,2,3,4]
    card_in_list = card.split("\n")
    
    total = 0
    for i, horizontal_nums in enumerate(card_in_list):
        horizontal_split = horizontal_nums.split(" ")
        #print(horizontal_split)
        j = 0
        for num in horizontal_split:
            
            try:
                int_num = int(num)
            except:
                continue
            j += 1
            print(i, j, int_num)
            if int_num not in nums:
                total += int_num
                if j in vertical:
                    vertical.remove(j)
                if i in horizontal:
                    horizontal.remove(i)
            
            if vertical == [] or horizontal == []:
                return 0

    print(vertical, horizontal, total)
    total = 0
    for i, horizontal_nums in enumerate(card_in_list):
        horizontal_split = horizontal_nums.split(" ")
        #print(horizontal_split)
        for j, num in enumerate(horizontal_split):
            try:
                int_num = int(num)
            except:
                continue

            if int_num not in nums:
                total += int_num

    return total

def partTwo(input_text):
    pass

def solution_in_list(inputText):
    input_split = inputText.split("\n\n")
    return input_split


with open("2021/day4/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
print(partTwo(file_to_read))
