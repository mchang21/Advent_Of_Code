PATH = '../Advent_Of_Code/2021/Day_07/'

def parse_data(file):
    with open(file, 'r') as f:
        data = [int(pos) for pos in f.read().strip().split(',')]
    return data

def calc_fuel_cost(data, pos, part2=False):
    return sum([abs(crab_pos-pos) if not part2 else ((abs(crab_pos-pos))*(abs(crab_pos-pos)+1)) // 2 for crab_pos in data])

def min_fuel_required(data, part2=False):
    # part one
    if not part2:
        data.sort()
        # use the median
        return calc_fuel_cost(data, data[len(data)//2])
    # part two
    else:
        min_cost = float('inf')
        for i in range(min(data), max(data)+1):
            cost = calc_fuel_cost(data, i, part2)
            min_cost = min(min_cost, cost)
        return min_cost


data = parse_data(PATH + "input.txt")
# part one
print(f"The minimum amount of fuel required to align the crabs is {min_fuel_required(data)}.")
# The minimum amount of fuel required to align the crabs is 348664.

# part two
print(f"The minimum amount of fuel required to align the crabs is {min_fuel_required(data, True)}.")
# The minimum amount of fuel required to align the crabs is 100220525.

