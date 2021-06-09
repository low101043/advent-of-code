import os
import hashlib

def partone(input):
    password = ["", "", "", "", "", "", "",""]
    finished = False
    i = 0
    while not finished:
        input_to_hash = input + str(i)
        result = hashlib.md5(input_to_hash.encode())
        hex_hash = result.hexdigest()

        if len(hex_hash) >= 7 and hex_hash[:5] == "00000":
            #print(hex_hash)
            
            place_str = hex_hash[5]
            if (place_str.isnumeric()):
                place = int(place_str)
                if (place <= 7 and place >= 0 and password[place] == ""):
                    password[place] = hex_hash[6]
                    finished = True
                    for letter in password:
                        if letter == "":
                            finished = False

        i += 1
    return password

    


print(os.getcwd())
with open("2016/day5/input.txt") as data:
    file_to_read = data.read()


print(partone(file_to_read))