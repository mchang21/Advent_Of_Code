from collections import deque

PATH = '../Advent_Of_Code/2022/Day_12/'
# part one
def parse(filename):
    with open(filename) as f:
        graph = [[l for l in line] for line in f.read().strip().split()]
    return graph

def bfs(graph, src, dest):
    m, n = len(graph), len(graph[0])
    # mapping of each letter to its elevation
    elevation = {chr(i): i - 96 for i in range(97, 97 + 26)}
    elevation['S'] = 1
    elevation['E'] = 26
    # bfs
    q, visited, steps = deque([src]), set([src]), 0
    while q:
        for _ in range(len(q)):
            i,j = q.popleft()
            # reached destination
            if (i,j) == dest: return steps
            curr = graph[i][j]
            # get each neighbor
            for (x,y) in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                # check if within bounds and not visited
                if 0 <= x < m and 0 <= y < n and (x,y) not in visited:
                    nxt = graph[x][y]
                    # check if elevation is within 1
                    if elevation[nxt] - elevation[curr] <= 1:
                        visited.add((x,y))
                        q.append((x,y))
        steps += 1
    # no path possible
    return float('inf')

# parse the graph
graph = parse(PATH + "input.txt")
m,n = len(graph), len(graph[0])
# find start and end positions
src, dest  = None, None
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'S':
            src = (i,j)
        if graph[i][j] == 'E':
            dest = (i,j)

# part two
# find all possible starting points
starts = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'a' or graph[i][j] == 'S':
            starts.append((i,j))
# use bfs from all starting points and record the best answer
min_steps = float('inf')
for src in starts:
    min_steps = min(min_steps, bfs(graph, src, dest))

# part one 
print(f"The minimum number of steps taken is {bfs(graph, src, dest)}\n")
# part two
print(f"The minimum number of steps taken is {min_steps}\n")
