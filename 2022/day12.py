from collections import deque
from itertools import product

with open("input_files/day12", "r") as f:
    data = f.read().splitlines()
    data = [[ord(c) for c in line] for line in data]

S, E, A, Z = (ord(c) for c in "SEaz")
HEIGHTS, WIDTHS = range(len(data)), range(len(data[0]))

start = next((i, j) for i, j in product(HEIGHTS, WIDTHS) if data[i][j] == S)
end = next((i, j) for i, j in product(HEIGHTS, WIDTHS) if data[i][j] == E)

data[start[0]][start[1]] = A
data[end[0]][end[1]] = Z

deltas = (0, 1), (0, -1), (1, 0), (-1, 0)

distance = 0
best_spot = None
queue = deque([(end, 0)])
seen = {end}
while queue:
    (i, j), dist = queue.popleft()
    if (i, j) == start:
        distance = dist
        break
    if data[i][j] == A and best_spot is None:
        best_spot = dist

    children = ((i + di, j + dj) for di, dj in deltas)
    children = {(i1, j1) for i1, j1 in children
                if (i1 in HEIGHTS and j1 in WIDTHS
                    and (i1, j1) not in seen
                    and data[i][j] - data[i1][j1] <= 1)}

    queue.extend((pos, dist + 1) for pos in children)
    seen |= children

print(distance)
print(best_spot)
