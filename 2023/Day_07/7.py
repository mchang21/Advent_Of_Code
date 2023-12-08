PATH = '../Advent_Of_Code/2023/Day_07/'
import collections, functools

def parse_data(file):
    with open(file, 'r') as f:
       data = f.read().strip().split('\n')
       for i, d in enumerate(data):
           data[i] = d.split()
           data[i][1] = int(data[i][1])  
    return data

def get_hand_type(hand):
    counter = collections.Counter(hand)
    # five of a kind
    if len(counter) == 1:
        return 7
    # four of a kind or full house
    elif len(counter) == 2:
        # four of a kind
        if 1 in counter.values(): return 6
        # full house
        else: return 5
    # three of a kind or two pair
    elif len(counter) == 3:
        # three of a kind
        if 3 in counter.values(): return 4
        # two pair
        else: return 3
    # one pair
    elif len(counter) == 4: return 2
    # high card
    else: return 1

def compare_same_hand(hand1, hand2):
    card_strength = {card: i for i, card in enumerate('23456789TJQKA')}
    i, j = 0, 0
    while hand1[i] == hand2[j]:
        i, j = i+1, j+1
    if card_strength[hand1[i]] > card_strength[hand2[j]]: return 1
    elif card_strength[hand1[i]] < card_strength[hand2[j]]: return -1
    else: return 0

def compare_hands(hand1, hand2):
    hand1, hand2 = hand1[0], hand2[0]
    hand1_type, hand2_type = get_hand_type(hand1), get_hand_type(hand2)
    # hand 1 is stronger
    if hand1_type > hand2_type: return 1
    # hand 2 is stronger
    elif hand1_type < hand2_type: return -1
    # same hand type,
    else: return compare_same_hand(hand1, hand2)
    
def calculate_total_winnings(hands):
    sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hands))
    winnings = 0
    for i, (_, bid) in enumerate(sorted_hands, start=1):
        winnings += (bid*i)
    return winnings

hands = parse_data(PATH + "input.txt")
# part one
print(f"The total winnings earned is {calculate_total_winnings(hands)}.")
# The total winnings earned is 248559379.

# part two
def get_new_hand_type(hand):
    card_count = collections.Counter(hand)
    size = len(card_count)
    if len(card_count) > 1:
        # get number of jokers and remove it from counter
        jokers = card_count['J']
        card_count.pop('J')
        # get card with maximum count and increase it by # of jokers
        card = max(card_count, key=card_count.get)
        card_count[card] += jokers
        # create the new hand and get its new hand type
        new_hand = []
        for c, count in card_count.items():
            new_hand.append(c*count)
    return  get_hand_type(''.join(new_hand)) if size > 1 else get_hand_type(hand)

def compare_same_hand_part_2(hand1, hand2):
    card_strength = {card: i for i, card in enumerate('J23456789TQKA')} # 'J' is now the lowest ranking card
    i, j = 0, 0
    while hand1[i] == hand2[j]:
        i, j = i+1, j+1
    if card_strength[hand1[i]] > card_strength[hand2[j]]: return 1
    elif card_strength[hand1[i]] < card_strength[hand2[j]]: return -1
    else: return 0

def compare_hands_part_2(hand1, hand2):
    hand1, hand2 = hand1[0], hand2[0] # original hand
    hand1_type, hand2_type = get_hand_type(hand1), get_hand_type(hand2) # original hand type
    # new hand type if it contains a 'J'
    if 'J' in hand1:
        hand1_type = get_new_hand_type(hand1)
    if 'J' in hand2:
        hand2_type = get_new_hand_type(hand2)
    # hand 1 is stronger
    if hand1_type > hand2_type: return 1
    # hand 2 is stronger
    elif hand1_type < hand2_type: return -1
    # same hand type,
    else: return compare_same_hand_part_2(hand1, hand2)

def calc_new_total_winnings(hands):
    sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hands_part_2))
    winnings = 0
    for i, (_, bid) in enumerate(sorted_hands, start=1):
        winnings += (bid*i)
    return winnings

# part two
print(f"The new total winnings earned is {calc_new_total_winnings(hands)}.")
# The new total winnings earned is 249631254.