with open('input_files/day02') as f:
    data = [line.split() for line in f]
    data = [(direction, int(delta)) for direction, delta in data]

x, y, y1 = 0, 0, 0
for direction, delta in data:
    match direction:
        case 'forward':
            x += delta
            y1 += y * delta
        case 'up':
            y -= delta
        case 'down':
            y += delta

print(x * y)
print(x * y1)
