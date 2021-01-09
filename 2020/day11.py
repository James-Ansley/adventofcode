def step_cell(neighbours):
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if data[i][j] != '.':
                n = neighbours(i, j)
                if vals[i][j] == 0 and n == 0:
                    temp[i][j] = 1
                if vals[i][j] == 1 and n >= 5:
                    temp[i][j] = 0


with open('input_files/day11') as f:
    data = [['.'] + list(line) + ['.'] for line in f.read().split()]

width = len(data[0])
data = [['.'] * width] + data + [['.'] * width]
height = len(data)


vals = [[0] * width for _ in range(height)]
while True:
    temp = [list(line) for line in vals]

    row_sum = [[sum(x) for x in zip(vals[i], vals[i][1:], vals[i][2:])] for i in range(height)]
    col_sum = [[sum(x) for x in zip(row_sum[i - 1], row_sum[i], row_sum[i + 1])] for i in range(1, height - 1)]

    step_cell(lambda i, j: col_sum[i - 1][j - 1])
    if temp == vals:
        break
    vals = temp

print(sum(x for line in vals for x in line))

edges = [[[] for _ in range(width)] for _ in range(height)]
for i in range(1, height - 1):
    for j in range(1, width - 1):
        for xd, yd in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
            y, x = i + yd, j + xd
            while 0 <= y < height and 0 <= x < width:
                if data[y][x] != '.':
                    edges[i][j].append((y, x))
                    break
                y, x = y + yd, x + xd

vals = [[0] * width for _ in data]
while True:
    temp = [list(line) for line in vals]
    step_cell(lambda i, j: sum(vals[y][x] for y, x in edges[i][j]))
    if temp == vals:
        break
    vals = temp

print(sum(x for line in vals for x in line))
