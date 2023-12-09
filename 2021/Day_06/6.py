PATH = '../Advent_Of_Code/2021/Day_06/'
from collections import Counter, deque

def parse_data(file):
    with open(file, 'r') as f:
        data = [int(age) for age in f.read().strip().split(',')]
    return data

def fish_after_n_days(ages, days):
    fish = deque([Counter(ages)[i] for i in range(9)]) # where `fish[i]` fish represent `i` days until they spawn a new fish
    for _ in range(days):
        new_fish = fish.popleft()  # pop left to simulate day decrement for all fish
        fish[6] += new_fish        # num fish which reset to 6 days
        fish.append(new_fish)      # num fish which get added to entire population
    return sum(fish)

ages = parse_data(PATH + "input.txt")
# part one
print(f"There would be {fish_after_n_days(ages, 80)} lantern fish after 80 days.")
# There would be 365131 lantern fish after 80 days.
# part two
print(f"There would be {fish_after_n_days(ages, 256)} lantern fish after 256 days.")
# There would be 1650309278600 lantern fish after 256 days.
