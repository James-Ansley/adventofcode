import re


def shoot(dx, dy, x=0, y=0):
    if min_x <= x <= max_x and min_y <= y <= max_y:
        return True
    if x > max_x or y < min_y:
        return False
    return shoot(max(0, dx - 1), dy - 1, x+dx, y+dy)


with open('input_files/day17') as f:
    data = re.search(r'x=(\d+)..(\d+), y=(-?\d+)..(-?\d+)', f.read()).groups()
    min_x, max_x = int(data[0]), int(data[1])
    min_y, max_y = int(data[2]), int(data[3])

print(min_y * (min_y + 1) // 2)

total = 0
for dx in range(int(min_x ** 0.5), max_x + 1):
    for dy in range(min_y, -min_y + 1):
        total += shoot(dx, dy)
print(total)
