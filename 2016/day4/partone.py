import os

def partone(input):

    input_split = input.split("\n")
    total = 0
    for line in input_split:
        print(line)
        room_name = line[:line.rfind("-")]
        checksum_created = checksum(room_name)
        checksum_used = line[line.find("[")+1:len(line)-1]
        print(checksum_used)
        if checksum_created == checksum_used:
            str_room_num = line[line.rfind("-") +1: line.find("[")]
            total += int(str_room_num)

    return total


def checksum(encrypted_name):
    print(encrypted_name)
    numbers = {}
    for letter in encrypted_name:
        if letter in numbers.keys():
            old_num = numbers[letter]
            old_num += 1
            numbers[letter] = old_num
        elif letter != "-":
            numbers[letter] = 1

    #print(numbers)
    keys = list(numbers.keys())
    values = list(numbers.values())

    values_ordered, keys_ordered = bubble(values, keys)
    #print(keys_ordered, values_ordered)
    checksum = ""

    j = 0
    i = 0
    while i < 5:
        
        
        if values_ordered[j] != values_ordered[j+1]:
            checksum += keys_ordered[j]
            
        else:
            k = j
            while k+1 < len(values_ordered) and  values_ordered[k] == values_ordered[k+1]:
                k += 1
            
            sub_list = keys_ordered[j:k+1]
            sub_list.sort()
            #print(sub_list)
            for checksum_letter in sub_list:
                checksum += checksum_letter
            j = k   
        #print(checksum)
        if (len(checksum) >= 5):
            i = 30
        j += 1
        i+= 1
    return checksum[:5]

def bubble(alist, b_list):
    
    passnum = len(alist) -1
    for outerLoop in range(passnum):    #Checks where you are in the list
        
        for innerLoop in range(passnum):    #does each comparison
            
            if alist[innerLoop] < alist[innerLoop+1]:   #comparing
                temp = alist[innerLoop]         #swap
                temp_b = b_list[innerLoop]
                alist[innerLoop]= alist[innerLoop+1]    #swap
                b_list[innerLoop] = b_list[innerLoop+1]
                alist[innerLoop + 1] = temp     #swap
                b_list[innerLoop+1] = temp_b
            
            
        
        
    return alist, b_list


print(os.getcwd())
with open("2016/day4/input.txt") as data:
    file_to_read = data.read()


print(partone(file_to_read))