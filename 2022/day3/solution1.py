from collections import Counter


def partOne(input):
    input_format = input_split(input)

    total = 0

    for rucksack in input_format:
        length = len(rucksack)
        compartment_one = list(set(rucksack[:int(length/2)]))
        compartment_two = list(set(rucksack[int(length/2):]))

        counted = Counter(compartment_one+compartment_two)
        #print(counted)
        for letter, num in counted.items():
            if num == 2:
                shared = letter
       
       # print(shared)
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

print(partOne(file_to_read))
