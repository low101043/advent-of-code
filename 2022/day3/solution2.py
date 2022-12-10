from collections import Counter


def parttwo(input):
    input_format = input_split(input)

    total = 0

    for rucksack_ints in range(3, len(input_format)+3, 3):

        rucksack_one = list(set(input_format[rucksack_ints-3]))
        rucksack_two = list(set(input_format[rucksack_ints-2]))
        rucksack_three = list(set(input_format[rucksack_ints-1]))

        #print(rucksack_one)
        #print(rucksack_two)
        #print(rucksack_three)
        
        counted = Counter(rucksack_one+rucksack_two+rucksack_three)
        #print(counted)
        for letter, num in counted.items():
            if num == 3:
                shared = letter
       
        #print(shared)
        if shared.isupper():
            ascii = ord(shared)
            total += (ascii-64+26)
        #    print((ascii-64))
        else:
            ascii = ord(shared)
            total += (ascii-96)
         #   print((ascii-96))

    return total
        
    

def input_split(input):
    split_input = input.split("\n")

    return split_input


with open("2022/day3/input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))
