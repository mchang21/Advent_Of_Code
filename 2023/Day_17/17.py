import os, heapq

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = [l for l in f.read().strip().split('\n')]
    return data

def minimum_heat_loss(graph, mn, mx):
    dirs = {
        ( 0, 0) : [( 1, 0), ( 0, 1)], # initial direction at (0,0)
        ( 0, 1) : [( 1, 0), (-1, 0)],
        ( 0,-1) : [( 1, 0), (-1, 0)],
        ( 1, 0) : [( 0, 1), ( 0,-1)],
        (-1, 0) : [( 0, 1), ( 0,-1)]
    }
    m, n = len(graph), len(graph[0])
    start = ( 0, (0,0), (0,0) ) # heat loss, (x,y), (dx,dy)
    q, visited = [start], set([start])

    # minimum cost to get to end
    while q:
        heat_loss, (x,y), (dx,dy) = heapq.heappop(q)
        # reached end
        if (x,y) ==  (m-1,n-1): return heat_loss
        # skip
        if (x,y,dx,dy) in visited: continue
        visited.add((x,y,dx,dy))
        # change directions
        for (di,dj) in dirs[(dx,dy)]:
            # initial values
            i, j, heat_cost = x, y, heat_loss
            # step in direction mx times
            for step in range(mx):
                i,j = i+di, j+dj
                if 0 <= i < m and 0 <= j < n:
                    heat_cost += int(graph[i][j])
                    # must go in same dir mn-1 times before it can change directions
                    if step >= mn-1:
                        heapq.heappush(q, (heat_cost, (i,j), (di,dj)))

graph = parse_data(file)

# part one
print(f"The least heat cost which incurs is {minimum_heat_loss(graph, 1, 3)}.")
# The least heat cost which incurs is 851.

# part two
print(f"The least heat cost which incurs is {minimum_heat_loss(graph, 4, 10)}.")
# The least heat cost which incurs is 982.