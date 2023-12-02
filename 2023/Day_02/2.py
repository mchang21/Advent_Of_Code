PATH = '../Advent_Of_Code/2023/Day_02/'

RED = 'red'
GREEN = 'green'
BLUE = 'blue'

# part one
def parse_data(file):
    with open(file, 'r') as f:
        data = [line.strip() for line in f]
    return data

def clean_data(data):
    data = [d.split(':') for d in data]
    games = []
    # extract round data of each game
    for d in data:
        rounds = d[1].strip().split(';')
        for i, r in enumerate(rounds):
            # each round[i] contains [['int','color'...]... [...'int,'color']]
            rounds[i] = r.replace(',',' ').strip().split()
        games.append(rounds)
    return games

def sum_valid_ids(data):
    id_sum = 0
    # iterate over each game
    for i, game in enumerate(data):
        valid = True
        # iterate over each round
        for round in game:
            # get each cube count and cube color
            for j in range(0, len(round), 2):
                count, color = int(round[j]), round[j+1]
                # conditions to invalidate game
                if color == RED:
                    if count > 12: valid = False
                elif color == GREEN:
                    if count > 13: valid = False
                elif color == BLUE:
                    if count > 14: valid = False
        id_sum += (i+1) if valid else 0

    return id_sum
data = parse_data(PATH + 'input.txt')
data = clean_data(data)

# part one
print(f"The sum of valid game IDs are {sum_valid_ids(data)}.\n")

# part two
def sum_power_of_sets(data):
    powers = []
    # iterate over each game
    for i, game in enumerate(data):
        red, green, blue = 0, 0, 0
        # iterate over each round
        for round in game:
            # get each cube count and cube color
            for j in range(0, len(round), 2):
                count, color = int(round[j]), round[j+1]
                # get fewest num of cube of each color
                if color == RED:
                    red = max(red, count)
                elif color == GREEN:
                    green = max(green, count)
                elif color == BLUE:
                    blue = max(blue, count)
        powers.append(red*green*blue)
    return sum(powers)

# part two
print(f"The sum of power of sets are {sum_power_of_sets(data)}.\n")
