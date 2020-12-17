from itertools import product
from operator import add

with open('../input_files/day17') as f:
    data = [list(line) for line in f.read().split('\n')]


def run(dims):
    deltas = list(product((-1, 0, 1), repeat=dims))
    cells = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                coord = (i, j) + (0,) * (dims - 2)
                cells[coord] = 1

    for i in range(6):
        temp = {}
        for coord in cells.keys():
            n = sum(cells.get(tuple(map(add, coord, delta)), 0) for delta in deltas)
            if n == 3 or n == 4:
                temp[coord] = 1

            for neighbour in deltas:
                neighbour = tuple(map(add, coord, neighbour))
                if neighbour not in cells:
                    n = sum(cells.get(tuple(map(add, neighbour, delta)), 0) for delta in deltas)
                    if n == 3:
                        temp[neighbour] = 1
        cells = temp
    return len(cells)


print(run(3))
print(run(4))
