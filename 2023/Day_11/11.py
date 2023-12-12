import os

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
       data = [line for line in f.read().strip().split('\n')]
    return data

def find_empty_lines(graph):
    m, n = len(graph), len(graph[0])
    rows, cols = [], []
    for r in range(m):
        if all([graph[r][c] == '.' for c in range(n)]):
            rows.append(r)
    for c in range(n):
        if all([graph[r][c] == '.' for r in range(m)]):
            cols.append(c)
    return rows, cols

def transpose_graph(graph):
    transposed = []
    m, n = len(graph), len(graph[0])
    for c in range(n):
        col = []
        for r in range(m):
            col.append(graph[r][c])
        transposed.append(''.join(col))
    return transposed

def get_galaxies(graph, rows, cols, factor):
    m, n = len(graph), len(graph[0])
    galaxies = []
    # get original pos of the galaxies
    for i in range(m):
        for j in range(n):
            if graph[i][j] == '#':
                galaxies.append((i,j))
    # calculate new pos after row/col insertions
    for i, galaxy in enumerate(galaxies):
        x,y = galaxy
        dx = sum([galaxy[0] > row for row in rows])
        dy = sum([galaxy[1] > col for col in cols])
        new_x, new_y = x + (dx*factor), y + (dy*factor)
        galaxies[i] = (new_x,new_y)
    return galaxies

def sum_shortest_paths(galaxies):
    sum_dist = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            (x1,y1), (x2,y2) = galaxies[i], galaxies[j]
            sum_dist += abs(x1-x2) + abs(y1-y2)
    return sum_dist

graph = parse_data(file)
# find rows/cols with no galaxies
rows, cols = find_empty_lines(graph)
# get galaxy positions in the expanded universe
galaxies = get_galaxies(graph, rows, cols, 1)
print(f"The sum of the shortest path between all pairs of galaxies is {sum_shortest_paths(galaxies)}.")
# The sum of the shortest path between all pairs of galaxies is 9591768.

# part two
galaxies = get_galaxies(graph, rows, cols, 999_999)
print(f"The sum of the shortest path between all pairs of galaxies is {sum_shortest_paths(galaxies)}.")
# The sum of the shortest path between all pairs of galaxies is 746962097860.