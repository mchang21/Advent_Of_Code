import os, re
from collections import defaultdict

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().strip().split('\n\n')
    return data

def get_workflows(workflows):
    parts = {'x':0,'m':1,'a':2,'s':3}
    wf = defaultdict(list)
    for w in workflows.strip().split('\n'):
        workflow, rules = w[:-1].split('{')
        for rule in rules.split(','):
            op = '>' if '>' in rule else '<'
            if len(rule.split(op)) == 2:
                part, val_and_next = rule.split(op)
                val_and_next = val_and_next.split(':')
                value, next_workflow = int(val_and_next[0]), val_and_next[1]
                wf[workflow].append([parts[part], op, value, next_workflow])
            else:
                wf[workflow].append([rule])
    return wf

def get_ratings(ratings):
    r = ratings.split('\n')
    for i in range(len(r)):
        r[i] = list(map(int, re.findall(r'\d+', r[i])))
    return r

def get_rating_for_accepted(workflows, ratings):
    rating_for_accepted = 0
    for rating in ratings:
        curr = 'in'
        # continue until accepted or rejected
        while (curr != 'A' and curr != 'R'):
            rules = workflows[curr]
            # iterate over each rule for the current workflow
            for rule in rules:
                if len(rule) > 1:
                    part, op, val, next_workflow = rule
                    # check if part meets workflow condition
                    accepted = rating[part] > val if op == '>' else rating[part] < val
                    if accepted:
                        curr = next_workflow
                        break
                # none of the workflow conditions were met
                else:
                    curr = rule[0]
        # part was accepted, add sum of parts to total
        if curr == 'A':
            rating_for_accepted += sum(rating)
    return rating_for_accepted

data = parse_data(file)
workflows, ratings = get_workflows(data[0]), get_ratings(data[1])

# part one
print(f"The sum of accepted rating numbers is {get_rating_for_accepted(workflows,ratings)}.")
# The sum of accepted rating numbers is 476889.

# part two
def calc_range(ranges, part, op, val):
    new_range = [r[:] for r in ranges] # create deep copy
    if op == '>':
        # lower bound
        new_range[part][0] = max(new_range[part][0], val+1)
    elif op == '<':
        # upper bound
        new_range[part][1] = min(new_range[part][1], val-1)
    return new_range

def calc_product(ranges):
    prod = 1
    for part in ranges:
        prod *= (part[1] - part[0] + 1)
    return prod

def calc_combinations(workflows, ranges, curr):
    # reached acceptable workflow
    if curr == 'A':
        return calc_product(ranges)
    elif curr == 'R':
        return 0
    
    res = 0
    for rule in workflows[curr]:
        if len(rule) == 1:
            res += calc_combinations(workflows, ranges, rule[0])
        else:
            part, op, val, next_workflow = rule
            # want to calc the range of numbers for which the rule will be true
            new_range = calc_range(ranges, part, op, val)
            res += calc_combinations(workflows, new_range, next_workflow)
            # continue as if the rule failed, make update to range
            if op == '>':
                ranges[part][1] = val
            else:
                ranges[part][0] = val
    return res

# part two
ranges = [[1,4000], [1,4000], [1,4000], [1,4000]]
print(f"The number of distinct combinations of ratings that will be accepted by the Elves' workflows is {calc_combinations(workflows, ranges, 'in')}.")
# The number of distinct combinations of ratings that will be accepted by the Elves' workflows is 132380153677887.