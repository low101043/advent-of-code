import csv
import os
from collections import Counter

def partone(input):
    input_split = input.split("\n")

    valid = 0
    for line in input_split:
        if passphraseValid(line):
            valid += 1

    return valid

def passphraseValid(passphrase):

    words = passphrase.split(" ")

    counter = Counter(words).most_common()

    return not counter[0][1] > 1
    
    



print(os.getcwd())
with open("2017/day4/input.txt") as data:
    file_to_read = data.read()

print(partone(file_to_read))
