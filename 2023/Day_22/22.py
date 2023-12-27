import os
from collections import defaultdict

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        bricks = f.read().strip().split('\n')
        for i, brick in enumerate(bricks):
            s,e = brick.split("~")
            sx, sy, sz = list(map(int, s.split(",")))
            ex, ey, ez = list(map(int, e.split(",")))
            assert sx <= ex; assert sy <= ey; assert sz <= ez
            bricks[i] = ([sx,sy,sz], [ex,ey,ez])
    return bricks

# given a brick, find its final position
def drop_brick(brick, heights):
    # new z = start z - delta z
    (sx, sy, sz), (ex, ey, ez) = brick
    coords = [(x,y) for x in range(sx, ex+1) for y in range(sy, ey+1)]
    # max_z = max(heights[xy] for xy in coords)
    max_z = max(heights.get(xy, 0) for xy in coords)
    dz = max(sz - max_z - 1, 0)
    # return start coords, end coords of dropped brick
    return ([sx, sy, sz-dz], [ex, ey, ez-dz])

def simulate_fall(bricks):
    bricks.sort(key=lambda b: b[0][2])
    heights, settled, falls = defaultdict(int), [], 0
    for b in bricks:
        (sx, sy, sz), (ex, ey, _) = b
        settled_brick = drop_brick(b, heights)
        settled.append(settled_brick)
        # brick fell
        if settled_brick[0][2] != sz:
            falls += 1
        # update max height
        for x in range(sx, ex+1):
            for y in range(sy, ey+1):
                heights[(x,y)] = settled_brick[1][2] # set max height to end_z
    return falls, settled

def count_disintegrated_and_fallen(bricks):
    disintegrated, chain_fall, n = 0, 0, len(bricks)
    for i in range(n):
        # remove brick i, check if any bricks fall becuase of brick i
        falls, _ = simulate_fall(bricks[:i]+bricks[i+1:])
        # part one
        if not falls:
            disintegrated += 1
        # part two
        else:
            chain_fall += falls
    return disintegrated, chain_fall

bricks = parse_data(file)
_, settled = simulate_fall(bricks)
# part one / part two
disintegrated, fallen = count_disintegrated_and_fallen(settled)
print(f"The number of bricks that can be disintegrated is {disintegrated}.")
# The number of bricks that can be disintegrated is 459.
print(f"The number of other bricks that will fall is {fallen}.")
# The number of other bricks that will fall is 75784.