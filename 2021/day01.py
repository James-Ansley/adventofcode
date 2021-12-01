with open('input_files/day01') as f:
    data = [int(x) for x in f.read().splitlines()]

print(sum(x < y for x, y in zip(data, data[1:])))

windowed = [sum(data[i:i + 3]) for i in range(len(data) - 2)]
print(sum(x < y for x, y in zip(windowed, windowed[1:])))
