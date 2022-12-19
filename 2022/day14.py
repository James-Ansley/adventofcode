import re
from itertools import count, pairwise, product


def fall(sx, sy, grid, lowest_point):
    if (500, 0) in grid:
        return None
    for y in range(sy, lowest_point + 1):
        if (sx, y) in grid:
            if (sx - 1, y) not in grid:
                return fall(sx - 1, y, grid, lowest_point)
            elif (sx + 1, y) not in grid:
                return fall(sx + 1, y, grid, lowest_point)
            else:
                return sx, y - 1


def run(grid):
    grid = set(grid)
    lowest_point = max(p[1] for p in grid)
    for i in count(0):
        stopped_at = fall(500, 0, grid, lowest_point)
        if stopped_at is None:
            return i
        grid.add(stopped_at)


with open("input_files/day14", "r") as f:
    data = f.read().splitlines()
    data = [re.findall(r"(\d+),(\d+)", line) for line in data]
    data = [[(int(v1), int(v2)) for v1, v2 in line] for line in data]

points = set()
for line in data:
    for start, end in pairwise(line):
        (x1, x2), (y1, y2) = (sorted(pair) for pair in zip(start, end))
        points.update(product(range(x1, x2 + 1), range(y1, y2 + 1)))

lowest_point = max(p[1] for p in points) + 2
left, right = 500 - lowest_point, 501 + lowest_point
inf_floor = {(i, lowest_point) for i in range(left, right)}

print(run(points))
print(run(points | inf_floor))
