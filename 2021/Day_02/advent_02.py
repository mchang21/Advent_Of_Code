PATH = '../Advent_Of_Code/2021/Day_02/'

def parse_data(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

data = parse_data(PATH + "input02.txt")
# remove newline character
for i in range(len(data)):
    data[i] = data[i].rstrip()

# part one
def calculate_position_and_depth(data):
    horizontal_position = 0
    depth = 0
    for d in data:
        direction, units = d.split(" ")
        units = int(units)
        if direction == "forward":
            horizontal_position += units
        elif direction == "down":
            depth += units
        else:
            depth -= units
    
    return horizontal_position * depth

print(f"The product of the final horizontal position and final depth is {calculate_position_and_depth(data)}")
# Output: The product of the final horizontal position and final depth is 2019945

# part two
def calculate_position_and_depth_and_aim(data):
    horizontal_position = 0
    depth = 0
    aim = 0

    for d in data:
        direction, units = d.split(" ")
        units = int(units)
        if direction == "forward":
            horizontal_position += units
            depth += (aim * units)
        elif direction == "down":
            aim += units
        else:
            aim -= units
    
    return horizontal_position * depth

print(f"The product of the final horizontal position and final depth is {calculate_position_and_depth_and_aim(data)}")
# Output: The product of the final horizontal position and final depth is 1599311480