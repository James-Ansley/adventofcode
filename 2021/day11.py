from copy import deepcopy
from itertools import product


def get_adjacent(data, i, j):
    for dy, dx in product([-1, 0, 1], repeat=2):
        i1, j1 = i + dy, j + dx
        if 0 <= i1 < len(data) and 0 <= j1 < len(data[0]):
            yield i1, j1


def flash(data, flashes, i, j):
    flashes[i][j] = True
    for i1, j1 in get_adjacent(data, i, j):
        data[i1][j1] += 1
        if not flashes[i1][j1] and data[i1][j1] > 9:
            flash(data, flashes, i1, j1)


def step(data):
    next_ = [[0] * len(data[0]) for _ in range(len(data))]
    flashes = [[False] * len(data[0]) for _ in range(len(data))]
    for i, j in product(range(len(data)), range(len(data[0]))):
        next_[i][j] += data[i][j] + 1
        if next_[i][j] > 9:
            flash(next_, flashes, i, j)
    return [[0 if val > 9 else val for val in row] for row in next_]


with open('input_files/day11') as f:
    data = [[int(val) for val in line.strip()] for line in f]

board = deepcopy(data)
flashes = 0
for _ in range(100):
    board = step(board)
    flashes += sum(val == 0 for row in board for val in row)
print(flashes)

board = deepcopy(data)
steps = 0
while any(val for row in board for val in row):
    board = step(board)
    steps += 1
print(steps)
