import csv
import os

print(os.getcwd())
os.chdir("/home/low101043/Documents/adventOfCode/2020/day1")
with open("day1Input1.txt") as data:
    file_to_read = data.read()

number_to_add = ""
numbers = []

for letter in file_to_read:
    if (letter == "\n" and number_to_add != ""):
        number_as_int = int(number_to_add)
        numbers.append(number_as_int)
        number_to_add = ""
    else:
        number_to_add += letter

print(numbers)

found = False
number1 = numbers.pop()
number2 = -1
number3 = -1
while not found and len(numbers) > 1:
    j = 0
    while (j < len(numbers) and not found):
        number_to_try_2 = numbers[j]
        i = 0
        while (i < len(numbers) -1 and not found):
            number_to_try = numbers[i]
            if (number_to_try + number1 + number_to_try_2 == 2020):
                found = True
                number2 = number_to_try
                number3 = number_to_try_2
            i += 1
        j += 1
    if (not found):
        number1 = numbers.pop()

print(number1, number2, number3)


final_total = number1 * number2 * number3
print(final_total)