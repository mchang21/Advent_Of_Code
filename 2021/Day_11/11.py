import os

file = os.path.join(os.path.dirname(__file__), "input.txt")
sample = os.path.join(os.path.dirname(__file__), "sample.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().strip().split('\n')
        for i, d in enumerate(data):
            data[i] = list(map(int, d))
    return data

def get_neighbors(data, i,j):
    m,n = len(data), len(data[0])
    neighbors = []
    for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1), (i-1,j-1), (i-1,j+1), (i+1,j-1), (i+1,j+1)]:
        if 0 <= x < m and 0 <= y < n:
            neighbors.append((x,y))
    return neighbors

def simulate_flashes(data, steps, part2=False):
    m, n = len(data), len(data[0])
    total_flashes, k = 0, 1
    while k:
        flashed = []
        # increment each of the octopus' energy levels by 1
        for i in range(m):
            for j in range(n):
                data[i][j] += 1
                # if octopus flashed, increase neighboring octopus energy level
                if data[i][j] > 9:
                    flashed = get_neighbors(data, i,j)
                    data[i][j] = -9999
                # increase energy levels for neighbors
                while flashed:
                    x,y = flashed.pop()
                    data[x][y] += 1
                    if data[x][y] > 9:
                        data[x][y] = -9999
                        flashed.extend(get_neighbors(data, x,y))
                    
        # reset energy levels for octopus that flashed this step
        # and count flashes that occurred
        curr_flash = 0
        for i in range(m):
            for j in range(n):
                if data[i][j] < 0:
                    curr_flash += 1
                    data[i][j] = 0
        total_flashes += curr_flash
        # return part 1 answer
        if not part2 and k == steps:
            return total_flashes
        # return part 2 answer
        if part2 and curr_flash == m*n:
            return k
        k += 1

data = parse_data(file)
steps = 100
print(f"The total number of flashes after {steps} steps is {simulate_flashes(data, steps, False)}.")

data = parse_data(file)
print(f"The first step in which all octopuses flash is the {simulate_flashes(data, steps, True)}th step.")