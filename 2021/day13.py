import re


def fold(axis, coordinate, points):
    new_points = set()
    for x, y in points:
        if axis == 'x' and x > coordinate:
            new_points.add((coordinate * 2 - x, y))
        elif axis == 'y' and y > coordinate:
            new_points.add((x, coordinate * 2 - y))
        else:
            new_points.add((x, y))
    return new_points


def print_grid(points):
    max_x = max(x for x, _ in points) + 1
    max_y = max(y for _, y in points) + 1
    for y in range(max_y):
        row = ('#' if (x, y) in points else ' ' for x in range(max_x))
        print(' '.join(row))


with open('input_files/day13') as f:
    points, folds = f.read().split('\n\n')

points = re.findall(r'(\d+),(\d+)', points)
points = {(int(x), int(y)) for x, y in points}
folds = re.findall(r'fold along ([xy])=(\d+)', folds)
folds = [(axis, int(coordinate)) for axis, coordinate in folds]

print(len(fold(*folds[0], points)))

for axis, coordinate in folds:
    points = fold(axis, coordinate, points)
print_grid(points)
