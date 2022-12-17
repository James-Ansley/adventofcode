def solve(positions, n):
    t_steps = [(0, 0)]
    for _ in range(n):
        t_steps = [(0, 0)]
        for h in positions:
            hx, hy, tx, ty = *h, *t_steps[-1]
            dx, dy = hx - tx, hy - ty
            if max(abs(dx), abs(dy)) > 1:
                dx, dy = max(-1, min(dx, 1)), max(-1, min(dy, 1))
                t_steps.append((tx + dx, ty + dy))
        positions = t_steps
    return len(set(t_steps))


with open("input_files/day09", "r") as f:
    data = f.read().splitlines()
    data = [line.split() for line in data]
    data = [(dir_, int(dist)) for dir_, dist in data]

dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
steps = [(0, 0)]
for dir_, dist in data:
    x, y, dx, dy = *steps[-1], *dirs[dir_]
    steps += [(x + dx * i, y + dy * i) for i in range(1, dist + 1)]

print(solve(steps, 1))
print(solve(steps, 9))
