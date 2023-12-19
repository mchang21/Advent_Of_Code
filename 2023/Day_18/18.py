import os, numpy as np

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = [l.split() for l in f.read().strip().split('\n')]
    return data

def get_boundary(data, dirs, part1=True):
    x, y, n, boundary = 0, 0, 0, []
    for d, num, c in data:
        if part1:
            num = int(num)
        else:
            num, d = int(c[2:-2],16), int(c[-2])
        # get corner point
        dx,dy = dirs[d]
        x, y = x + (dx*num), y + (dy*num)
        boundary.append((x,y))
        n += num
    return boundary, n

def get_area(boundary):
    # ref: https://stackoverflow.com/a/30408825
    def PolyArea(x,y):
        return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
    x_coords, y_coords = [x for (x,_) in boundary], [y for (_,y) in boundary]
    return PolyArea(x_coords,y_coords)

# ref: https://en.wikipedia.org/wiki/Pick's_theorem#Formula
def get_inside(boundary, n):
    # i = area + 1 - (b//2)
    return int(get_area(boundary) + 1 - (n // 2))

def get_lagoon_size(data, dirs, part1):
    boundary, n = get_boundary(data, dirs, part1)
    inside = get_inside(boundary, n)
    return n + inside

data = parse_data(file)

# part one
dirs = {'R': ( 0, 1 ),'D': ( 1, 0 ),'L': ( 0,-1 ),'U': (-1, 0 )}
print(f"The lagoon can hold {get_lagoon_size(data, dirs, True)} cubic meters of lava.")
# The lagoon can hold 28911 cubic meters of lava.

# part two
dirs = [( 0, 1 ), ( 1, 0 ), ( 0,-1 ), (-1, 0 )]
print(f"The lagoon can hold {get_lagoon_size(data, dirs, False)} cubic meters of lava.")
# The lagoon can hold 77366737561114 cubic meters of lava.