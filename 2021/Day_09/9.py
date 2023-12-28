import os

file = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().strip().split('\n')
        for i, line in enumerate(data):
            data[i] = list(map(int, line))
    return data

def sum_risk_level(data):
    m,n = len(data), len(data[0])
    low_points = []
    for i in range(m):
        for j in range(n):
            lowest = []
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n:
                    lowest.append(data[i][j] < data[x][y])
            if all(lowest):
                low_points.append(data[i][j])
    return sum(low_points) + len(low_points)

data = parse_data(file)
print(f"The sum of the risk levels of all low points in the heightmap is {sum_risk_level(data)}.")

def get_basins(data):
    m,n = len(data), len(data[0])
    basins = []
    for i in range(m):
        for j in range(n):
            lowest = []
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n:
                    lowest.append(data[i][j] < data[x][y])
            if all(lowest):
                basins.append((i,j))
    return basins

def multiply_three_largest(data, basins):
    def dfs(x,y):
        for i, j in [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]:
            if 0 <= i < m and 0 <= j < n and (i,j) not in visited and data[i][j] != 9:
                visited.add((i,j))
                dfs(i,j)
        return
    m, n = len(data), len(data[0])
    sizes = []
    for (x,y) in basins:
        visited = set([(x,y)])
        dfs(x,y)
        sizes.append(len(visited))
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]

basins = get_basins(data)
print(f"The product of the three largest sizes is {multiply_three_largest(data, basins)}.")