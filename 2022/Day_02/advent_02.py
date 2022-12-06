PATH = '../Advent_Of_Code/2022/Day_02/'

def parse_data(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

data = parse_data(PATH + "input02.txt")

# part one
def calculate_score(data):
    win_conditions = {'A':'Z', 'B':'X', 'C':'Y', 'X':'C', 'Y':'A', 'Z':'B'}
    scores = {'X' : 1, 'Y' : 2, 'Z' : 3}
    total_score = 0

    for d in data:
        opp_choice, my_choice = d[:-1].split(' ')
        # Win condition
        if win_conditions[my_choice] == opp_choice:
            total_score += (6 + scores[my_choice])
        
        # Lose condition
        elif win_conditions[opp_choice] == my_choice:
            total_score += scores[my_choice]

        # Draw
        else:
            total_score += (3 + scores[my_choice])
    
    return total_score

print(f"The total score according to the strategy guide is {calculate_score(data)}")
# Output: The total score according to the strategy guide is 11063

# part two
def calculate_new_score(data):
    lose_conditions = {'A':'C', 'B':'A', 'C':'B'}
    win_conditions = {'A':'B', 'B':'C', 'C':'A'}
    scores = {'A' : 1, 'B' : 2, 'C' : 3}
    total_score = 0

    for d in data:
        opp_choice, condition = d[:-1].split(' ')
        # must lose
        if condition == 'X':
            total_score += scores[lose_conditions[opp_choice]]

        # must win
        elif condition == 'Z':
            total_score += (6 + scores[win_conditions[opp_choice]])

        # must draw
        else:
            total_score += (3 + scores[opp_choice])
    
    return total_score

print(f"The new total score according to the strategy guide is {calculate_new_score(data)}")
# Output: The new total score according to the strategy guide is 10349