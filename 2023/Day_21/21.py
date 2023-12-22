import os
from collections import deque

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().strip().split('\n')
    return data

def get_start(graph):
    for i, row in enumerate(graph):
        j =  row.find('S')
        if j != -1:
            return (i, j)
    return

def bfs(graph, start_x, start_y, max_steps):
    garden_plots, size = set(), len(graph)
    q, visited = deque([(start_x, start_y, max_steps)]), set((sr, sc))
    while q:
        i, j, s = q.popleft()
        # if steps is even, can end at this garden plot
        if not (s % 2):
            garden_plots.add((i,j))
        # skip
        if s == 0: continue
        # go to neighboring plot if not rock or visited
        for x, y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
            if 0 <= x%size < size and 0 <= y%size < size and (x,y) not in visited and graph[x%size][y%size] != '#':
                visited.add((x,y))
                q.append((x,y,s-1))
    return len(garden_plots)

graph = parse_data(file)
# part one
(sr, sc), steps = get_start(graph), 64
print(f"The Elf can reach {bfs(graph, sr, sc, steps)} garden plots in exactly {steps} steps.")

# part two
def quadratic(points, n):
    a = (points[2] - (2 * points[1]) + points[0]) // 2
    b = points[1] - points[0] - a
    c = points[0]
    return (a * n**2) + (b * n) + c

def part2(graph, steps):
    # coefficients for quadratic formula
    points = [bfs(graph, sr, sc, 65 + i * 131) for i in range(3)]
    size, edge = len(graph), len(graph) // 2
    n = (steps - edge) // size
    return quadratic(points, n)

# part two
steps = 26501365
print(f"The Elf can reach {part2(graph, steps)} garden plots in exactly {steps} steps.")