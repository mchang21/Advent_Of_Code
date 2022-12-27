from collections import deque

PATH = '../Advent_Of_Code/2022/Day_11/'

def parse_monkeys(file):
    monkeys = []
    with open(file) as f:
        monkey = Monkey()
        for line in f:
            if line == '\n':
                continue
            attribute, data = line.strip().split(':')
            if attribute == "Starting items":
                monkey.set_items(data)
            elif attribute == "Operation":
                monkey.set_operator(data)
                monkey.set_factor(data)
            elif attribute == "Test":
                monkey.set_divisible_by(data)
            elif attribute == "If true":
                monkey.set_throw_to_true(data)
            elif attribute == "If false":
                monkey.set_throw_to_false(data)
            else:
                if monkey.items:
                    monkeys.append(monkey)
                    monkey = Monkey()
        # append the last monkey
        monkeys.append(monkey)
    return monkeys

class Monkey:
    def __init__(self):
        self.items = deque()
        self.operator = None
        self.factor = None
        self.divisor = None
        self.throw_to_true = None
        self.throw_to_false = None
        self.inspections = 0

    def set_items(self, data):
        data = data.strip().split(', ')
        for item in data:
            self.items.append(int(item))
        return

    def set_operator(self, data):
        data = data.strip().split()
        self.operator = data[3]
        return
    
    def set_factor(self, data):
        data = data.strip().split()
        self.factor = data[4]
        return

    def set_divisible_by(self, data):
        data = data.strip().split()
        self.divisor = int(data[-1])
        return
    
    def set_throw_to_true(self, data):
        data = data.strip().split()
        self.throw_to_true = int(data[-1])
        return

    def set_throw_to_false(self, data):
        data = data.strip().split()
        self.throw_to_false = int(data[-1])
        return

    def calculate_worry_level(self, item):
        if self.operator == "*":
            if self.factor == "old":
                return item * item
            return item * int(self.factor)
        elif self.operator == "+":
            if self.factor == "old":
                return item + item
            return item + int(self.factor)
    
    def inspect_items(self, monkeys, part_one=True):
        self.inspections += len(self.items)
        # calculate common divisor to mod worry level by
        mod = 1
        for monkey in monkeys:
            mod *= monkey.divisor

        # simulate throwing
        while self.items:
            item = self.items.popleft()
            # calculate new worry level
            if part_one:
                new_item = self.calculate_worry_level(item) // 3
            else:
                new_item = self.calculate_worry_level(item) % mod
            # throw to the new monkey
            if new_item % self.divisor == 0:
                self.throw_to(monkeys[self.throw_to_true], new_item)
            else:
                self.throw_to(monkeys[self.throw_to_false], new_item)
        return

    def throw_to(self, monkey, item):
        monkey.items.append(item)
        return

monkeys = parse_monkeys(PATH + 'input.txt')
# monkeys = parse_monkeys(PATH + 'example.txt')

# part one
# simulate monkey business
round = 0
while round < 20:
    # simulate item throwing
    for i in range(len(monkeys)):
        if monkeys[i].items:
            monkeys[i].inspect_items(monkeys, True)
    round += 1
# calculate monkey business
inspections = []
for monkey in monkeys:
    inspections.append(monkey.inspections)
inspections.sort()
print(f"The level of monkey business after 20 rounds is {inspections[-1] * inspections[-2]}")

# part two
# simulate monkey business
monkeys = parse_monkeys(PATH + 'input.txt')
round = 0
while round < 10000:
    # simulate item throwing
    for i in range(len(monkeys)):
        if monkeys[i].items:
            monkeys[i].inspect_items(monkeys, False)
    round += 1
# calculate monkey business
inspections = []
for monkey in monkeys:
    inspections.append(monkey.inspections)
inspections.sort()
print(f"The level of monkey business after 10000 rounds is {inspections[-1] * inspections[-2]}")