def partOne(input_text):
    template, insertion_rules = solution_in_list(input_text)
    print(template)
    print(insertion_rules)

    for i in range(10):
        new_template = ""
        for i in range(len(template) - 1):
            to_check = template[i:i+2]
            if to_check in insertion_rules.keys():
                new_template = new_template + to_check[0] + insertion_rules[to_check] 
            else:
                new_template += to_check[0]
        new_template += to_check[1]

        template = new_template
        #print(template)

    #print(template)

    return final_total(template)
    
def final_total(template):
    num = {}

    for letter in template:
        if letter not in num.keys():
            num[letter] = 1
        else:
            num[letter] = num[letter] + 1

    max_num = max(num.values())
    min_num = min(num.values())

    print(max_num)
    print(min_num)

    return max_num - min_num

def partTwo(input_text):
    template, insertion_rules = solution_in_list(input_text)
    print(template)
    print(insertion_rules)

    for i in range(40):
        print(i)
        new_template = ""
        for i in range(len(template) - 1):
            to_check = template[i:i+2]
            if to_check in insertion_rules.keys():
                new_template = new_template + to_check[0] + insertion_rules[to_check] 
            else:
                new_template += to_check[0]
        new_template += to_check[1]

        template = new_template
        #print(template)

    #print(template)

    return final_total(template)


def solution_in_list(inputText):
    split = inputText.split("\n")

    insertion_rules = {}

    for rule in split[2:]:
        two_halves = rule.split(" -> ")
        insertion_rules[two_halves[0]] = two_halves[1]
    return split[0], insertion_rules
            


with open("2021/day14/input.txt") as data:
    file_to_read = data.read()

print(partOne(file_to_read))
print(partTwo(file_to_read))