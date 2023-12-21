import os
from collections import deque
from math import lcm

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    graph, ff, cj, modules = {}, {}, {}, []
    with open(file, 'r') as f:
        for line in f:
            name, dest = line.strip().split(' -> ')
            dest = dest.split(', ')
            modules.append((name,dest))

        for name, dest in modules:
            if name.startswith('%'):
                ff[name[1:]] = False    # False if low pulse, True if high pulse
                graph[name[1:]] = dest
            elif name.startswith('&'):
                cj[name[1:]] = {}       # {input: most recent pulse}
                graph[name[1:]] = dest
            else:
                graph[name] = dest
                
        # initialize conjunction inputs
        for cj_name, state in cj.items():
            for name, dest in modules:
                if cj_name in dest:
                    state[name[1:]] = False
    return graph, ff, cj

def simulate_button(graph, ff, cj):
    count = {False:0, True:0}   # {low:0, high:0}
    # simulate 1000 button presses
    for _ in range(1000):
        q = deque([("button", "broadcaster", False)]) # (name, origin, pulse)
        while q:
            origin, curr, pulse = q.popleft()
            # increment low/high count
            count[pulse] += 1
            # skip
            if curr not in graph: continue
            # process pulse for flip flip module
            if curr in ff:
                # low pulse passed in
                if not pulse:
                    # flip state 
                    ff[curr] = not ff[curr]
                    new_pulse = ff[curr]    # high pulse if turned on, else low pulse
                    for next_module in graph[curr]:
                        q.append((curr, next_module, new_pulse))
            # process pulse for conjunction module
            elif curr in cj:
                cj[curr][origin] = pulse    # update pulse received
                new_pulse = not all(cj[curr].values())
                for next_module in graph[curr]:
                    q.append((curr, next_module, new_pulse))
            # is broadcaster
            else:
                for next_module in graph[curr]:
                    q.append((curr, next_module, pulse))
    return count[False] * count[True]

# part one
graph, ff, cj = parse_data(file)
print(f"The product of low and high pulse counts sent is {simulate_button(graph, ff, cj)}.")
# The product of low and high pulse counts sent is 711650489.

#part two
def simulate_button_part_2(graph, ff, cj):
    target, res = next((name for name, dest in graph.items() if "rx" in dest), None), []
    target_modules = [name for name, dest in graph.items() if target in dest]
    count = 1
    # simulate button presses
    while True:
        q = deque([("button", "broadcaster", False)]) # (name, origin, pulse)
        while q:
            origin, curr, pulse = q.popleft()
            # skip
            if curr not in graph: continue
            # at target module
            if not pulse and curr in target_modules:
                res.append(count)
                target_modules.remove(curr)
                if not target_modules: return res
            # process pulse for flip flip module
            if curr in ff:
                # low pulse passed in
                if not pulse:
                    # flip state 
                    ff[curr] = not ff[curr]
                    new_pulse = ff[curr]    # high pulse if turned on, else low pulse
                    for next_module in graph[curr]:
                        q.append((curr, next_module, new_pulse))
            # process pulse for conjunction module
            elif curr in cj:
                cj[curr][origin] = pulse    # update pulse received
                new_pulse = not all(cj[curr].values())
                for next_module in graph[curr]:
                    q.append((curr, next_module, new_pulse))
            # is broadcaster
            else:
                for next_module in graph[curr]:
                    q.append((curr, next_module, pulse))
        count += 1

# part two
graph, ff, cj = parse_data(file)
print(f"The fewest number of button presses required is {lcm(*simulate_button_part_2(graph, ff, cj))}.")
# The fewest number of button presses required is 219388737656593.