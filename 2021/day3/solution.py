
from os import fwalk


def partOne(input_text):
    input_in_list = solution_in_list(input_text)
    gamma = ''
    epislon = ''

    for i in range(len(input_in_list[0])):
        num_of_ones = 0
        num_of_zeros = 0

        for binary in input_in_list:
            if binary[i] == '1':
                num_of_ones += 1
            else:
                num_of_zeros += 1

        if num_of_ones > num_of_zeros:
            gamma += '1'
            epislon += '0'
        else:
            gamma += '0'
            epislon += '1'

    gamma_dec = convert_from_bin(gamma)
    epislon_dec = convert_from_bin(epislon)

    return gamma_dec * epislon_dec

    
def partTwo(input_text):
    input_in_list_o2 = solution_in_list(input_text)    
    input_in_list_co2 = solution_in_list(input_text)

    i = 0
    while len(input_in_list_o2) > 1:
        num_to_keep = bit_criteria(input_in_list_o2, True, i)
        input_in_list_o2 = [binary for binary in input_in_list_o2 if binary[i] == num_to_keep]
        i += 1

    i = 0
    while len(input_in_list_co2) > 1:
        num_to_keep = bit_criteria(input_in_list_co2, False, i)
        input_in_list_co2 = [binary for binary in input_in_list_co2 if binary[i] == num_to_keep]
        i += 1
    print(input_in_list_o2)
    print(input_in_list_co2)

    o2 = convert_from_bin(input_in_list_o2[0])
    co2 = convert_from_bin(input_in_list_co2[0])

    return o2 * co2


def convert_from_bin(binary):
    flipped = binary[::-1]
    total = 0
    for i, num in enumerate(flipped):
        total += int(num) * (2**i)

    return total

def solution_in_list(inputText):
    input_split = inputText.split("\n")
    return input_split

def bit_criteria(input_binary, most_common, i):
    num_of_ones = 0
    num_of_zeros = 0

    for binary in input_binary:
        if binary[i] == '1':
            num_of_ones += 1
        else:
            num_of_zeros += 1

    if most_common:
        if num_of_ones >= num_of_zeros:
            return '1'
        else:
            return '0'
    else:
        if num_of_ones >= num_of_zeros:
            return '0'
        else:
            return '1'

with open("2021/day3/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
print(partTwo(file_to_read))
