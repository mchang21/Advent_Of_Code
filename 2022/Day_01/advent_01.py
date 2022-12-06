import heapq

def parse_data(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

file = "../Advent2022/2022/Day_01/input01.txt"
data = parse_data(file)

# part one
def find_calories(data):
    calories = []
    curr_calories = 0

    # count how many calories each elf is carrying
    for d in data:        
        d = d[:-1]
        if len(d) > 0:
            curr_calories += int(d)
        else:
            calories.append(curr_calories)
            curr_calories = 0

    return max(calories)
    
print(f"The total calories the top elf is carrying is: {find_calories(data)}")

# part two
def find_three_most_calories(data):
    calories = [] # max heap
    curr_calories, total_calories = 0, 0

    # count how many calories each elf is carrying and push to max heap
    for d in data:        
        d = d[:-1]
        if len(d) > 0:
            curr_calories += int(d)
        else:
            heapq.heappush(calories, -curr_calories)
            curr_calories = 0

    # pop 3 largest calories
    for _ in range(3):
        total_calories += -heapq.heappop(calories)

    return total_calories

print(f"The total calories the top three elves are carrying is: {find_three_most_calories(data)}")