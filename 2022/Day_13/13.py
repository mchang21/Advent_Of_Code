PATH = '../Advent_Of_Code/2022/Day_13/'

from ast import literal_eval
import functools

def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().split("\n\n")
        for i, d in enumerate(data):
            packets = d.split('\n')
            data[i] = [literal_eval(packets[0]), literal_eval(packets[1])]
    return data

def compare_int(l, r):
    if l < r: return 1
    elif l > r: return -1
    else: return 0

def compare_packets(left, right):
    match left, right:
        # base case
        case int(), int():
            return compare_int(left, right)
        # recurse on lists
        case int(), list():
            return compare_packets([left], right)
        case list(), int():
            return compare_packets(left, [right])
        case list(), list():
            # compare each num/list in the lists
            for l, r in zip(left,right):
                res = compare_packets(l, r)
                # return when end is met
                if res != 0:
                    return res
            return compare_packets(len(left), len(right))

def calc_idx_sum(data):
    sum_idx = 0
    for i, pair in enumerate(data):
        # returns 1 if the pair is in the right order
        if compare_packets(pair[0], pair[1]) == 1:
            sum_idx += (i+1)
    return sum_idx

data = parse_data(PATH + "input.txt")

# part one
print(f"The sum of indices for pairs which are in order is {calc_idx_sum(data)}.")

# part two
def calculate_decoder_key(data):
    packets = []
    for pair in data:
        packets.append(pair[0])
        packets.append(pair[1])
    packets += [[2]], [[6]]
    packets_sorted = sorted(packets, key=functools.cmp_to_key(compare_packets), reverse=True)
    return (1 + packets_sorted.index([[2]])) * (1 + packets_sorted.index([[6]]))
# part two
print(f"The decoder key for the distress signal is {calculate_decoder_key(data)}.")