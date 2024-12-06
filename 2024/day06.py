from collections import defaultdict

with open("input_files/day06", "r") as f:
    data = f.read()

start_idx = data.find("^")
grid = data.splitlines()
width, height = len(grid[0]), len(grid)
start = start_idx // (width + 1), start_idx % (width + 1)


def run(block=None):
    seen = defaultdict(set)
    di, dj = -1, 0
    i, j = start
    while 0 <= i < width and 0 <= j < height and (di, dj) not in seen[(i, j)]:
        seen[(i, j)].add((di, dj))
        i1, j1 = i + di, j + dj
        if (0 <= i1 < height and 0 <= j1 < width
              and (grid[i1][j1] == "#" or (i1, j1) == block)):
            di, dj = dj, -di
        else:
            i, j = i1, j1
    return seen, 0 <= i < width and 0 <= j < height


blocks, _ = run()
total = sum(run(b)[1] for b in blocks)

print(len(blocks))
print(total)
