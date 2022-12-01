def adjacent(i, j, di, dj):
    return (i + di) % HEIGHT, (j + dj) % WIDTH


def step_facing(grid, facing, di, dj):
    next_grid = [line[:] for line in grid]
    for i, line in enumerate(grid):
        for j, elt in enumerate(line):
            if elt == facing:
                i1, j1 = adjacent(i, j, di, dj)
                if grid[i1][j1] == ".":
                    next_grid[i][j] = "."
                    next_grid[i1][j1] = facing
    return next_grid


def step(grid):
    grid = step_facing(grid, ">", 0, 1)
    grid = step_facing(grid, "v", 1, 0)
    return grid


with open("input_files/day25", "r") as f:
    grid = f.read().splitlines()

grid = [list(line) for line in grid]

WIDTH = len(grid[0])
HEIGHT = len(grid)

steps = 1
last_grid = grid
current_grid = step(grid)
while last_grid != current_grid:
    steps += 1
    current_grid, last_grid = step(current_grid), current_grid

print(steps)
