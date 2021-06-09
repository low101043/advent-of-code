import os
import hashlib

def partone(input):
    password = ""
    i = 0
    while (len(password) != 8):
        input_to_hash = input + str(i)
        result = hashlib.md5(input_to_hash.encode())
        hex_hash = result.hexdigest()

        if len(hex_hash) >= 6 and hex_hash[:5] == "00000":
            password += hex_hash[5]

        i += 1
    return password

    


print(os.getcwd())
with open("2016/day5/input.txt") as data:
    file_to_read = data.read()


print(partone(file_to_read))