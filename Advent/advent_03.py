PATH = "C:/Users/melvi/Desktop/Advent2022/Input/"

def parse_data(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

data = parse_data(PATH + "input03.txt")
# strip newline character
for i in range(len(data)):
    data[i] = data[i].rstrip()

# part one
def find_common_item_sum(data):
    common_items = []
    priority_sum = 0

    # find the item that is in both compartments of the rucksack
    for d in data:
        duplicates = set()
        size = len(d)
        # iterate first half of the rucksack
        for i in range(size // 2):
            duplicates.add(d[i])
        # iterate second half of the rucksack, checking for duplicate item
        for i in range(size // 2, size):
            if d[i] in duplicates:
                common_items.append(d[i])
                break
    # calculate the sum of the priorities of the items
    for item in common_items:
        if item.isupper():
            priority_sum += (ord(item) - ord('A') + 27)
        else:
            priority_sum += (ord(item) - ord('a') + 1)

    return priority_sum

print(f"The sum of priorities of the item types that appear in both compartments is {find_common_item_sum(data)}")
# Output: The sum of priorities of the item types that appear in both compartments is 7785 

# part two
def find_group_item_sum(data):
    common_item_type = []
    priority_sum = 0

    # find the item type that corresponds to the badges of each three-Elf group.
    for i in range(0, len(data), 3):
        second_rucksack = set(data[i+1])
        third_rucksack = set(data[i+2])

        for item in data[i]:
            if item in second_rucksack and item in third_rucksack:
                common_item_type.append(item)
                break
    
    # calculate the sum of the priorities of the item types
    for item in common_item_type:
        if item.isupper():
            priority_sum += (ord(item) - ord('A') + 27)
        else:
            priority_sum += (ord(item) - ord('a') + 1)

    return priority_sum

print(f"The sum of the priorities of the item types corresponding to the badges of each three-Elf group is {find_group_item_sum(data)}")
# Output: The sum of the priorities of the item types corresponding to the badges of each three-Elf group is 2633
