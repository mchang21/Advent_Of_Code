import os

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = [l.split('\n') for l in f.read().strip().split('\n\n')]
    return data

def transpose(matrix):
    return [''.join(row) for row in zip(*matrix)]

# returns the number of rows/cols before the line of reflection
def check_reflection(matrix):
    for i in range(len(matrix)-1):
        l, r = i, i+1
        # check for matching rows
        while l >= 0 and r < len(matrix) and matrix[l] == matrix[r]:
            l -= 1
            r += 1
        # if we get to the end, we found a line of reflection between i and i+1
        if l < 0 or r >= len(matrix):
            return i+1
    return 0

def summarize_notes(data, smudge=False):
    total = 0
    for matrix in data:
        if not smudge:
            total += check_reflection(transpose(matrix)) + (check_reflection(matrix)*100)
        else:
            total += check_reflection_with_smudge(transpose(matrix)) + (check_reflection_with_smudge(matrix)*100)
    return total

data = parse_data(file)
# part one
print(f"The number you get after summarizing all notes is {summarize_notes(data)}.")
# The number you get after summarizing all notes is 34918.

# part two
def check_reflection_with_smudge(matrix):
    for i in range(len(matrix)-1):
        smudge = False
        l, r = i, i+1
        while l >= 0 and r < len(matrix):
            # count number of differences between rows
            diff = sum(1 for a,b in zip(matrix[l], matrix[r]) if a!=b)
            # condition to break
            if diff >= 2 or (diff and smudge): break
            # fix smudge
            if diff == 1: smudge = True
            l -= 1
            r += 1
        # found a line of reflection after fixing smudge and reaching out of bounds
        if smudge and (l < 0 or r >= len(matrix)):
            return i+1
    return 0

print(f"The number you get after summarizing all smudged notes is {summarize_notes(data, True)}.")
# The number you get after summarizing all smudged notes is 33054.