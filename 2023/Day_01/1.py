PATH = '../Advent_Of_Code/2023/Day_01/'
# part one
def parse_data(file):
    with open(file, 'r') as f:
        data = [line for line in f.read().strip().split()]
    return data

def get_sum(data):
    total = 0
    for line in data:
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(int(c))
        total += digits[0]*10 + digits[-1]
    return total

# part one answer
data = parse_data(PATH+"/input.txt")
print(f"The sum of the calibration values are {get_sum(data)}.\n")

# part two
def get_sum2(data):
    total = 0
    for line in data:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(int(c))
            for j, num in enumerate(["one","two","three","four","five","six","seven","eight","nine"]):
                if line[i:].startswith(num):
                    digits.append(j+1)
                    break
        total += digits[0]*10 + digits[-1]
    return total

# part two answer
print(f"The sum of the calibration values are {get_sum2(data)}.")