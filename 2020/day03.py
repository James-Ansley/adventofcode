with open('input_files/day03') as f:
    data = f.read().split()

width = len(data[0])
print(sum(data[i][(i * 3) % width] == '#' for i in range(len(data))))

prod = 1
for xd, yd in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    prod *= sum(data[i * yd][(i * xd) % width] == '#' for i in range(len(data) // yd))
print(prod)
