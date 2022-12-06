with open("input_files/day06", "r") as f:
    data = f.read()

fours = [set(data[i:i+4]) for i in range(len(data))]
fourteens = [set(data[i:i + 14]) for i in range(len(data))]

idx4 = next(i + 4 for i, window in enumerate(fours) if len(window) == 4)
idx14 = next(i + 14 for i, window in enumerate(fourteens) if len(window) == 14)

print(idx4)
print(idx14)
