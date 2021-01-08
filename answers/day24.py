from collections import defaultdict
from operator import add

with open('../input_files/day24') as f:
    data = f.read()
    for direction, val in ('se', '1'), ('sw', '2'), ('nw', '4'), ('ne', '5'), ('e', '0'), ('w', '3'):
        data = data.replace(direction, val)
    data = data.split('\n')

deltas = (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)

for i, row in enumerate(data):
    x = sum(deltas[c][0] for c in map(int, row))
    y = sum(deltas[c][1] for c in map(int, row))
    data[i] = (x, y)

tiles = defaultdict(bool)
for row in data:
    tiles[row] = not tiles[row]

print(sum(tiles.values()))

tiles = set(key for key, val in tiles.items() if val)
for _ in range(100):
    temp = set()
    for tile in tiles:
        n = sum(tuple(map(add, tile, delta)) in tiles for delta in deltas)
        if n == 1 or n == 2:
            temp.add(tile)
        for neighbour in deltas:
            neighbour = tuple(map(add, tile, neighbour))
            if neighbour not in tiles:
                n = sum(tuple(map(add, neighbour, delta)) in tiles for delta in deltas)
                if n == 2:
                    temp.add(neighbour)
    tiles = temp

print(len(tiles))
