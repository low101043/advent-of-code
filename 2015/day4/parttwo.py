import csv
import os
import hashlib

def parttwo(input):
    for i in range(0, 100000000000):

        result = hashlib.md5((input + str(i)).encode()).hexdigest()
        if len(result) > 6 and result[0:6] == "000000":
            return i
        

print(os.getcwd())
with open("2015/day4/input.txt") as data:
    file_to_read = data.read()
print(file_to_read)
print(parttwo(file_to_read))