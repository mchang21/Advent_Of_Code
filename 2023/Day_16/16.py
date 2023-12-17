import os, sys

file = os.path.join(os.path.dirname(__file__), "input.txt")
sys.setrecursionlimit(10000)

def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().strip().split('\n')
    return data

def traverse(graph, x, y, dx, dy, visited):
    # index out of bounds
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]): return
    if (x,y,dx,dy) in visited: return
    visited.add((x,y,dx,dy))
    if graph[x][y] == '\\':
        # coming from left, move down
        if (dx,dy) == (0,1):
            traverse(graph, x+1, y, 1, 0, visited)
        # coming from top, move right
        elif (dx,dy) == (1,0):
            traverse(graph, x, y+1, 0, 1, visited)
        # coming from right, move up
        elif (dx,dy) == (0,-1):
            traverse(graph, x-1, y, -1, 0, visited)
        # coming from bottom, move left
        else:
            traverse(graph, x, y-1, 0, -1, visited)
    elif graph[x][y] == '/':
        # coming from left, move up
        if (dx,dy) == (0,1):
            traverse(graph, x-1, y, -1, 0, visited)
        # coming from top, move left
        elif (dx,dy) == (1, 0):
            traverse(graph, x, y-1, 0, -1, visited)
        # coming from right, move down
        elif (dx,dy) == (0, -1):
            traverse(graph, x+1, y, 1, 0, visited)
        # coming from bottom, move right
        else:
            traverse(graph, x, y+1, 0, 1, visited)
    elif graph[x][y] == '|':
        # traverse up
        traverse(graph, x-1, y, -1, 0, visited)
        # traverse down
        traverse(graph, x+1, y, 1, 0, visited)
    elif graph[x][y] == '-':
        # traverse left
        traverse(graph, x, y-1, 0, -1, visited)
        # traverse right
        traverse(graph, x, y+1, 0, 1, visited)
    else:
        traverse(graph, x+dx, y+dy, dx, dy, visited)
    return visited

def get_num_energized_tiles(visited):
    new_visited = set()
    for (x,y,_,_) in visited:
        new_visited.add((x,y))
    return len(new_visited)

graph = parse_data(file)
# part one
visited = traverse(graph, 0, 0, 0, 1, set())
print(f"The number of energized tiles is {get_num_energized_tiles(visited)}.")
# The number of energized tiles is 8125.

# part two
def get_maximum_energized_tiles(graph):
    m, n = len(graph), len(graph[0])
    max_energized_tiles = float('-inf')
    # start from top row, going downward
    # or bottom row, going upward
    for i in range(n):
        # print((0, i),(m-1,i))
        max_energized_tiles = max(max_energized_tiles, get_num_energized_tiles(traverse(graph, 0, i, 1, 0, set())))
        max_energized_tiles = max(max_energized_tiles, get_num_energized_tiles(traverse(graph, m-1, i, -1, 0, set())))
        # start from left column, going right
        # or right column, going left
    for i in range(m):
        max_energized_tiles = max(max_energized_tiles, get_num_energized_tiles(traverse(graph, i, 0, 0, 1, set())))
        max_energized_tiles = max(max_energized_tiles, get_num_energized_tiles(traverse(graph, i, n-1, 0, -1, set())))
    return max_energized_tiles

# part two
print(f"The beam configuration that energizes the largest number of tiles contains {get_maximum_energized_tiles(graph)} tiles.")
# The beam configuration that energizes the largest number of tiles contains 8489 tiles.