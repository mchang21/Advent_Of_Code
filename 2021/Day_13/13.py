import os

file = os.path.join(os.path.dirname(__file__), "input.txt")
sample = os.path.join(os.path.dirname(__file__), "sample.txt")

def parse_data(file):
    with open(file, 'r') as f:
        points, folds = f.read().strip().split('\n\n')
        points = [tuple(map(int, point.split(','))) for point in points.strip().split('\n')]
        folds = [tuple(f[-1].split('=')) for fold in folds.strip().split('\n') for f in [fold.split()]]
    return points, folds

def get_new_points(points, axis, val):
    new_points = set()
    match axis:
        case 'x':
            for (x,y) in points:
                if x < val: new_points.add((x,y))
                else:
                    dx = 2*(x-val)
                    new_points.add((x-dx,y))
        case 'y':
            for (x,y) in points:
                if y < val: new_points.add((x,y))
                else:
                    dy = 2*(y-val)
                    new_points.add((x,y-dy))
    return list(new_points)

def fold_paper(folds, points):
    for axis, val in folds:
        points = get_new_points(points, axis, int(val))
    return points

points, folds = parse_data(file)
# part one
axis, val = folds[0]
print(f"The number of points visible after the first fold is {len(get_new_points(points, axis, int(val)))}.")

# part two
print("The code for the infrared thermal imaging camera system is:")
final = fold_paper(folds, points)
d = [[' ' for _ in range(40)] for _ in range(6)]
for x,y in final:
    d[y][x] = '#'
for line in d:
    print(''.join(line))
