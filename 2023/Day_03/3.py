PATH = '../Advent_Of_Code/2023/Day_03/'

from collections import defaultdict

# part one
def parse_data(file):
    with open(file, 'r') as f:
        data = [list(line.strip()) + ['.'] for line in f]
    return data

# helper function to check if current number is neighboring a symbol
def check_neighbors(grid, i, j):
    m, n = len(grid), len(grid[0])
    # check each direction
    for x,y in [[i-1,j-1], [i-1,j], [i-1,j+1], [i,j-1], [i,j+1], [i+1,j-1], [i+1,j], [i+1,j+1]]:
        if 0 <= x < m and 0 <= y < n:
            if grid[x][y] != '.' and not grid[x][y].isdigit():
                return True
    return False

# iterate over the graph
# while iterating, parse digits
# while parsing each digit, check neighbors for symbol
# if there is a symbol and at end of parsing digit, add sum to res
# reset symbol flag
def calc_parts_sum(grid):
    m, n = len(grid), len(grid[0])
    parts_sum = 0
    curr_num, neighboring_symbol = 0, False
    for i in range(m):
        for j in range(n):
            # at digit
            if grid[i][j].isdigit():
                # parse digit
                curr_num = curr_num*10 + int(grid[i][j])
                # check if current number is neighboring a symbol
                if not neighboring_symbol:
                    neighboring_symbol = check_neighbors(grid, i, j)
            # not at digit
            else:
                # if we have a number and are no longer parsing digits
                if curr_num:
                    # current number is neighboring a symbol, add current number to answer
                    if neighboring_symbol:
                        parts_sum += curr_num
                    # otherwise it is not a valid number
                    curr_num = 0
                    neighboring_symbol = False
    return parts_sum

# part one
grid = parse_data(PATH + 'input.txt')
print(f"The sum of all of the part numbers in the engine schematic is {calc_parts_sum(grid)}.")

# part two
# helper to get gear index
def check_gears(grid, gear, i, j):
    m, n = len(grid), len(grid[0])
    # check each direction
    for x,y in [[i-1,j-1], [i-1,j], [i-1,j+1], [i,j-1], [i,j+1], [i+1,j-1], [i+1,j], [i+1,j+1]]:
        if 0 <= x < m and 0 <= y < n:
            if grid[x][y] != '.' and not grid[x][y].isdigit():
                if grid[x][y] == '*':
                    return (x,y)
    return False

def calc_gear_ratio_sum(grid):
    m, n = len(grid), len(grid[0])
    gear_ratio_sum = 0
    gears = defaultdict(list)
    curr_num, gear = 0, False
    for i in range(m):
        for j in range(n):
            # at digit
            if grid[i][j].isdigit():
                # parse digit
                curr_num = curr_num*10 + int(grid[i][j])
                # check if current number is neighboring a gear
                if not gear:
                    gear = check_gears(grid, gear, i, j)
            # not at digit
            else:
                # if we have a number and are no longer parsing digits
                if curr_num:
                    # current number is neighboring a gear, add current number to list of num adjacent to gear
                    if gear:
                        gears[gear].append(curr_num)
                        if len(gears[gear]) == 2:
                            gear_ratio_sum += (gears[gear][0] * curr_num)
                    # reset values
                    curr_num = 0
                    gear = False
    return gear_ratio_sum

# part two
print(f"The sum of all of the part numbers in the engine schematic is {calc_gear_ratio_sum(grid)}.")
