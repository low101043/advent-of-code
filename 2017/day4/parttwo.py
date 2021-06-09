import csv
import os
from collections import Counter

def parttwo(input):
    input_split = input.split("\n")

    valid = 0
    for line in input_split:
        if passphraseValid(line):
            valid += 1

    return valid

def passphraseValid(passphrase):

    words = passphrase.split(" ")
    print(words)

    for i in range(len(words)):
        word = words[i]
        letter_count = Counter(word).most_common()

        
        for j in range(len(words)):
            if (i == j):
                pass
            else:
                word_check = words[j]
                letter_count_check = Counter(word_check).most_common()
                
                letter_count.sort(key =lambda x: x[0])
                letter_count_check.sort(key =lambda x:x[0])
                #print(letter_count, letter_count_check, word, word_check)
                if letter_count_check == letter_count:
                    return False


    return True

    
    
    



print(os.getcwd())
with open("2017/day4/input.txt") as data:
    file_to_read = data.read()

print(parttwo(file_to_read))
