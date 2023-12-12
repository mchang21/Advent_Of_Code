import os
from collections import deque

file = os.path.join(os.path.dirname(__file__), "input.txt")

pipe_paths = {
    '|': [ 'N', 'S' ],
    '-': [ 'W', 'E' ],
    'L': [ 'N', 'E' ],
    'J': [ 'N', 'W' ],
    '7': [ 'S', 'W' ],
    'F': [ 'S', 'E' ],
    'S': [ 'N', 'S' ]
}
# directions = { "N": (-1,0), "W": (0,-1), "S": (1,0), "E": (0,1) }

def parse_data(file):
    with open(file, 'r') as f:
       data = [line for line in f.read().strip().split('\n')]
    return data

def get_start(graph):
    m,n = len(graph), len(graph[0])
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 'S':
                return (i,j)
            
def bfs(graph):
    pipe_paths = {
        '|': [ (-1, 0), ( 1, 0) ],
        '-': [ ( 0,-1), ( 0, 1) ],
        'L': [ ( 0, 1), (-1, 0) ],
        'J': [ (-1, 0), ( 0,-1) ],
        '7': [ ( 1, 0), ( 0,-1) ],
        'F': [ ( 1, 0), ( 0, 1) ],
        'S': [ (-1, 0), ( 1, 0) ]
    }
    m, n, start = len(graph), len(graph[0]), get_start(graph)
    q, visited, steps = deque([start]), set([start]), 0
    while q:
        for _ in range(len(q)):
            (x,y) = q.popleft()
            pipe = graph[x][y]
            # go in the direction depending on the current pipe type
            for (dx,dy) in pipe_paths[pipe]:
                i, j = x+dx, y+dy
                # skip if visited
                if (i,j) in visited: continue
                # add next direction to queue
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
                    visited.add((i,j))
                    q.append((i,j))
        steps += 1
        if len(q) == 1: break
    return steps, visited

graph =  parse_data(file)
steps, visited = bfs(graph)
# part one
print(f"The number of steps furthest from the starting position is {steps}.")
# The number of steps furthest from the starting position is 6909.

# part two
def count_enclosed_tiles(graph, visited):
    graph = [list(line) for line in graph]
    m, n, start = len(graph), len(graph[0]), get_start(graph)
    graph[start[0]][start[1]] = '|'     # hard code starting pipe
    count = 0
    for i in range(m):
        norths = 0
        for j in range(n):
            pipe = graph[i][j]
            # count number of north-facing pipes per line
            if (i,j) in visited:
                pipe_dirs = pipe_paths[pipe]
                if 'N' in pipe_dirs:
                    norths += 1
                continue
            if norths % 2:
                count += 1
    return count

# part two
print(f"The number of tiles enclosed by the loop is {count_enclosed_tiles(graph, visited)}.")
#The number of tiles enclosed by the loop is 461.
