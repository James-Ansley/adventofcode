import re
from collections import Counter


def get_intersection(cube1, cube2):
    x1, x2, y1, y2, z1, z2 = cube1
    x3, x4, y3, y4, z3, z4 = cube2
    ox1 = max(x1, x3)
    ox2 = min(x2, x4)
    oy1 = max(y1, y3)
    oy2 = min(y2, y4)
    oz1 = max(z1, z3)
    oz2 = min(z2, z4)
    if ox1 <= ox2 and oy1 <= oy2 and oz1 <= oz2:
        return ox1, ox2, oy1, oy2, oz1, oz2


def get_area(cube):
    x1, x2, y1, y2, z1, z2 = cube
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)


def run(ranges):
    cubes = Counter()
    for setting, *cube in ranges:
        temp = Counter()
        if setting > 0:
            temp[tuple(cube)] = setting
        for other_cube, other_setting in cubes.items():
            intersection = get_intersection(cube, other_cube)
            if intersection:
                temp[intersection] -= other_setting
        cubes.update(temp)
    return sum(get_area(cube) * setting for cube, setting in cubes.items())


pattern = r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'
with open('input_files/day22') as f:
    ranges = re.findall(pattern, f.read())
    ranges = [(line[0], *(int(x) for x in line[1:])) for line in ranges]
    ranges = [(1 if line[0] == 'on' else -1, *line[1:]) for line in ranges]

core_ranges = [line for line in ranges if all(x < 50 for x in line[1:])]
core_ranges = [line for line in core_ranges if all(x > -50 for x in line[1:])]

print(run(core_ranges))
print(run(ranges))
