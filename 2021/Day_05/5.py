PATH = '../Advent_Of_Code/2021/Day_05/'
import collections, numpy
# part one
def parse_data(file):
    with open(file, 'r') as f:
        data = f.read().split('\n')
        for i, row in enumerate(data):
            data[i] = row.strip().split(" -> ")
            for j, point in enumerate(data[i]):
                data[i][j] = [int(p) for p in point.split(',')]
    return data

def mark_points(marked_points, x1, y1, x2, y2):
    flipped = False
    if y1 == y2 and x1 != x2:
        x1, x2, y1, y2 = y1, y2, x1, x2
        flipped = True

    for j in range(min(y1, y2), max(y1, y2)+1):
        if flipped:
            marked_points[(j,x1)] += 1
        else:
            marked_points[(x1,j)] += 1
    return

def mark_diagonals(marked_points, x1, y1, x2, y2):
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    # diagonals are guaranteed to be 45 degrees
    slope = (y2-y1) // (x2-x1)  # either 1 or -1
    dx, dy = numpy.sign(x2-x1), numpy.sign(y2-y1) # adjust range according to orientation
    for i,j in zip(range(x1, x2+dx), range(y1,y2+dy,slope)):
        marked_points[(i,j)] += 1

def count_overlap(data, include_diagonals=False):
    marked_points = collections.defaultdict(int)
    for points in data:
        x1,y1 = points[0]
        x2,y2 = points[1]
        # mark horizontals/verticals
        if x1==x2 or y1==y2:
            mark_points(marked_points, x1, y1, x2, y2)
        # mark diagonals
        elif include_diagonals:
            mark_diagonals(marked_points, x1, y1, x2, y2)
    
    overlap = 0
    for num in marked_points.values():
        overlap += 1 if num >= 2 else 0

    return overlap

data = parse_data(PATH + "input.txt")
# part one
print(f"The number of points where at least two horizontal/vertical lines overlap is {count_overlap(data)}.")
# part two
print(f"The number of points where at least two horizontal/vertical/diagonal lines overlap is {count_overlap(data, True)}.")
