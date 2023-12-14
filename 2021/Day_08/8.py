import os
from collections import defaultdict
file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
       data = [line.split('|') for line in f.read().strip().split('\n')]
    return data

def sort_data(line):
    res = []
    res.append([''.join(sorted(num)) for num in sorted(line[0].strip().split(), key=len)])
    res.append([''.join(sorted(num)) for num in line[1].strip().split()])
    return res

def map_numbers(digits):
    len_group = defaultdict(list)
    for word in digits:
        len_group[len(word)].append(word)

    # { sorted word: number (it maps to) }
    num_map = defaultdict(int)
    # hard code 1, 7, 4, 8
    num_map[len_group[2][0]] = 1
    num_map[len_group[3][0]] = 7
    num_map[len_group[4][0]] = 4
    num_map[len_group[7][0]] = 8

    # solve for 3
    for word in len_group[5]:
        # check set(1).intersect(set(3)) have len 2
        if len(set(list(len_group[2][0])).intersection(set(list(word)))) == 2:
            num_map[word] = 3
            len_group[5].remove(word)
            break
    # solve for 6
    for word in len_group[6]:
        # check set(1).intersect(set(3)) have len 2
        if len(set(list(len_group[2][0])).intersection(set(list(word)))) == 1:
            num_map[word] = 6
            len_group[6].remove(word)
            break
    # solve for 5 and 2
    for word in len_group[5]:
        six = ""
        for w in num_map:
            if num_map[w] == 6:
                six = w
        if len(set(list(six)).intersection(set(list(word)))) == 5:
            num_map[word] = 5
        else:
            num_map[word] = 2
    # solve for 0 and 9
    for word in len_group[6]:
        five = ""
        for w in num_map:
            if num_map[w] == 5:
                five = w
        if len(set(list(five)).intersection(set(list(word)))) == 5:
            num_map[word] = 9
        else:
            num_map[word] = 0

    return num_map

def sum_1_4_7_8(data):
    total = 0
    for line in data:
        digits, output = sort_data(line)
        num_map = map_numbers(digits)
        for num in output:
            total += 1 if num_map[num] in [1,4,7,8] else 0
    return total

data = parse_data(file)
# part 1
print(f"The amount of time 1,4,7,8 appear is {sum_1_4_7_8(data)}.")
# The amount of time 1,4,7,8 appear is 479.

# part two
def sum_output(data):
    total = 0
    for line in data:
        digits, output = sort_data(line)
        num_map, curr = map_numbers(digits), 0
        for num in output:
            curr = curr*10 + num_map[num]
        total += curr
    return total

print(f"The sum if you add up all the output values is {sum_output(data)}.")
# The sum if you add up all the output values is 1041746.