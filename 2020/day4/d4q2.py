import csv
import os


def in_list(data, to_find):
    for key_value in data:
        if key_value[:3] == to_find:
            if (to_find == "byr"):
                
                numbers = key_value[4:]
                print("BYR", numbers)
                if (len(numbers) != 4):
                    return False
                if (int(numbers) >= 1920 and int(numbers) <= 2002):
                    #print("Here")
                    return True
                
                return False
            if (to_find == "iyr"):
                numbers = key_value[4:]
                print("IYR", numbers)
                if (len(numbers) != 4):
                    return False
                if (int(numbers) >= 2010 and int(numbers) <= 2020):
                    return True
                
                return False

            if (to_find == "eyr"):
                numbers = key_value[4:]
                print("EYR", numbers)
                if (len(numbers) != 4):
                    return False
                if (int(numbers) >= 2020 and int(numbers) <= 2030):
                    return True
                
                return False
            
            if (to_find == "hgt"):
                metric = key_value[-2] + key_value[-1]
                print("HGT", metric)
                if (metric == "cm"):
                    index = 4
                    number = ""
                    while (key_value[index] != "c"):
                        number += key_value[index]
                        index += 1
                    
                    print(number)
                    if (int(number) >= 150 and int(number) <= 193):
                        return True
                    else:
                        return False
                elif (metric == "in"):
                    index = 4
                    number = ""
                    while (key_value[index] != "i"):
                        number += key_value[index]
                        index += 1
                    print(number)
                    if (int(number) >= 59 and int(number) <= 76):
                        return True
                    else:
                        return False
                else:
                    return False
            
            if (to_find == "hcl"):
                print("HCL", key_value[4])
                if (key_value[4] != "#"):
                    return False
                else:
                    index = 5
                    while index < len(key_value):
                        print(key_value[index])
                        if (key_value[index] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]):
                            return False
                        index += 1
                    
                    return True
            
            if (to_find == "ecl"):
                print("ECL")
                if (len(key_value) > 7):
                    return False
                else:

                    eye_colour = key_value[4:7]
                    print(eye_colour)
                    if (eye_colour in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                        return True
                    else:
                        return False
            
            if (to_find == "pid"):
                pid = key_value[4:]
                print("PID", pid)
                if (len(pid) != 9):
                    return False
                else:
                    print(pid.isnumeric())
                    return (pid.isnumeric())
    return False

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/solutions/2020/day4")
with open("day4Input1.txt") as data:
    file_to_read = data.read()

number_to_add = []
numbers = []
to_add = ""

for letter in file_to_read:
    if (letter == " "):
        number_to_add.append(to_add)
        to_add = ""
    elif (letter == "\n"):
        number_to_add.append(to_add)
        to_add = ""
        numbers.append(number_to_add)
        number_to_add = []
    else:
        to_add += str(letter)

number_to_add.append(to_add)
numbers.append(number_to_add)
print(numbers)
print("\n\n")

final_input = []
previous = []
for data in numbers:
    #print(data)
    if (data == ['']):
        final_input.append(previous)
        previous = []
    else:
        for key_value in data:
            previous.append(key_value)

final_input.append(previous)
print(final_input)

valid = 0

for credentials in final_input:

    if (in_list(credentials, "byr") and in_list(credentials, "iyr") and in_list(credentials, "eyr") and in_list(credentials, "hgt") and in_list(credentials, "hcl") and in_list(credentials, "ecl") and in_list(credentials, "pid")):
        valid += 1
    print(in_list(credentials, "byr"), in_list(credentials, "iyr") , in_list(credentials, "eyr") , in_list(credentials, "hgt") , in_list(credentials, "hcl"), in_list(credentials, "ecl") ,in_list(credentials, "pid"))
    print("\n")

print(valid)
