import os

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = [line.strip().split(' -> ') for line in f.read().strip().split('\n')]
        for d in data:
            for i,coord in enumerate(d):
                d[i] = tuple(map(int, coord.split(',')))
    return data

def place_rocks(data):
    rocks = set()
    for d in data:
        for (x1, y1), (x2, y2) in zip(d, d[1:]):
            flipped = False
            if y1 == y2:
                x1, x2, y1, y2 = y1, y2, x1, x2
                flipped = True
            for j in range(min(y1,y2), max(y1,y2)+1):
                if flipped:
                    rocks.add((j, x1))
                else:
                    rocks.add((x1, j))
    return rocks

def simulate_sand_fall(rocks, part_2=False):
    # find abyss level
    max_y = float('-inf')
    for (_,y) in rocks: max_y = max(max_y, y if not part_2 else y+2)
    sand = 0
    # simulate until cannot add more sand
    while True:
        # initial sand position
        x,y = 500, 0
        # simulate sand falling
        while True:
            if part_2:
                if (x,y) in rocks:
                    return sand
            # reached abyss
            if y >= max_y:
                rocks.add((x,y))
                if part_2:
                    break
                return sand
            # check down
            if (x,y+1) not in rocks:
                y +=1
            # check down-left
            elif (x-1,y+1) not in rocks:
                x -= 1; y += 1
            # check down-right
            elif (x+1,y+1) not in rocks:
                x += 1; y += 1
            # stopped falling
            else:
                rocks.add((x,y))
                sand += 1
                break

data = parse_data(file)
rocks = place_rocks(data)
# part one
print(f"The amount of sand that will come to rest is {simulate_sand_fall(rocks)}.")
# part two
rocks = place_rocks(data)
print(f"The amount of sand that will come to rest is {simulate_sand_fall(rocks, True)}.")


