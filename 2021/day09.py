from bisect import insort
from collections import deque
from itertools import product
from math import prod


def get_adjacent(data, i, j):
    adjacent = []
    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        i1, j1 = i + dy, j + dx
        if 0 <= i1 < len(data) and 0 <= j1 < len(data[0]):
            adjacent.append((i1, j1))
    return adjacent


def bfs(data, i, j):
    visited = [(i, j)]
    queue = deque(((i, j),))
    while queue:
        i, j = queue.pop()
        for i1, j1 in get_adjacent(data, i, j):
            if (i1, j1) not in visited and data[i1][j1] != 9:
                queue.appendleft((i1, j1))
                visited.append((i1, j1))
    return len(visited)


with open('input_files/day09') as f:
    data = [[int(value) for value in line.strip()] for line in f]

risks = []
basins = []
for i, j in product(range(len(data)), range(len(data[0]))):
    adjacent = get_adjacent(data, i, j)
    if all(data[i][j] < data[i1][j1] for (i1, j1) in adjacent):
        risks.append(data[i][j] + 1)
        insort(basins, bfs(data, i, j))

print(sum(risks))
print(prod(basins[-3:]))
