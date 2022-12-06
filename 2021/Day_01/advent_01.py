PATH = '../Advent_Of_Code/2021/Day_01/'

def parse_data(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

data = parse_data(PATH + "input01.txt")
# convert data into int
cleaned = []
for d in data:
    cleaned.append(int(d[:-1]))
data = cleaned

# part one
def find_increasing(data):
    num_increasing = 0
    prev = data[0]
    # compare current depth to the previous depth
    for d in data[1:]:
        depth = d
        if depth > prev:
            num_increasing += 1
        prev = depth
    
    return num_increasing

print(f"There are {find_increasing(data)} measurements larger than the previous measurement")
# Output: There are 1711 measurements larger than the previous measurement

# part two
def find_increasing_window(data):
    num_increasing = 0
    prev_window = sum(data[:3])

    # compare current window sum to the previous window sum
    for i in range(3, len(data)):
        # increase sum by new depth, and subtract by old depth
        next_window = prev_window + data[i] - data[i-3]
        if next_window > prev_window:
            num_increasing += 1
        prev_window = next_window

    return num_increasing

print(f"There are {find_increasing_window(data)} sums larger than the previous sum")
