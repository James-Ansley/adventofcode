import re
from collections import defaultdict
from itertools import repeat


def make_range(a, b, c, d):
    if a == b:
        return repeat(a, abs(c - d) + 1)
    if a > b:
        return range(a, b - 1, -1)
    return range(a, b + 1)


def is_orthogonal(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2


def points(x1, y1, x2, y2):
    return zip(make_range(x1, x2, y1, y2), make_range(y1, y2, x1, x2))


with open('input_files/day05') as f:
    lines = re.findall(r'(\d+),(\d+) -> (\d+),(\d+)\n', f.read())
    lines = [[int(x) for x in line] for line in lines]

orthogonal_overlaps = defaultdict(int)
overlaps = defaultdict(int)
for line in lines:
    for point in points(*line):
        overlaps[point] += 1
        orthogonal_overlaps[point] += is_orthogonal(*line)

print(sum(overlap > 1 for overlap in orthogonal_overlaps.values()))
print(sum(overlap > 1 for overlap in overlaps.values()))
