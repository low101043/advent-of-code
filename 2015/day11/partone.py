import csv
import os
import itertools

# Have to implement Branch and Bound as TSP.  Thanks Wikipedia

def partone(input):
    password = nextPassword(input)
    while not checks(password):
        
        password = nextPassword(password)
        #print(password)
    return password


def nextPassword(oldPassword):
    last_letter = oldPassword[-1]
    completed = False
    newPassword = ""
    i = -1
    past_letter = ""
    while not completed:
        next_letter = ord(last_letter) + 1
        if next_letter != 123:
            newPassword = oldPassword[:len(oldPassword) + i] + chr(next_letter) + past_letter
            completed = True
        else:
            past_letter += "a"
            if (i*-1 == len(oldPassword)):
                return "a" * len(oldPassword) + 1
            else:
                i -= 1
                last_letter = oldPassword[i]
    
    return newPassword

def checks(password):

    same_letter_once = False
    same_letter_twice = False
    ascending = False
    for i in range(len(password)):
        letter = password[i]
        if letter in ['i', 'l', 'o']:
            return False
        
        if i + 1 < len(password):
            if i -1 < 0:
                if letter == password [i+1] and letter != password[i+2]:
                    same_letter_once = True
            
            if i + 2 < len(password):
                if letter == password [i+1] and letter != password[i+2] and letter != password[i-1]:
                    if (same_letter_once):
                        same_letter_twice = True
                    else:
                        same_letter_once = True

            else:
                if letter == password [i+1] and letter != password[i-1]:
                    if (same_letter_once):
                        same_letter_twice = True
                    else:
                        same_letter_once = True

        if i + 2 < len(password):
            if ord(letter) == ord(password[i + 1]) -1 and ord(password[i+1]) == ord(password[i+2]) -1:
                ascending = True

    return same_letter_once and same_letter_twice and ascending


print(os.getcwd())
with open("2015/day11/input.txt") as data:
    file_to_read = data.read()


print(partone("hepxxyzz"))
