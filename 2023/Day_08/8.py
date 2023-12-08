PATH = '../Advent_Of_Code/2023/Day_08/'
import collections, math

def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().strip().split('\n\n')
        instructions = data[0]
        edges = []
        for edge in data[1].split('\n'):
            edges.append(edge.replace('=', ' ').replace('(',' ').replace(')',' ').replace(',',' ').split())
    return instructions, edges

def create_graph(edges):
    graph = collections.defaultdict(list)
    for root, left, right in edges:
        graph[root].extend([left,right])
    return graph

def calculate_steps(graph, instructions):
    curr, i, steps = 'AAA', 0, 0
    # dfs
    while curr != 'ZZZ':
        next_node = 0 if instructions[i] == 'L' else 1
        curr = graph[curr][next_node]
        steps += 1
        i = (i+1) % len(instructions)
    return steps

# part one
instructions, edges = parse_data(PATH + "input.txt")
graph = create_graph(edges)
print(f"The number of steps required to reach 'ZZZ' is {calculate_steps(graph,instructions)}.")
# The number of steps required to reach 'ZZZ' is 18827.

# part two
def calculate_steps_part_2(graph, edges, instructions):
    starts = [edge[0] for edge in edges if 'A' in edge[0]]
    lcm, i = 1, 0
    # dfs for each start
    for start in starts:
        curr, steps = start, 0
        # end when we reach a node ending with 'Z'
        while not curr.endswith('Z'):
            next_node = 0 if instructions[i] == 'L' else 1
            curr = graph[curr][next_node]
            steps += 1
            i = (i+1) % len(instructions)
        # find lowest common multiple between all starts
        lcm = math.lcm(lcm, steps)
    return lcm

print(f"The number of steps is takes to simultaneously reach nodes that end with 'Z' is {calculate_steps_part_2(graph, edges, instructions)}.")
# The number of steps is takes to simultaneously reach nodes that end with 'Z' is 20220305520997.
