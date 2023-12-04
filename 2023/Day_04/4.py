PATH = '../Advent_Of_Code/2023/Day_04/'

def parse_data(file):
    with open(file, 'r') as f:
        data = [line.strip().split(':') for line in f]
        for i, card in enumerate(data):
            winning, candidates = card[1].split('|')
            winning = set([int(num) for num in winning.split()])
            candidates = [int(num) for num in candidates.split()]
            data[i] = [winning, candidates]
    return data

def calc_card_score(cards):
    score = 0
    for card in cards:
        win, cand = card
        matches = len(set(cand).intersection(win))
        score += 2**(matches-1) if matches else 0
    return score

cards = parse_data(PATH + "input.txt")

# part one
print(f"All of the elf's scratchcards are worth {calc_card_score(cards)} points.")

def calc_total_cards(cards):
    scratchcards = {i:1 for i in range(len(cards))}
    for i, card in enumerate(cards):
        win, cand = card
        matches = len(set(cand).intersection(win))
        # add card count to each winning card
        for j in range(i+1, i+1+matches):
            scratchcards[j] += scratchcards[i]
    return sum(scratchcards.values())

# part two
print(f"The total amount of scratchcards the elf ends up with is {calc_total_cards(cards)} cards.")