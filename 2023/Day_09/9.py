import os
file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
       data = f.read().strip().split('\n')

       for i, d in enumerate(data):
           data[i] = [int(num) for num in d.split()]
    return data

# helper to get all differences for each step of a given history
def get_differences(history):
    curr = [num for num in history]
    differences = [curr]
    while not all([num == 0 for num in curr]):
        diff = [curr[i] - curr[i-1] for i in range(1, len(curr))]
        curr = diff
        differences.append(diff)
    return differences

def extrapolate(differences, part1=False):
    if part1:
        # only care about the last digit
        extrapolated_value = sum([difference[-1] for difference in differences[::-1]])
    else:
        # part two
        difference = [difference[0] for difference in differences[::-1]]
        extrapolated_value = 0
        for num in difference:
            extrapolated_value = num - extrapolated_value
    return extrapolated_value

def sum_extrapolated(data, part1=False):
    total = 0
    for history in data:
        differences = get_differences(history)
        total += extrapolate(differences, part1)
    return total

data = parse_data(file)

# part one
print(f"The sum of extrapolated values is {sum_extrapolated(data, True)}.")
# The sum of extrapolated values is 1743490457.

# part two
print(f"The sum of extrapolated values is {sum_extrapolated(data)}.")
# The sum of extrapolated values is 1053.