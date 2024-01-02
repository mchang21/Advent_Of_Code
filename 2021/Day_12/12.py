import os
from collections import defaultdict

file = os.path.join(os.path.dirname(__file__), "input.txt")
sample = os.path.join(os.path.dirname(__file__), "sample.txt")

def parse_data(file):
    with open(file, 'r') as f:
        graph = defaultdict(list)
        edges = [cave.split('-') for cave in f.read().strip().split('\n')]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    return graph

def num_distinct_paths(graph, part2=False):
    def dfs(curr_node, can_visit_twice):
        if curr_node == "end":
            return 1
        paths = 0
        for neigh in graph[curr_node]:
            # small cave- can only visit once, track in visited
            if neigh.islower():
                if neigh not in visited_small:
                    visited_small.add(neigh)
                    paths += dfs(neigh, can_visit_twice)
                    visited_small.remove(neigh)
                # has been visited, want to visit twice
                elif can_visit_twice and neigh not in {"start", "end"}:
                    paths += dfs(neigh, False)
            # big cave -can visit multiple times
            else:
                paths += dfs(neigh, can_visit_twice)
        return paths
    visited_small = set(["start"])
    res = dfs("start", part2)
    return res

graph = parse_data(file)
print(f"The number of distinct paths in the graph for part one is {num_distinct_paths(graph, False)}.")
# The number of distinct paths in the graph for part one is 3450.

print(f"The number of distinct paths in the graph for part two is {num_distinct_paths(graph, True)}.")
# The number of distinct paths in the graph for part two is 96528.